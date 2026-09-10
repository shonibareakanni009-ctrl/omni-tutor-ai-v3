from pathlib import Path
from xml.etree import ElementTree

root = Path(__file__).parent
ElementTree.parse(root / 'sitemap.xml')
assert len(list(ElementTree.parse(root / 'sitemap.xml').getroot())) == 23
routes = list((root / 'features').glob('*/index.html')) + list((root / 'learning').glob('*/index.html')) + list((root / 'resources').glob('*/index.html'))
routes += [root / 'learning/index.html', root / 'resources/index.html', root / 'blog/index.html', root / 'about/index.html', root / 'pricing/index.html', root / 'contact/index.html', root / 'privacy/index.html', root / 'terms/index.html', root / 'security/index.html', root / 'changelog/index.html']
assert len(routes) == 22
for route in routes:
    text = route.read_text(encoding='utf-8')
    assert '<title>' in text and '<meta name="description"' in text and 'rel="canonical"' in text
    assert 'application/ld+json' in text and 'href="/"' in text
print('seo-validation-ok')
