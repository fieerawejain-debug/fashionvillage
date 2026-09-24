import glob
import re

# Look for HTML entities like &#128..., &#x..., and unicode emojis
entity_pattern = re.compile(r'&#(128\d{3}|x1[fF]\w{3});')
unicode_emoji_pattern = re.compile(r'[\U00010000-\U0010ffff\u2700-\u27bf\u2600-\u26ff\u2b50\u2728\u2705\u2714\u2716\u2b06\u2b07\u2b05\u27a1]')

files = glob.glob('*.html') + glob.glob('js/*.js') + glob.glob('css/*.css')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    entities = entity_pattern.findall(content)
    emojis = unicode_emoji_pattern.findall(content)
    
    if entities or emojis:
        print(f'{f}:')
        if entities:
            print('  HTML entities:', set(entities))
        if emojis:
            # print unicode code points
            print('  Unicode emojis:', [f'U+{ord(c):04X} ({c.encode("ascii", "namereplace").decode()})' for c in set(emojis)])

print('Scan complete.')
