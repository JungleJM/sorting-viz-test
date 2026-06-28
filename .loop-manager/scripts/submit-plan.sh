#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  .loop-manager/scripts/submit-plan.sh [options]

Find a PlanContract under specs/, run spec-planning verification, and submit the
plan to Loop Manager on Bluefin.

Options:
  --plan PATH          Use this plan-contract YAML file.
  --feature SLUG      Use specs/SLUG/plan-contract.bluefin.yaml.
  --api-url URL       Loop Manager API URL.
                       Default: $LOOP_MANAGER_API_URL or http://bluefin.tail90eacc.ts.net:8010
  --profile ID        Optional Loop Manager profile_id.
  --latest            If multiple plans exist, choose the newest one.
  --skip-verify       Do not run .loop-manager/scripts/verify-spec-planning.sh first.
  --dry-run           Discover, verify, and parse the plan, but do not POST.
  -v                  Verbose output.
  -vv                 Very verbose output, including response JSON summary.
  -h, --help          Show this help.

Environment:
  LOOP_MANAGER_API_URL
  LOOP_MANAGER_PROFILE_ID
  LOOP_MANAGER_DASHBOARD_URL
  PAPERCLIP_DASHBOARD_URL
  PAPERCLIP_EVENTS_URL
EOF
}

log() {
  printf '%s\n' "$*"
}

verbose() {
  if (( verbosity >= 1 )); then
    log "$@"
  fi
}

very_verbose() {
  if (( verbosity >= 2 )); then
    log "$@"
  fi
}

die() {
  printf 'submit-plan: %s\n' "$*" >&2
  exit 1
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "required command not found: $1"
}

json_escape() {
  ruby -rjson -e 'print JSON.generate(ARGV[0])' "$1"
}

plan_to_json() {
  local plan_path="$1"
  ruby -ryaml -rjson -e '
    path = ARGV.fetch(0)
    data = YAML.load_file(path)
    print JSON.generate(data)
  ' "$plan_path"
}

pick_plan_interactive() {
  local count="$1"
  if [[ ! -t 0 ]]; then
    log "Multiple PlanContracts found:"
    printf '  %s\n' "${found[@]}"
    die "use --plan PATH, --feature SLUG, or --latest"
  fi

  log "Multiple PlanContracts found:"
  local i
  for ((i = 0; i < count; i++)); do
    printf '  [%d] %s\n' "$((i + 1))" "${found[$i]}"
  done
  printf 'Choose a plan number: '
  local choice
  read -r choice
  [[ "$choice" =~ ^[0-9]+$ ]] || die "invalid selection: $choice"
  (( choice >= 1 && choice <= count )) || die "selection out of range"
  printf '%s\n' "${found[$((choice - 1))]}"
}

find_plan() {
  if [[ -n "$plan_path" ]]; then
    [[ -f "$plan_path" ]] || die "plan file not found: $plan_path"
    printf '%s\n' "$plan_path"
    return
  fi

  if [[ -n "$feature_slug" ]]; then
    local candidate="specs/$feature_slug/plan-contract.bluefin.yaml"
    [[ -f "$candidate" ]] || die "feature plan not found: $candidate"
    printf '%s\n' "$candidate"
    return
  fi

  found=()
  while IFS= read -r item; do
    found+=("$item")
  done < <(find specs -path '*/plan-contract.bluefin.yaml' -type f 2>/dev/null | sort)
  ((${#found[@]} > 0)) || die "no plan-contract.bluefin.yaml found under specs/"

  if ((${#found[@]} == 1)); then
    printf '%s\n' "${found[0]}"
    return
  fi

  if [[ "$choose_latest" == "true" ]]; then
    ls -t "${found[@]}" | head -1
    return
  fi

  pick_plan_interactive "${#found[@]}"
}

response_summary() {
  ruby -rjson -e '
    data = JSON.parse(STDIN.read)
    puts "Plan: #{data["plan_id"]} — #{data["title"]}"
    puts "Tasks: #{data["task_count"]}"
    puts "Stopped early: #{data["stopped_early"]}"
    if data["stop_reason"] && !data["stop_reason"].empty?
      puts "Stop reason: #{data["stop_reason"]}"
    end
    puts "Run IDs:"
    Array(data["run_ids"]).each { |id| puts "  - #{id}" }
  '
}

response_plan_id() {
  ruby -rjson -e 'print JSON.parse(STDIN.read)["plan_id"]'
}

plan_path=""
feature_slug=""
profile_id="${LOOP_MANAGER_PROFILE_ID:-}"
api_url="${LOOP_MANAGER_API_URL:-http://bluefin.tail90eacc.ts.net:8010}"
dashboard_url="${LOOP_MANAGER_DASHBOARD_URL:-}"
paperclip_dashboard_url="${PAPERCLIP_DASHBOARD_URL:-http://100.102.1.117:3100/}"
paperclip_events_url="${PAPERCLIP_EVENTS_URL:-http://bluefin.tail90eacc.ts.net:3199/events?limit=25}"
choose_latest=false
skip_verify=false
dry_run=false
verbosity=0

while (($#)); do
  case "$1" in
    --plan)
      shift
      plan_path="${1:-}"
      [[ -n "$plan_path" ]] || die "--plan requires a path"
      ;;
    --feature)
      shift
      feature_slug="${1:-}"
      [[ -n "$feature_slug" ]] || die "--feature requires a slug"
      ;;
    --api-url)
      shift
      api_url="${1:-}"
      [[ -n "$api_url" ]] || die "--api-url requires a URL"
      ;;
    --profile)
      shift
      profile_id="${1:-}"
      [[ -n "$profile_id" ]] || die "--profile requires an ID"
      ;;
    --latest)
      choose_latest=true
      ;;
    --skip-verify)
      skip_verify=true
      ;;
    --dry-run)
      dry_run=true
      ;;
    -v)
      verbosity=$((verbosity + 1))
      ;;
    -vv)
      verbosity=$((verbosity + 2))
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
  shift
done

require_cmd curl
require_cmd ruby

[[ -d specs ]] || die "run this from a target repo that has a specs/ directory"
[[ -d .loop-manager ]] || die "run this from a target repo that has .loop-manager/"

api_url="${api_url%/}"
if [[ -z "$dashboard_url" ]]; then
  dashboard_url="$api_url"
fi

selected_plan="$(find_plan)"
verbose "Selected plan: $selected_plan"

if [[ "$skip_verify" != "true" ]]; then
  [[ -x .loop-manager/scripts/verify-spec-planning.sh ]] || \
    die ".loop-manager/scripts/verify-spec-planning.sh is missing or not executable"
  log "Running spec-planning verification..."
  .loop-manager/scripts/verify-spec-planning.sh
else
  log "Skipping spec-planning verification."
fi

plan_json="$(plan_to_json "$selected_plan")"
if [[ -n "$profile_id" ]]; then
  payload="{\"plan_contract\":$plan_json,\"profile_id\":$(json_escape "$profile_id")}"
else
  payload="{\"plan_contract\":$plan_json}"
fi

very_verbose "Submitting payload built from: $selected_plan"
log "Dashboard: $dashboard_url"
log "Paperclip dashboard: $paperclip_dashboard_url"
log "Paperclip events: $paperclip_events_url"

if [[ "$dry_run" == "true" ]]; then
  log "Dry run complete. Plan parsed successfully; no POST was sent."
  exit 0
fi

log "Checking Loop Manager health: $api_url/health"
curl -fsS "$api_url/health" >/dev/null

log "Checking Loop Manager worker/model inventory: $api_url/worker-models"
worker_models_file="$(mktemp)"
worker_model_status="$(
  curl -sS -o "$worker_models_file" -w "%{http_code}" \
    "$api_url/worker-models"
)"
if [[ "$worker_model_status" != "200" ]]; then
  cat "$worker_models_file" >&2
  rm -f "$worker_models_file"
  die "worker/model inventory failed with HTTP $worker_model_status"
fi
if (( verbosity >= 1 )); then
  ruby -rjson -e '
    data = JSON.parse(File.read(ARGV.fetch(0)))
    puts "Available worker/model profiles:"
    Array(data["workers"]).each do |worker|
      profiles = (worker["model_profiles"] || {}).map do |name, profile|
        "#{name}=#{profile["model"]}"
      end
      puts "  - #{worker["worker"]} (#{worker["role"]}): #{profiles.join(", ")}"
    end
  ' "$worker_models_file"
fi
rm -f "$worker_models_file"

log "Submitting plan to: $api_url/plans"
log "Note: current Loop Manager /plans requests are synchronous; this command may stay open until the plan stops or completes."

response_file="$(mktemp)"
status="$(
  curl -sS -o "$response_file" -w "%{http_code}" \
    -X POST "$api_url/plans" \
    -H "content-type: application/json" \
    -d "$payload"
)"

if [[ "$status" != "201" ]]; then
  cat "$response_file" >&2
  rm -f "$response_file"
  die "submission failed with HTTP $status"
fi

response="$(cat "$response_file")"
rm -f "$response_file"

log "Submission accepted."
response_summary <<<"$response"
submitted_plan_id="$(response_plan_id <<<"$response")"
log "Plan dashboard: $dashboard_url/plans/$submitted_plan_id"

if (( verbosity >= 2 )); then
  log "Raw response JSON:"
  ruby -rjson -e 'puts JSON.pretty_generate(JSON.parse(STDIN.read))' <<<"$response"
fi
