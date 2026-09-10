from pathlib import Path
from html import escape
from datetime import date

ROOT = Path(__file__).parent
BASE = 'https://omni-ai-tutor-v3.netlify.app'
TODAY = date.today().isoformat()

PAGES = {
    '/features/ai-tutor/': ('AI Tutor | Omni AI Tutor v3', 'Learn with a contextual AI tutor that explains concepts, guides practice, and helps you build lasting understanding.', 'AI Tutor', 'Ask questions naturally and get explanations that meet you where you are. Omni AI Tutor connects each conversation to your learning context so answers become useful next steps.'),
    '/features/ai-quizzes/': ('AI Quizzes for Active Recall | Omni AI Tutor v3', 'Practice with AI-generated quizzes, immediate feedback, and learning signals built from your own notes.', 'AI Quizzes', 'Turn saved learning notes into focused practice. Generate questions, test your recall, review explanations, and identify the ideas that deserve another look.'),
    '/features/coding-tutor/': ('Coding Tutor and ProCode Lab | Omni AI Tutor v3', 'Learn programming with an AI coding tutor, guided explanations, and a workspace for experimenting with code.', 'Coding Tutor', 'Move from “what does this code do?” to confident practice. The Coding Tutor direction combines guided explanations with a ProCode workspace for examples, debugging, and reflection.'),
    '/features/language-learning/': ('AI Language Learning | Omni AI Tutor v3', 'Build language skills through conversational practice, explanations, vocabulary review, and personalized learning sessions.', 'Language Learning', 'Practice a new language with a tutor that can explain grammar, rehearse conversations, and turn unfamiliar phrases into reusable learning packets.'),
    '/features/personalized-learning/': ('Personalized Learning | Omni AI Tutor v3', 'A personalized learning workspace that adapts explanations and practice to your context, questions, and progress.', 'Personalized Learning', 'Personalized learning starts with evidence. Omni tracks the context you choose, the questions you ask, and the practice you complete so future learning can become more relevant.'),
    '/learning/': ('Learning Hub | Omni AI Tutor v3', 'Explore original learning paths, study guides, and practical explanations for mathematics, programming, science, and languages.', 'Learning Hub', 'The Omni Learning Hub is a growing public library for clear explanations and practical study support. Start with a learning area, then bring useful ideas into your private workspace.'),
    '/learning/mathematics/': ('Mathematics Learning | Omni AI Tutor v3', 'Understand mathematics through step-by-step explanations, active recall, and focused practice with an AI tutor.', 'Mathematics Learning', 'Build mathematical understanding by connecting intuition, examples, and practice. Use the tutor to unpack difficult steps and the Quiz Engine to check what you can recall.'),
    '/learning/programming/': ('Programming Learning | Omni AI Tutor v3', 'Learn programming concepts with explanations, examples, debugging guidance, and deliberate practice.', 'Programming Learning', 'Programming becomes easier to retain when you explain, modify, and test ideas. Explore concepts with the Coding Tutor and save the patterns you want to revisit.'),
    '/learning/science/': ('Science Learning | Omni AI Tutor v3', 'Study science with clear explanations, connected concepts, and quizzes designed to strengthen understanding.', 'Science Learning', 'Use the tutor to connect scientific ideas, ask “why” questions, and turn complex notes into smaller, reviewable learning packets.'),
    '/learning/languages/': ('Language Learning Paths | Omni AI Tutor v3', 'Explore language learning support for vocabulary, grammar, conversation, and spaced review.', 'Languages Learning', 'Language learning improves with frequent retrieval and meaningful use. Combine conversation practice with saved examples and short review quizzes.'),
    '/resources/': ('Learning Resources | Omni AI Tutor v3', 'Guides, tutorials, and study resources for using AI to learn more effectively.', 'Resources', 'Find practical resources for building better learning habits with an AI tutor: from asking precise questions to reviewing concepts with active recall.'),
    '/resources/articles/': ('Learning Articles | Omni AI Tutor v3', 'Evidence-informed articles about AI tutoring, active recall, personalization, and digital learning.', 'Articles', 'Read practical articles about the habits and systems that make AI-assisted learning more useful, transparent, and measurable.'),
    '/resources/tutorials/': ('Learning Tutorials | Omni AI Tutor v3', 'Step-by-step tutorials for learning with the Omni AI Tutor workspace.', 'Tutorials', 'Follow guided tutorials for asking better questions, creating Knowledge Canvas packets, and using quizzes to reinforce understanding.'),
    '/resources/study-guides/': ('Study Guides | Omni AI Tutor v3', 'Focused study guides for turning difficult topics into clear, reviewable learning plans.', 'Study Guides', 'Use a study guide as a starting point, then personalize it with the tutor and turn the most important ideas into Canvas packets.'),
    '/about/': ('About Omni AI Tutor | Learning with momentum', 'Learn about the vision behind Omni AI Tutor: an AI tutor, learning platform, and assessment system.', 'About Omni', 'Omni AI Tutor is being built as a digital learning environment rather than a simple chatbot. The product connects tutoring, knowledge capture, practice, and reflection.'),
    '/pricing/': ('Omni AI Tutor Plans | Learning Workspace', 'Explore the current product direction and workspace access for Omni AI Tutor.', 'Plans', 'Omni AI Tutor is currently an evolving product prototype. This page will document available plans and limits as the production service becomes available.'),
    '/contact/': ('Contact Omni AI Tutor', 'Contact the Omni AI Tutor project with questions, feedback, and learning product suggestions.', 'Contact', 'Have feedback about the learning experience, accessibility, or a useful feature? Send a clear note so the product can improve around real learner needs.'),
    '/privacy/': ('Privacy | Omni AI Tutor', 'Read how Omni AI Tutor approaches privacy, learning data, and responsible product development.', 'Privacy', 'Privacy information will be expanded as production accounts, storage, and AI gateway services are introduced. Private learning content should remain private and access-controlled.'),
    '/terms/': ('Terms | Omni AI Tutor', 'Read the terms and responsible-use information for Omni AI Tutor.', 'Terms', 'Omni AI Tutor is an educational support tool, not a replacement for qualified educators or professional advice. Product terms will be updated before production launch.'),
    '/security/': ('Security | Omni AI Tutor', 'Learn about the security direction for AI tutoring, learning content, files, and code execution.', 'Security', 'Security is part of the product foundation: private content access controls, server-side provider credentials, isolated execution, redaction, and auditability.'),
    '/changelog/': ('Changelog | Omni AI Tutor v3', 'Follow the progress of Omni AI Tutor v3 as the learning workspace evolves.', 'Changelog', 'Track product improvements, documentation updates, and milestones as Omni AI Tutor moves from foundation to a complete learning environment.'),
}

NAV = [('/','Home'),('/features/ai-tutor/','Features'),('/learning/','Learning'),('/resources/','Resources'),('/about/','About'),('/contact/','Contact')]

def links_for(path):
    related = []
    if path.startswith('/features/'):
        related = [('/features/ai-quizzes/','AI Quizzes'),('/features/personalized-learning/','Personalized Learning'),('/learning/','Learning Hub')]
    elif path.startswith('/learning/'):
        related = [('/features/ai-tutor/','AI Tutor'),('/features/ai-quizzes/','AI Quizzes'),('/resources/study-guides/','Study Guides')]
    elif path.startswith('/resources/'):
        related = [('/learning/','Learning Hub'),('/features/personalized-learning/','Personalized Learning'),('/contact/','Contact')]
    else:
        related = [('/features/ai-tutor/','AI Tutor'),('/learning/','Learning Hub'),('/resources/','Resources')]
    return related

def page(path, title, description, heading, intro):
    canonical = BASE + path
    related = links_for(path)
    related_html = ''.join(f'<a class="link-card" href="{u}"><strong>{escape(label)}</strong><span>Explore this learning path →</span></a>' for u, label in related)
    nav_html = ''.join(f'<a href="{u}">{escape(label)}</a>' for u, label in NAV)
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(description)}"><meta name="author" content="Akanni Shonibare">
<link rel="canonical" href="{canonical}"><meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Omni AI Tutor"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(description)}"><meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{escape(title)}"><meta name="twitter:description" content="{escape(description)}">
<script type="application/ld+json">{json_ld(title, description, canonical, path)}</script>
<link rel="stylesheet" href="/style.css">
</head><body class="public-page"><div class="public-shell"><header class="public-nav"><a class="brand" href="/"><span class="brand-mark">O</span><span>OMNI <small>v3</small></span></a><nav aria-label="Primary">{nav_html}</nav></header><main><article class="public-hero"><div class="eyebrow">OMNI AI TUTOR · LEARNING</div><h1>{escape(heading)}<br><span>with momentum.</span></h1><p>{escape(intro)}</p><div class="public-actions"><a class="btn btn-primary" href="/">Open learning workspace ↗</a><a class="btn btn-outline" href="/learning/">Explore learning</a></div></article><section class="public-section" aria-labelledby="continue"><h2 id="continue">Continue exploring</h2><p>Connect this page to the rest of the Omni learning system through clear, descriptive internal links.</p><div class="link-grid">{related_html}</div></section><section class="public-section lineage" aria-labelledby="lineage"><h2 id="lineage">Explore the Omni project lineage</h2><p>See how the project evolved from its original AI assistant foundation into a broader AI learning environment.</p><div class="lineage-links"><a href="https://omni-ai-ruby.vercel.app/" rel="noopener"><strong>Omni AI Ruby</strong><span>Early AI experimentation ↗</span></a><a href="https://omni-ai-tutor-v1.netlify.app/" rel="noopener"><strong>Omni AI Tutor v1</strong><span>Original tutor foundation ↗</span></a><a href="https://omni-ai-tutor-v2.netlify.app/" rel="noopener"><strong>Omni AI Tutor v2</strong><span>Structured learning platform ↗</span></a></div></section></main><footer class="public-footer"><span>OMNI AI TUTOR v3 · {TODAY}</span><span><a href="/privacy/">Privacy</a> · <a href="/security/">Security</a> · <a href="/terms/">Terms</a> · <a href="/changelog/">Changelog</a></span></footer></div></body></html>'''

def json_ld(title, description, canonical, path):
    import json
    kind = 'WebSite' if path == '/' else 'WebPage'
    data = {'@context':'https://schema.org','@type':kind,'name':title,'description':description,'url':canonical,'isPartOf':{'@type':'WebSite','name':'Omni AI Tutor','url':BASE}}
    if path == '/': data['publisher'] = {'@type':'Person','name':'Akanni Shonibare'}
    return json.dumps(data, separators=(',',':'))

for path, values in PAGES.items():
    target = ROOT / path.strip('/') / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page(path, *values), encoding='utf-8')

# Public homepage links and canonical domain are updated without disturbing the app workspace.
home = ROOT / 'index.html'
text = home.read_text(encoding='utf-8')
text = text.replace('https://omni-ai-tutor-v3.vercel.app', BASE)
text = text.replace('<a href="OMNI_AI_TUTOR_V3_BLUEPRINT.md" class="btn btn-ghost hidden sm:inline-flex">Blueprint</a>', '<a href="/features/ai-tutor/" class="btn btn-ghost hidden sm:inline-flex">Features</a><a href="/learning/" class="btn btn-ghost hidden sm:inline-flex">Learning</a><a href="/resources/" class="btn btn-ghost hidden sm:inline-flex">Resources</a><a href="OMNI_AI_TUTOR_V3_BLUEPRINT.md" class="btn btn-ghost hidden sm:inline-flex">Blueprint</a>')
text = text.replace('<footer class="footer"><span>OMNI AI TUTOR <b>v3</b></span><span>Ask · Capture · Practice · Reflect</span><a href="OMNI_AI_TUTOR_V3_BLUEPRINT.md">Read the verified blueprint →</a></footer>', '<footer class="footer"><span>OMNI AI TUTOR <b>v3</b></span><span>Ask · Capture · Practice · Reflect</span><span><a href="/privacy/">Privacy</a> · <a href="/security/">Security</a> · <a href="/contact/">Contact</a></span><a href="OMNI_AI_TUTOR_V3_BLUEPRINT.md">Read the verified blueprint →</a></footer>')
home.write_text(text, encoding='utf-8')

# Crawl directives: only public routes are listed; no private app routes are invented.
(ROOT / 'robots.txt').write_text(f'''User-agent: *\nAllow: /\nDisallow: /api/\nDisallow: /admin/\nDisallow: /search?\nSitemap: {BASE}/sitemap.xml\n''', encoding='utf-8')
urls = ['/'] + list(PAGES.keys())
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path in urls:
    priority = '1.0' if path == '/' else ('0.9' if path in ['/learning/','/features/ai-tutor/','/resources/'] else '0.7')
    sitemap.append(f'  <url><loc>{BASE}{path}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{priority}</priority></url>')
sitemap.append('</urlset>')
(ROOT / 'sitemap.xml').write_text('\n'.join(sitemap) + '\n', encoding='utf-8')

print(f'Generated {len(PAGES)} public SEO pages, sitemap.xml, and robots.txt')
