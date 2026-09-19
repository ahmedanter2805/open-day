import os, re, shutil

src_dir = r'C:\Users\Ahmed Anter\Desktop\Digital Scrapbook\Personal Photo (File responses)-20260919T201711Z-1-001\Personal Photo (File responses)'
dst_dir = 'photos'
os.makedirs(dst_dir, exist_ok=True)

files = os.listdir(src_dir)

members = []
for f in files:
    name_part = f.rsplit('.', 1)[0]
    if ' - ' in f:
        name_part = f.split(' - ')[-1].rsplit('.', 1)[0].strip()
    elif 'WhatsApp Image' in f:
        m = re.search(r'(?:PM|AM)\s+(.*)', name_part)
        if m:
            name_part = m.group(1).strip()
            
    name = ' '.join([w.capitalize() for w in name_part.split()])
    
    ext = f.rsplit('.', 1)[-1]
    new_f = f"m_{name.replace(' ', '_').replace('(', '').replace(')', '')}.{ext}"
    
    shutil.copy(os.path.join(src_dir, f), os.path.join(dst_dir, new_f))
    members.append({
        'name': name,
        'role': 'عضو بالفريق',
        'photo': 'photos/' + new_f
    })

def get_order(m):
    n = m['name'].lower()
    if 'hana' in n: return 0
    if 'youssef' in n: return 1
    if 'ziad' in n: return 2
    if 'anter' in n: return 3
    return 4

members.sort(key=get_order)

for m in members:
    n = m['name'].lower()
    if 'anter' in n:
        m['role'] = 'Head of Tech Team'
    elif 'hana' in n or 'youssef' in n or 'ziad' in n:
        m['role'] = 'Board Member' # Just an assumption since they are prioritized

items_js = "items: [\n"
for m in members:
    items_js += f'      {{ name: "{m["name"]}", role: "{m["role"]}",  photo: "{m["photo"]}" }},\n'
items_js += "    ]"

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace members items
def repl(match):
    return "members: {\n    title: \"الناس اللي ورا الحكاية\",\n    hint: \"اضغط على الصورة عشان تشوف اللي بعدها\",\n    " + items_js + ","
    
html = re.sub(r'members:\s*\{.*?items:\s*\[.*?\],', repl, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done!")
