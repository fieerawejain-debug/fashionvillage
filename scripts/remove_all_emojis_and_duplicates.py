import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove all the duplicate mobile blocks that were injected into index.html
# We want clean sections:
# Hero:
html = re.sub(r'\s*<!-- Mobile Hero Section.*?</div>\s*</div>\s*</div>\s*', '\n', html, flags=re.DOTALL)
html = re.sub(r'\s*<!-- Mobile Concierge Suite.*?</div>\s*</div>\s*</div>\s*', '\n', html, flags=re.DOTALL)
html = re.sub(r'\s*<!-- Mobile Category Showcase Grid.*?</div>\s*</div>\s*', '\n', html, flags=re.DOTALL)
html = re.sub(r'\s*<!-- Mobile Curated Bestsellers Grid.*?</div>\s*</div>\s*', '\n', html, flags=re.DOTALL)
html = re.sub(r'\s*<!-- Mobile Everyday Grace Spotlight.*?</div>\s*</div>\s*', '\n', html, flags=re.DOTALL)
html = re.sub(r'\s*<!-- Mobile Weaver Story Section.*?</div>\s*</div>\s*', '\n', html, flags=re.DOTALL)
html = re.sub(r'\s*<!-- Mobile Testimonials Section.*?</div>\s*</div>\s*', '\n', html, flags=re.DOTALL)
html = re.sub(r'\s*<!-- Mobile Instagram Lookbook Gallery.*?</div>\s*</div>\s*', '\n', html, flags=re.DOTALL)

# Also remove any leftover .mobile-only or .desktop-only classes from section-frame so it behaves naturally
html = html.replace('section-frame desktop-only', 'section-frame')

# 2. Replace all children's emojis and HTML entity codes
# Emojis in tooltips & buttons:
html = html.replace('&#128269; ', '')
html = html.replace('&#128269;', '')
html = html.replace('&#128197; ', '')
html = html.replace('&#128197;', '')
html = html.replace('&#128172; ', '')
html = html.replace('&#128172;', '')
html = html.replace('&#128205; ', '')
html = html.replace('&#128205;', '')

# Unicode emojis:
emojis_to_remove = ['✨', '📅', '💬', '👑', '★', '📍', '🔍']
for em in emojis_to_remove:
    html = html.replace(em, '')

# In tooltips, replace &#10022; (asterisk) with clean typography
html = html.replace('&#10022; ', '')

# 3. Clean up drawer button text (remove leftover whitespace)
html = html.replace('> Find a Flagship Boutique', '>Find a Flagship Boutique &rarr;')
html = html.replace('> Book Private Video Trial', '>Book Private Video Trial &rarr;')
html = html.replace('> WhatsApp Senior Stylist', '>WhatsApp Senior Stylist &rarr;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully cleaned index.html of all emojis and duplicate mobile sections!')

# 4. Clean up js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace toast icon with a clean, luxury gold bullet
js = js.replace('<span style="color:var(--color-gold-light); font-size:16px;">✦</span>', '<span style="color:var(--color-gold-light); font-size:12px;">&bull;</span>')

# Remove any unicode emojis if present
for em in emojis_to_remove:
    js = js.replace(em, '')

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully cleaned js/main.js!')

# 5. Clean up css/style.css:
# Remove .desktop-only display:none from media queries and ensure clean responsive styling
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove .mobile-only and .desktop-only overrides that cause layout switching
css = css.replace('.desktop-only {\n  display: block;\n}', '')
css = css.replace('.desktop-only {\n    display: none !important;\n  }', '')
css = css.replace('.mobile-only {\n  display: none !important;\n}', '')
css = css.replace('.mobile-only {\n    display: block !important;\n  }', '')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Successfully cleaned css/style.css!')
