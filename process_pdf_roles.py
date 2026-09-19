import os, re

pdf_data = [
    ("Hana", "President"),
    ("Youssef", "Vice President"),
    ("Ziad", "Treasurer"),
    ("Eyad", "Projects Team Head"),
    ("Basmala", "Projects Team Vice Head"),
    ("Marwan", "Research Team Head"),
    ("Hamdy", "Research Team Vice Head"),
    ("Rahma", "Marketing Team Head"),
    ("Mohamed Hussien", "Marketing Team Vice Head"),
    ("Omar", "Multimedia Team Head"),
    ("Maryam", "Multimedia Team Vice Head"),
    ("Lina", "Multimedia Team Vice Head"),
    ("Mohamed Yousef", "Tech Team Head"),
    ("Ahmed Anter", "Tech Team Vice Head"),
    ("Loujaina", "Presentation Team Head"),
    ("Retaj", "Presentation Team Vice Head"),
    ("Abdallh", "PR Team Head"),
    ("Malak Ashraf", "HR Team Head"),
    ("Ahmed Khaled", "HR Team Vice Head"),
    ("Khadega", "Operations Team Head")
]

photo_dir = 'photos'
files = os.listdir(photo_dir)

members = []
for f in files:
    if not f.startswith('m_'): continue
    name = f[2:].rsplit('.', 1)[0].replace('_', ' ')
    
    matched_role = "Board Member"
    order = 999
    
    n = name.lower().replace('à', 'a').replace('ř', 'r').replace('ñ', 'n').replace('1', '')
    
    for i, (pdf_name, role) in enumerate(pdf_data):
        pn = pdf_name.lower()
        if pn in n or (pn == "marwan" and "mrwn" in n.replace('a','')) or (pn == "abdallh" and "abdallh" in n):
            matched_role = role
            order = i
            break
            
    # Some hardcoded fuzzy matches just in case
    if "marwan" in n or "mrwan" in n or "m r w n" in n:
        matched_role = "Research Team Head"
        order = 5
        
    members.append({
        'name': name.title(),
        'role': matched_role,
        'photo': 'photos/' + f,
        'order': order
    })

members.sort(key=lambda x: (x['order'], x['name']))

items_js = "items: [\n"
for m in members:
    items_js += f'      {{ name: "{m["name"]}", role: "{m["role"]}",  photo: "{m["photo"]}" }},\n'
items_js += "    ]"

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def repl(match):
    return "members: {\n    title: \"الناس اللي ورا الحكاية\",\n    hint: \"اضغط على الصورة عشان تشوف اللي بعدها\",\n    " + items_js + ","

html = re.sub(r'members:\s*\{.*?items:\s*\[.*?\],', repl, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with Hana as President.")
