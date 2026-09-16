# Omni Tutor V3 — AI Continuation Handoff

**Project owner:** Akanni Shonibare  
**Repository:** `shonibareakanni009-ctrl/omni-tutor-ai-v3`  
**Branch:** `main`  
**Latest commit:** `3bb23ac Redesign public V3 landing page`  
**Last verified state:** `main` matches `origin/main` and the working tree is clean.

## 1. What this project is

Omni Tutor V3 is Akanni Shonibare’s AI-powered learning environment. The product is intended to help a learner ask questions, understand difficult concepts, capture useful knowledge, practice active recall, write code, build projects, and track progress.

The original V3 foundation is identified as **OmniTutor v2.9**. V2 provided the earlier immersive workspace direction. V3 is the evolution toward a clearer learning system with a public product surface and a focused browser workspace.

## 2. Current product architecture

This repository is currently a static, client-first prototype. It does not yet have authentication, a server-side AI gateway, relational persistence, secure code execution, private object storage, collaboration, or production account analytics.

| Surface | Location | Purpose | Indexing |
|---|---|---|---|
| Public landing page | `/index.html` | Product presentation and primary entry point | `index,follow` |
| Public SEO pages | `/features/` generated routes, `/learning/`, `/resources/`, `/blog/`, `/changelog/`, `/about/`, `/pricing/`, `/contact/`, `/privacy/`, `/terms/`, `/security/` | Crawlable product and learning content | Public pages are indexable where configured |
| Workspace entry | `/app/` | Local browser learning workspace | `noindex,nofollow` |
| Workspace pages | `/app/assistant.html`, `/app/canvas.html`, `/app/practice.html`, `/app/code.html`, `/app/map.html`, `/app/progress.html`, `/app/settings.html` | One focused page per workspace destination | `noindex,nofollow` |

## 3. What is complete

### Public landing page

The root landing page was redesigned without changing the workspace. It includes a sticky glass-style navigation bar, mobile menu, V3 hero headline, AI learning positioning, a realistic miniature tutor preview, a six-card feature section, Ask/Learn/Build steps, a larger workspace preview, a final CTA, and a minimal footer.

The landing page uses scoped `landing-v3` styles in `style.css`. It has responsive layouts for mobile, tablet, and desktop. It includes subtle scroll reveal, floating preview motion, hover states, technical grid effects, neon accents, and `prefers-reduced-motion` support.

The primary landing-page CTA points to the real `/app/` entry point. No fake authentication route was created.

### Workspace

The workspace is split into independent HTML pages so mobile users are not forced through one crowded screen. Each page has a shared shell and focused purpose:

- Assistant: local tutor conversation and selected Canvas context.
- Knowledge Canvas: create, focus, pin, delete, and review packets.
- Practice: generate quizzes from saved packets and record attempts.
- Code Lab: current development placeholder for future guided coding.
- Mind Map: render pinned or focused packet relationships.
- Progress: show packet count, quiz attempts, and average score.
- Settings: save a Gemini API key locally and store a ProCode scratchpad.

The workspace uses `app.js` and browser `localStorage` under the key `omnitutor_v29`. The logic is written defensively so each independent page binds only to controls that exist on that page.

### SEO and documentation

`build_seo_pages.py` generates the public SEO pages, sitemap, and robots rules. `validate_seo.py` checks the sitemap, route count, metadata, structured data, and public links. The project documents are written in Akanni’s first-person owner voice:

- `README.md`
- `OMNI_AI_TUTOR_V3_BLUEPRINT.md`
- `IMPLEMENTATION_LOG.md`

## 4. Important files

| File | Role |
|---|---|
| `index.html` | Public landing page only |
| `style.css` | Shared styles; contains both workspace styles and scoped public landing styles |
| `app.js` | Client-side workspace state, tutor fallback, packets, quiz, map, progress, and settings logic |
| `app/` | Independent workspace HTML pages |
| `build_app_pages.py` | Regenerates the independent workspace pages |
| `build_seo_pages.py` | Generates public SEO routes and crawl files |
| `validate_seo.py` | Validates sitemap and public SEO metadata |
| `README.md` | Owner-facing project overview and development instructions |
| `OMNI_AI_TUTOR_V3_BLUEPRINT.md` | Product direction, confirmed scope, and deferred scope |
| `IMPLEMENTATION_LOG.md` | First-person implementation history |
| `AI_CONTINUATION_HANDOFF.md` | This continuation guide |

## 5. Local development and validation

From the repository root, serve the static project with:

```bash
python3 -m http.server 4173 --bind 0.0.0.0
```

Then inspect:

```text
/
/app/
/app/assistant.html
/app/canvas.html
/app/practice.html
/app/code.html
/app/map.html
/app/progress.html
/app/settings.html
```

Run the normal checks:

```bash
node --check app.js
python3 validate_seo.py
python3 build_app_pages.py
python3 build_seo_pages.py
 git diff --check
```

The extra leading space before `git diff --check` above is accidental when copying; the correct command is:

```bash
git diff --check
```

After running generators, remove generated Python cache directories if they appear:

```bash
rm -rf __pycache__ app/__pycache__
```

Before committing, verify:

```bash
git status --short --branch
git log -1 --oneline
git diff --check
```

## 6. Guardrails for the next AI

1. Preserve the owner voice as **Akanni Shonibare** in all Markdown documentation.
2. Treat `/app/` as a real existing product surface. Do not break its routes, localStorage behavior, or client-side learning features.
3. Keep the root `/` landing page separate from the workspace.
4. Keep `/app/` pages `noindex,nofollow`; they are not public SEO content.
5. Do not claim authentication, secure execution, database persistence, server-side model security, or production analytics unless those features are actually implemented and tested.
6. Do not add fake routes for unavailable functionality. Use the existing `/app/` route for the current local workspace.
7. When changing a generated route, update the generator rather than editing only the generated output. Regenerate and validate afterward.
8. Keep public landing styles scoped under `.landing-v3` or another landing-only scope so workspace styling does not regress.
9. Prefer mobile-first layout decisions. Avoid crowded panels and horizontal overflow.
10. Do not expose or commit API keys. The current prototype stores a user-provided Gemini key in browser localStorage only; this is not production security.
11. Make reversible, focused commits with clear messages and push completed work to `origin/main`.

## 7. Recommended next priorities

### Priority 1 — Visual QA

Test the public landing page and every workspace page at approximately 360px, 390px, 768px, and 1280px widths. Check for horizontal overflow, unreadable text, clipped controls, broken relative links, and mobile drawer behavior.

### Priority 2 — Improve accessible navigation

Add stronger keyboard focus styles, a close action for the mobile landing menu, Escape-key handling, and better current-page semantics for workspace navigation links.

### Priority 3 — Improve local learning flow

Replace browser `prompt()` packet creation with an accessible in-page form or modal. Add packet editing and a clearer empty-state path from Assistant to Canvas. Keep it client-side until a server architecture is approved.

### Priority 4 — Product quality layer

Add missed-concept tags, review history, quiz explanations, learning objectives, and the Omni Tutor Audit Lab as local-first features before introducing server dependencies.

### Priority 5 — Server-backed architecture

Only after the client experience is stable, plan authentication, server-side model access, private persistence, file storage, secure code execution, and account-level analytics. Treat this as a separate architecture phase rather than quietly mixing it into the static prototype.

## 8. Latest verified delivery

The latest pushed commit is:

```text
3bb23ac Redesign public V3 landing page
```

The previous workspace rebuild commit is:

```text
887d2b4 Split workspace into mobile-first pages
```

To resume safely, start with:

```bash
gh repo clone shonibareakanni009-ctrl/omni-tutor-ai-v3
cd omni-tutor-ai-v3
git status --short --branch
git log --oneline -8
```

Read this file, `README.md`, `OMNI_AI_TUTOR_V3_BLUEPRINT.md`, and `IMPLEMENTATION_LOG.md` before modifying product behavior.
