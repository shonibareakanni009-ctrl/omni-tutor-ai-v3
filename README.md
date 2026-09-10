# Omni AI Tutor v3

**Owner:** Akanni Shonibare
**Original V3 foundation:** OmniTutor v2.9
**Current phase:** Phase 1 — Client-side Core Workspace

Omni AI Tutor is my AI learning and building project. I am developing it to help learners ask better questions, understand explanations, capture useful knowledge, practice active recall, and eventually build projects with guided support.

The project is evolving from the original **OmniTutor v2.9** foundation. V2 established the immersive workspace direction. V3 keeps that workspace idea, improves the user experience, adds a clearer learning loop, and gives major public features their own crawlable URLs.

## Current product surfaces

The root homepage at `/` is my public landing page. It explains the product and links to the public learning content. The browser workspace is at `/app/`; it is intentionally marked noindex because it is currently a local-first prototype rather than a server-backed private application.

The public feature pages include `/features/ai-tutor/`, `/features/ai-quizzes/`, `/features/coding-tutor/`, `/features/language-learning/`, and `/features/personalized-learning/`. The public Learning pages include mathematics, programming, science, and languages.

I also publish `/resources/`, `/blog/`, `/changelog/`, `/about/`, `/pricing/`, `/contact/`, `/privacy/`, `/terms/`, and `/security/`.

## Client-side workspace capabilities

The current browser workspace includes the following capabilities:

- AI Tutor with local fallback responses and optional Gemini requests.
- Knowledge Canvas packets saved in browser localStorage.
- Focus mode for grounding tutor responses in selected packets.
- Quiz generation from saved learning packets.
- Immediate quiz feedback.
- Local quiz attempt history and average score signals.
- Packet counts and progress indicators.
- ProCode scratchpad storage.
- MathJax support for mathematical notation.
- Responsive Assistant, Canvas, Practice, Progress, Code Lab, Mind Map, and Settings views.

These capabilities are intentionally client-side for now. I am not claiming that server-backed accounts, private storage, secure code execution, or production analytics are already complete.

## Public SEO implementation

I created a public SEO surface so Google and learners can discover useful pages through normal links. Each public page has a unique title, meta description, canonical URL, robots directive, Open Graph data, Twitter data, JSON-LD, visible content, and internal links.

I maintain `sitemap.xml` with the public URLs only. I maintain `robots.txt` with the sitemap reference and rules for internal paths. The private `/app/` route is excluded from the sitemap.

I use `build_seo_pages.py` to generate public pages, the sitemap, and robots rules. I use `validate_seo.py` to verify page metadata, route counts, sitemap structure, and required public links.

## Project lineage

I keep the earlier projects connected to V3 so the evolution is clear:

- [Omni AI Ruby](https://omni-ai-ruby.vercel.app/)
- [Omni AI Tutor v1](https://omni-ai-tutor-v1.netlify.app/)
- [Omni AI Tutor v2](https://omni-ai-tutor-v2.netlify.app/)
- [Omni AI Tutor v3 on GitHub](https://github.com/shonibareakanni009-ctrl/omni-tutor-ai-v3)

## Local development

I can open the static project directly or serve it with any static HTTP server. For example:

```bash
python3 -m http.server 4173 --bind 0.0.0.0
```

I regenerate the public SEO pages after editing route copy with:

```bash
python3 build_seo_pages.py
```

I run the SEO checks with:

```bash
python3 validate_seo.py
```

## Roadmap

### Phase 0 — Digital foundation

I completed the initial product specification, public metadata, project documentation, and static foundation.

### Phase 1 — Client-side core workspace

I am improving the application shell, learning loop, local quizzes, progress signals, responsive behavior, and empty states without introducing a server.

### Phase 2 — Learning engine

I plan to add richer tutoring modes, configurable quizzes, explanations, missed-concept tags, review history, objectives, and the Omni Tutor Audit Lab.

### Phase 3 — Server-backed product

I will add authentication, server-side model access, private persistence, storage, secure execution, and account-level analytics only when the product is ready for that architecture.

## Project documents

- [My V3 blueprint](OMNI_AI_TUTOR_V3_BLUEPRINT.md)
- [My implementation log](IMPLEMENTATION_LOG.md)
- [Sitemap](sitemap.xml)
- [Robots rules](robots.txt)

## License

I retain the existing repository license and project ownership under my GitHub account.
