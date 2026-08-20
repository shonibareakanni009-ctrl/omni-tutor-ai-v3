# OmniTutor v2.9: The Hyper-Hub 🚀

OmniTutor is a next-generation **Knowledge Synthesis** platform designed to bridge the gap between AI conversation and long-term retention. By combining **Neural Hub** (conversational AI), **Knowledge Canvas** (persistence), and the **Quiz Engine** (validation), OmniTutor creates a closed-loop learning environment.

## 🌌 Core Architecture

### 1) Neural Hub (AI Interface)
- **Contextual Memory:** Automatically pulls context from your saved Canvas packets.
- **Document Focusing:** Pin a specific packet to force the AI to reason exclusively within that document’s boundaries.
- **LaTeX Integration:** Full rendering support for mathematical and scientific notation via MathJax.

### 2) Knowledge Canvas
- **Packet Persistence:** Save AI responses as permanent Knowledge Packets.
- **Focus Mode:** Toggle specific packets into the AI’s active attention window.
- **Micro-Learning:** Documents are kept concise to encourage rapid review and chunking of information.

### 3) Quiz Engine
- **Generative Assessment:** Uses the Gemini 2.0 Flash model to analyze your current Canvas and generate 3-question MCQ assessments.
- **Socratic Validation:** Tests your understanding of your own saved data to ensure active recall.

### 4) Neural Mind Map
- **Spatial Relationship:** Visualizes your knowledge ecosystem as a constellation.
- **Dynamic Growth:** The map expands automatically as you pin more packets to the Canvas.

## 🛠 Setup & Synchronization
- **API Key:** Obtain a Gemini API Key from Google AI Studio.
- **Config Node:** Navigate to Settings in the sidebar and enter your key.
- **ProCode:** Use the built-in ProCode editor for drafting scripts or prototyping alongside your tutor.

## 🗺 Future Roadmap (v3.0 and Beyond)

We are actively developing the following **Hyper-Sync** features:

### 🎙 Audio Synthesis (OmniVoice)
- **Neural Lectures:** Convert your Knowledge Canvas into a podcast-style audio lecture.
- **Voice Interactivity:** Ask questions using voice-to-text and receive spoken explanations.

### 🖼 Vision Integration
- **Diagram Interpretation:** Upload images of handwritten notes or complex diagrams for the AI to convert into Canvas packets.
- **Automatic Infographics:** Generate SVG diagrams directly from text-based knowledge packets.

### 👥 Collaborative Portals
- **Shared Hubs:** Create a public Hub ID to share your Knowledge Canvas with peers.
- **Group Quizzing:** Real-time competitive assessments based on shared study materials.

### 📈 Predictive Analytics
- **Retention Tracking:** The system will track quiz performance to identify weak nodes in your mind map.
- **Spaced Repetition:** Automatic reminders to review specific packets before you are likely to forget them.

## 📜 Technical Stack
- **Frontend:** HTML5, Tailwind CSS, FontAwesome.
- **Intelligence:** Google Generative AI (Gemini 2.5 Flash).
- **Rendering:** MathJax (LaTeX), SVG (Mind Mapping).
- **Persistence:** LocalStorage (in-memory browser state).

---

**OmniTutor v2.9 — Synthesizing the Future of Learning.**

# Omni AI v3 Specification — Planned, Not Yet Implemented

> **Status:** The v3 features below are a planning specification only. They have **not been added to the codebase yet**. The current repository remains the v2.9 Hyper-Hub implementation until each feature is built, tested, and released.

## Product direction

Omni AI v3 should become an AI learning and building workspace that combines the current Neural Hub, Knowledge Canvas, Quiz Engine, ProCode editor, LaTeX support, and Neural Mind Map with verified multimodal learning, safe code execution, project workspaces, collaborative study, and measurable retention. It should be a product upgrade, not only a theme or model-name change.

The product should have two surfaces: a public, crawlable knowledge surface for marketing pages, original tutorials, examples, documentation, policies, security information, and changelog content; and a private application surface for authenticated sessions, Canvas packets, files, quizzes, projects, model settings, and personal analytics. Private user content must not be indexed.

## V3 capabilities

| Capability | Requirement |
|---|---|
| Neural Hub | Streaming conversations, named sessions, search, export, context controls, memory on/off, citations to Canvas packets, and visible model status |
| Knowledge Canvas | Versioned packets, tags, folders, backlinks, source references, focus mode, import/export, search, and deletion controls |
| ProCode Lab | JavaScript first, followed by Python, HTML/CSS, and SQL adapters with isolated execution, run/stop/reset, file tree, console, error locations, diffs, and resource limits |
| Quiz Engine | Topic, level, question count, language, difficulty, objectives, explanations, missed-concept tags, retries, history, and spaced-review reminders |
| Vision | Image, PDF, diagram, screenshot, handwritten-code, and error-message uploads with progress, cancellation, processing state, and reviewable extracted text |
| OmniVoice | Accessible text-to-speech and speech-to-text with visible transcripts, controls, and clear provider/error states |
| Neural Mind Map | Accurate packet relationships, keyboard-accessible navigation, exportable SVG/PNG, and a non-visual list alternative |
| Collaboration | Shared hubs, roles, revocation, activity history, moderation controls, and private-by-default permissions |
| Predictive learning | Explainable progress summaries and user-controlled reminders based on actual quiz and review activity |
| AI gateway | One server-side model registry for `models/gemini-3.6-flash`, fallbacks, capability labels, context limits, usage tracking, retries, timeouts, and cost controls |
| Trust and safety | Privacy, Terms, Security, About, Contact, Status, Changelog, account deletion, data export, redaction, audit logs, and verification notices for high-impact topics |

## Security and privacy requirements

The client must not contain a shared production API key. Managed provider credentials must remain on the server. If bring-your-own-key is supported, keys must be encrypted at rest, scoped to the user, redacted from logs, removable from settings, and excluded from analytics and error reports.

Uploaded files, Canvas packets, conversations, memories, and shared hubs require explicit ownership and access rules. Private content must not appear in public routes, search results, sitemap entries, logs, or error messages. File uploads need type, size, malware, retention, and deletion controls. AI-generated code must execute in an isolated environment with CPU, memory, time, output, and network limits.

## Recommended architecture

A production v3 should move beyond a single static HTML file. Use a server-rendered or statically generated React application with a typed API, relational data, private object storage, and a server-side AI gateway.

| Layer | Responsibility |
|---|---|
| Public web | Server-rendered marketing, learning hub, tutorials, documentation, policies, changelog, and support pages |
| Application shell | Authenticated workspace, Canvas, sessions, quizzes, projects, uploads, settings, and accessibility |
| AI gateway | Provider adapters, model registry, streaming, prompt policy, retries, redaction, usage, and cost accounting |
| Execution service | Isolated language runners with resource and network limits |
| Data layer | Users, sessions, messages, packets, files, quiz attempts, memories, hubs, usage, and audit events |
| Storage | Private object storage with signed URLs and lifecycle policies |
| Observability | Structured logs, error tracking, latency, model failures, usage, abuse signals, and uptime |
| Delivery | CDN, immutable assets, security headers, sitemap generation, robots rules, and deployment checks |

## Google SEO plan

Google processes JavaScript sites through crawling, rendering, and indexing. Server-side rendering or pre-rendering is preferred because it improves initial performance and makes important content available to crawlers and users without depending on a later API request.[4]

### Crawlability and indexation

- Publish a root `robots.txt` and allow public marketing, learning, documentation, changelog, help, and policy routes.
- Disallow private workspace, account, session, Canvas, admin, API, preview, and internal-search routes.
- Generate an XML sitemap containing only canonical, public, indexable URLs and submit it through Google Search Console.
- Return meaningful `200`, `404`, `410`, `401`, and `403` status codes rather than soft errors.
- Use normal crawlable links with real `href` values; do not use URL fragments as the only representation of public pages.
- Use one canonical URL per page and redirect duplicate hostnames, protocols, and slash variants consistently.

### Public page map

| Route | Purpose | Indexing |
|---|---|---|
| `/` | OmniTutor learning and building workspace | Index |
| `/features/neural-hub` | Conversational tutoring and contextual memory | Index |
| `/features/knowledge-canvas` | Knowledge packet persistence and organization | Index |
| `/features/procode` | Safe browser code laboratory | Index |
| `/features/quiz-engine` | Active recall and assessment workflow | Index |
| `/features/vision` | Image and document learning | Index |
| `/learn/` | Original learning hub | Index |
| `/learn/javascript/` and `/learn/python/` | Original tutorials and examples | Index |
| `/use-cases/students` and `/use-cases/educators` | User workflows | Index |
| `/security`, `/privacy`, `/terms`, `/about`, `/contact`, `/changelog` | Trust and support pages | Index |
| `/app`, `/workspace`, `/canvas` | Private user application | Noindex or access-controlled |
| `/api/*`, `/admin/*`, `/search?*` | Internal or duplicate surfaces | Disallow and/or noindex |

### Metadata, structured data, and content

Every public page needs a unique concise `<title>`, unique meta description, canonical URL, one clear primary heading, useful visible copy, Open Graph metadata, and Twitter card metadata. Titles and descriptions should describe the actual page rather than repeat a keyword list. Google has stated that the obsolete `meta keywords` tag is not used for ranking.[3]

Add truthful JSON-LD in server-rendered output. The home page should use `Organization` and `WebSite`; product pages may use `SoftwareApplication` or `WebApplication`; original tutorials may use `Article`; and visible breadcrumbs may use `BreadcrumbList`. Do not fabricate ratings, reviews, prices, authors, dates, or organization details. Structured data must match visible content and should be validated with Google’s Rich Results Test and Search Console.[5]

The learning hub should publish original, technically reviewed tutorials with an identifiable author, last-updated date, prerequisites, version context, code examples, expected output, primary documentation links, and a correction path. Use descriptive internal links and avoid interchangeable keyword pages. Publish real trust information, not generated testimonials or stock avatars.

### Media and performance

Use optimized local AVIF or WebP assets where practical, descriptive filenames, meaningful alt text, width and height attributes, responsive sources, and lazy loading below the fold. Google recommends placing quality images near relevant text and using descriptive alt text.[3]

Track Core Web Vitals. The target is LCP at or below 2.5 seconds, INP below 200 milliseconds, and CLS below 0.1 at the 75th percentile.[6] Reduce third-party scripts, reserve image dimensions, split private application code, fingerprint static assets, cache immutable assets, and defer non-critical work.

### Measurement

Verify the canonical domain in Google Search Console, submit the sitemap, inspect representative URLs, monitor indexing and enhancements, and measure organic landing pages, sign-up, activation, retained learning sessions, Core Web Vitals, JavaScript errors, server latency, failed AI calls, upload failures, and cost per active user. Google notes that changes can take from hours to months to appear in search, so evaluate SEO changes over an appropriate period.[3]

## Implementation roadmap

### Phase 0: Foundation

Define the public/private route boundary, choose the production framework, add authentication, establish the data model, configure environments, remove client-side shared keys, add error tracking, and document data retention and threat protections.

### Phase 1: Core workspace

Implement sessions, streaming chat, model registry, Canvas packets, uploads, project files, safe code execution, code diffs, exports, and accessible loading and error states.

### Phase 2: Learning engine

Implement tutoring modes, quiz configuration, explanations, history, spaced review, learning objectives, progress summaries, voice, vision, and collaboration permissions.

### Phase 3: Public growth surface

Build server-rendered landing pages, the learning hub, documentation, canonical metadata, JSON-LD, sitemap, robots rules, policy pages, changelog, and Search Console verification.

### Phase 4: Quality and launch

Run security review, accessibility audit, cross-browser tests, unit and integration tests, crawl tests, structured-data validation, Lighthouse checks, Core Web Vitals monitoring, backup/restore checks, and staged release validation.

## Definition of done

- [ ] All verified v1 capabilities remain available: tutoring, code generation, browser execution, code improvement, quizzes, scoring, explanations, and progress feedback.
- [ ] Vision, document, and voice features work in the product rather than existing only as README claims.
- [ ] Users have projects, sessions, files, Canvas packets, exports, memory controls, and transparent model selection.
- [ ] API keys and private content are not exposed in public client code or indexed routes.
- [ ] Public pages are server-rendered or pre-rendered and contain meaningful HTML without requiring an API call to reveal the main content.
- [ ] Every indexable page has a unique title, description, canonical URL, primary heading, and useful visible content.
- [ ] `robots.txt`, `sitemap.xml`, status codes, internal links, redirects, and noindex rules are tested.
- [ ] JSON-LD is truthful, aligned with visible content, and validated with Google’s tools.
- [ ] Images have descriptive alt text, stable URLs, dimensions, and responsive delivery.
- [ ] Core Web Vitals targets are measured and monitored.
- [ ] Privacy, Terms, Security, About, Contact, Support, and Changelog pages are live.
- [ ] Automated tests, accessibility checks, security checks, error monitoring, usage monitoring, and rollback procedures are in place.

## References

[1]: https://github.com/shonibareakanni009-ctrl/Omni-ai "Omni AI v1 repository"

[2]: https://github.com/shonibareakanni009-ctrl/Omni-ai-tutor-v2 "Omni AI v2 repository"

[3]: https://developers.google.com/search/docs/fundamentals/seo-starter-guide "Google Search Engine Optimization Starter Guide"

[4]: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics "Google Search Central: JavaScript SEO basics"

[5]: https://developers.google.com/search/docs/appearance/structured-data/software-app "Google Search Central: Software app structured data"

[6]: https://developers.google.com/search/docs/appearance/core-web-vitals "Google Search Central: Core Web Vitals and Google Search"

---

**Implementation status:** The v3 implementation has not been added yet. This README documents the planned direction and acceptance criteria for the next development phase.
