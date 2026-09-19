with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

before = html.split('/* الرحلة */')[0]
after = '  /* دورك */' + html.split('/* دورك */')[1]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(before + after)

print("Pages 11, 12, 13 safely removed.")
