#!/usr/bin/env bash
set -euo pipefail

if [[ -n "${LOOP_MANAGER_REPO_DIR:-}" ]]; then
  loop_manager_repo="$LOOP_MANAGER_REPO_DIR"
else
  candidates=(
    "/var/home/j/code/loop-manager"
    "/Users/jmath/Documents/code/loop-manager"
    "$HOME/code/loop-manager"
    "$HOME/Documents/code/loop-manager"
  )
  loop_manager_repo=""
  for candidate in "${candidates[@]}"; do
    if [[ -x "$candidate/scripts/verify-spec-planning.sh" ]]; then
      loop_manager_repo="$candidate"
      break
    fi
  done
fi

if [[ -z "${loop_manager_repo:-}" || ! -x "$loop_manager_repo/scripts/verify-spec-planning.sh" ]]; then
  cat >&2 <<'EOF'
Cannot find Loop Manager's source checkout.

Set LOOP_MANAGER_REPO_DIR to the checkout that contains:

  scripts/verify-spec-planning.sh

Example:

  LOOP_MANAGER_REPO_DIR=/Users/jmath/Documents/code/loop-manager .loop-manager/scripts/verify-spec-planning.sh
EOF
  exit 1
fi

"$loop_manager_repo/scripts/verify-spec-planning.sh"
