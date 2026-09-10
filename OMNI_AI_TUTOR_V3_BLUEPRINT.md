# Omni AI Tutor v3 — Verified Product Blueprint

> **Status:** Phase 0 is complete. This document separates remembered, verified direction from unconfirmed future ideas and is the working blueprint for the repository.

## Product direction

Omni AI Tutor is evolving from an AI assistant into a digital learning environment: an AI tutor, structured learning platform, assessment system, personalization layer, progress tracker, and quality-audit lab in one product.

The v1 foundation established conversational help. V2 added structured lessons, questions, quizzes, feedback, and a more complete web application. V3 combines those capabilities with persistent learning context, measurable progress, and a public product surface.

## Verified V3 capabilities

| Capability | Product intent | Current repository status |
| --- | --- | --- |
| AI Tutor / Neural Hub | Natural questions, explanations, tutoring guidance, and contextual conversations | Local-first prototype with optional Gemini request |
| Knowledge Canvas | Persistent notes or packets that can be focused as tutor context | Implemented in `app.js` with localStorage |
| Quiz Engine | Questions, answers, scoring, and feedback for active recall | Implemented as a prototype with generated or fallback questions |
| Personalized learning | Adapt explanations to the learner’s context and demonstrated needs | Foundation: packet focus and learner context |
| Student progress | Track scores, performance, learning history, weaknesses, and improvement | Next implementation layer |
| Omni Tutor Audit Lab | Evaluate tutor quality instead of assuming model output is correct | Planned evaluation and regression surface |
| AI/ML experimentation | Gemini / Google GenAI, Hugging Face, Python, and model experimentation | Provider boundary is planned; client key flow is temporary prototype behavior |
| Public deployment and SEO | Crawlable product surface, canonical metadata, Search Console readiness | Landing-page metadata exists; route expansion remains |

## Explicitly unconfirmed

Voice tutor, PDF learning workflows, parent dashboards, teacher dashboards, and other adjacent features are not treated as historical V3 requirements until separately confirmed. They may be proposed in later phases, but should not be represented as shipped capabilities.

## Working architecture

The production direction is a server-rendered or pre-rendered public web surface plus an authenticated application surface. Private packets, conversations, files, sessions, quizzes, and analytics must be access-controlled and excluded from public indexing. Managed AI credentials belong on the server; browser API-key entry is retained only as a development fallback until a gateway is available.

### Core layers

1. **Public surface:** product overview, learning content, documentation, policies, changelog, and SEO metadata.
2. **Workspace shell:** tutor sessions, Knowledge Canvas, quizzes, progress, and settings.
3. **AI gateway:** model registry, streaming, retries, redaction, usage tracking, and cost controls.
4. **Execution and data services:** isolated code execution, relational records, private object storage, and audit events.
5. **Quality and trust:** accessibility, privacy, security, evaluation, observability, and rollback checks.

## Delivery roadmap

### Phase 0 — Digital foundation

Completed: SEO-aware public entry point, product direction, and initial repository documentation.

### Phase 1 — Core workspace

Current: connect the tutor workspace to the existing local-first state model; make packets, focus mode, quizzes, ProCode, and model settings discoverable in one application shell.

Next: add named sessions, export/import, better empty states, accessible navigation, model status, and a server-side AI gateway boundary.

### Phase 2 — Learning engine

Add tutoring modes, quiz configuration, explanations, attempt history, progress summaries, objectives, missed-concept tags, spaced review, and the Audit Lab evaluation workflow.

### Phase 3 — Multimodal and collaboration

After the core learning loop is stable, evaluate vision, document processing, voice, shared hubs, roles, moderation, and activity history as separately scoped features.

### Phase 4 — Public growth and launch quality

Build crawlable public routes, learning content, sitemap and robots rules, policy pages, structured-data validation, accessibility checks, security review, Core Web Vitals monitoring, and staged release validation.

## Definition of done for the first workspace slice

- A learner can ask the tutor a question and see a clear local or live response.
- A learner can create, focus, pin, and delete a Knowledge Canvas packet.
- A learner can generate a short quiz and receive immediate feedback.
- The UI communicates the V3 learning loop: ask, capture, practice, reflect.
- Empty and offline states are useful rather than misleading.
- No claim is made that unimplemented multimodal, voice, collaboration, or production security features are already shipped.

## Source note

This blueprint is reconstructed from the supplied project history. It intentionally marks uncertain ideas as unconfirmed rather than presenting them as historical requirements.

---

**Repository:** `shonibareakanni009-ctrl/omni-tutor-ai-v3`
