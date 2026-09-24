with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

start_mark = '<footer class="luxury-footer" id="site-footer">'
end_mark = '</footer>'
s_idx = index_content.find(start_mark)
e_idx = index_content.find(end_mark, s_idx)

if s_idx == -1 or e_idx == -1:
    print('Luxury footer not found in index.html!')
    exit(1)

luxury_footer = index_content[s_idx:e_idx + len(end_mark)]

pages = ['banarasi.html', 'concierge.html', 'everyday.html', 'kanjivaram.html', 'story.html']

for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    
    old_f_start = c.find('<footer')
    old_f_end = c.find('</footer>', old_f_start)
    if old_f_start != -1 and old_f_end != -1:
        new_c = c[:old_f_start] + luxury_footer + c[old_f_end + len('</footer>'):]
        with open(page, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f'Successfully updated footer in {page}')

print('All pages updated with the responsive luxury cream footer!')
