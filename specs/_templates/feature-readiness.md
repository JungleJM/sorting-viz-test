# Feature Human Review Readiness

## Feature

`<feature-slug>`

## Feature PR

- PR URL: `<gitea-feature-pr-url>`
- Base: `main`
- Head: `feature/<feature-slug>`
- Status: draft / ready-for-human-review

## Merged task PRs

- [ ] 001 <task title> — <PR URL>

## Interactive preview

- Preview URL: `https://<feature-slug>.<preview-domain>`
- Access scope: Tailscale/LAN only
- Backend data policy: dev/test resources only

## Proof artifacts

- <artifact link/path>

## Verification summary

```sh
<commands run>
```

## Human test script

1. <step>
2. <step>
3. <expected result>

## Known limitations

- <limitation>

## Merge policy

This feature branch must not merge into `main` until the human explicitly approves merging.
