# Omni AI Tutor v3 — My Product Blueprint

> **Author:** Akanni Shonibare
> **Status:** Phase 1 client-side workspace foundation in progress

## My product direction

I am building Omni AI Tutor as a digital learning environment, not just a chatbot. My goal is to combine AI tutoring, structured learning, knowledge capture, assessment, personalization, progress tracking, and a quality-audit layer in one product.

The original OmniTutor foundation was established as **v2.9**. V3 is the next product direction built on that foundation. V2 established the immersive workspace pattern, while V3 gives each major capability its own public URL and connects the private workspace to a crawlable public learning surface.

## My verified V3 capabilities

| Capability | My product intent | Current status |
| --- | --- | --- |
| AI Tutor / Neural Hub | I want learners to ask natural questions, receive explanations, and get contextual guidance. | Local-first prototype with optional Gemini request |
| Knowledge Canvas | I want learners to save notes and packets, focus them, pin them, and reuse them as context. | Implemented with browser localStorage |
| Quiz Engine | I want learners to test their understanding with questions, scoring, and feedback. | Implemented with generated and fallback questions |
| Personalized learning | I want explanations and practice to reflect the learner’s chosen context and demonstrated needs. | Foundation implemented through packet focus |
| Progress | I want progress to come from actual quiz and review activity. | Local packet and attempt metrics implemented |
| Omni Tutor Audit Lab | I want to evaluate tutor quality instead of assuming that AI output is correct. | Planned evaluation surface |
| AI/ML experimentation | I am exploring Gemini, Google GenAI, Hugging Face, Python, and related model workflows. | Provider boundary planned |
| Public SEO surface | I want Google and learners to understand the product through useful, crawlable pages. | Public routes, metadata, internal links, sitemap, and robots rules implemented |

## Features I have not confirmed as shipped

I am not treating voice tutoring, PDF learning workflows, parent dashboards, teacher dashboards, collaboration, or other adjacent ideas as shipped V3 capabilities. I may evaluate them later, but I will not present them as complete until I build and verify them.

## My current architecture

For now, I am keeping the product serverless and client-first. The public landing page and learning pages are static HTML. The local workspace lives at `/app/`, uses browser storage, and is marked noindex. This lets me improve the product experience without pretending that authentication, private storage, or server-side security already exist.

When I introduce a server, I will separate the public web, authenticated application, AI gateway, execution service, data layer, storage, observability, and delivery concerns. Production provider credentials will remain server-side. Any BYOK implementation will need encryption, user scoping, redaction, removal controls, and exclusion from analytics.

## My public route structure

The public homepage is `/`. My feature pages are `/features/ai-tutor/`, `/features/ai-quizzes/`, `/features/coding-tutor/`, `/features/language-learning/`, and `/features/personalized-learning/`. My Learning pages cover `/learning/mathematics/`, `/learning/programming/`, `/learning/science/`, and `/learning/languages/`.

I also publish `/resources/`, `/blog/`, `/changelog/`, `/about/`, `/pricing/`, `/contact/`, `/privacy/`, `/terms/`, and `/security/`. The private browser workspace is `/app/` and is excluded from the sitemap.

## My roadmap

### Phase 0 — Digital foundation

I completed the initial product direction, public metadata, project documentation, and static foundation.

### Phase 1 — Client-side core workspace

I am completing the local-first workspace shell: Assistant, Knowledge Canvas, Practice, Progress, Settings, responsive behavior, local quiz attempts, packet counts, and clearer empty states. I am intentionally deferring server-dependent features.

### Phase 2 — Learning engine

I will add richer tutoring modes, quiz configuration, explanations, attempt history, objectives, missed-concept tags, spaced review, and the Omni Tutor Audit Lab.

### Phase 3 — Server-backed product

When the product is ready, I will add authentication, a server-side AI gateway, private persistence, secure file storage, isolated code execution, and account-level analytics.

### Phase 4 — Multimodal, collaboration, and launch quality

I will evaluate vision, documents, voice, shared hubs, roles, moderation, accessibility, security, performance, structured-data validation, and staged release checks as separate workstreams.

## My first workspace definition of done

I consider the first client-side slice useful when a learner can ask the tutor a question, create and focus a Canvas packet, generate a quiz, receive feedback, and see local progress signals. The interface must clearly communicate the loop: **ask, capture, practice, reflect**.

I will not claim that server-backed privacy, secure execution, voice, vision, or collaboration are complete until those features are implemented and tested.

## Project history

I maintain links to the earlier projects so the evolution is visible:

- [Omni AI Ruby](https://omni-ai-ruby.vercel.app/)
- [Omni AI Tutor v1](https://omni-ai-tutor-v1.netlify.app/)
- [Omni AI Tutor v2](https://omni-ai-tutor-v2.netlify.app/)
- [Omni AI Tutor v3 repository](https://github.com/shonibareakanni009-ctrl/omni-tutor-ai-v3)
