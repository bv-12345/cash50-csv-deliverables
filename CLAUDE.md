# Owner working rules

<!-- OWNER GITHUB REUSE REQUIREMENT: BEGIN -->
## Owner GitHub reuse requirement

Before every task, edit, change or build, check public GitHub for useful existing work. Search other developers' repositories with at least 500 stars, preferring 1,000 or more. Consider code, components, layouts, libraries, tests, tools, finished implementations and reusable instructions. Check the dated source, licence, maintenance, compatibility, security, integration cost and fit before adopting anything.

Use `docs/GITHUB_REUSE_RULE.md` and `.agents/skills/github-reuse-scout/SKILL.md`. Record the live check and always report what was found, the decision, work avoided and estimated or measured time, usage or cost savings. Do not install blindly, expose private work, change product scope or publish because a project is popular.
<!-- OWNER GITHUB REUSE REQUIREMENT: END -->

<!-- owner-standing-style: BEGIN -->
## Owner standing interface and writing rules

- Do not add an eyebrow, kicker, overline or renamed equivalent above a main heading. An eyebrow is a small decorative label, often uppercase or letter-spaced. Breadcrumbs, navigation labels, useful status badges, form labels and dates are allowed when they serve their functional purpose.
- Do not use em dashes in newly generated copy, prose, comments or commit messages. Follow any local rule that also prohibits en dashes.
<!-- owner-standing-style: END -->

## Words never break in the middle

Text on a screen, email or printout never splits a word across two lines. Headings, names,
buttons, labels and prices wrap only between words: `overflow-wrap: anywhere` and
`word-break: break-all` are kept for long web addresses, codes and IDs. Anything sized to fit its
box (a banner title, a card name, a big number) is sized by its longest word as well as its total
length, and shrinks before it breaks. Where the project has a screen audit, it fails when a word
is split across lines, and is seen catching a planted example before anyone relies on it. Stress
data includes the longest real single words the product will show (business names, product
names, headlines people type in) and the live content, not only short demo text, checked at 320,
390, 768 and 1440 wide.
