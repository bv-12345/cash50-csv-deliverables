# Owner rule: check GitHub before work

The owner required this on 1 October 2026: **before every task, edit, change and build, check public GitHub for useful existing work**. Search other developers' public repositories with at least **500 stars**, preferring **1,000 or more**. The owner's private repos are where this rule is preserved, not the search target.

This covers code, UI components, layouts, design systems, animations, libraries, tests, tools, data models, finished implementations and skills. Use what fits the actual customer job and existing project. Do not turn every discovery into a new dependency or rebuild something useful that already exists.

Use the portable [github-reuse-scout workflow](../.agents/skills/github-reuse-scout/SKILL.md). Check live GitHub before work. A relevant saved shortlist can make the next edit/build check small: revalidate its source and metadata instead of repeating a broad catalog scan. Expand the search when the need changes. Record the dated check; do not silently skip it.

Inspect relevant source at a pinned revision and check behaviour, maintenance, licence, security, supported versions and integration costs. Stars determine where to look, not fitness. First-party projects below the threshold may be useful references, but do not replace the threshold-qualified search.

Always report in plain English:

- What was found and what it does.
- Whether/how it will be used, or why it was deferred or rejected.
- Which implementation work it avoids and how it could save time, model usage or money.
- Whether savings are estimated or measured; measurements need a baseline.
- If nothing fits, what was searched and why custom work remains necessary.

Keep private details out of public queries. Do not blindly execute code or install hooks, change product scope, spend money or publish because a popular project was found. Existing owner gates and chosen designs still govern. An agent skill is guidance, not a shipped capability.

This is portable instruction, not a guarantee that every arbitrary AI obeys it. Preserve dated application receipts and inspect compliance at handoff. It does not authorize unrelated product feature work.
