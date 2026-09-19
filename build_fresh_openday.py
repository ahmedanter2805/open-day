import base64, io, os, re, shutil
from PIL import Image

open_day_dir = r"c:\Users\Ahmed Anter\Documents\antigravity\quick-mendel\open-day"
template_path = r"C:\Users\Ahmed Anter\Desktop\Digital Scrapbook\template.html"
logo_src = r"C:\Users\Ahmed Anter\Desktop\Digital Scrapbook\600382923_122109525819107976_2481656308617062851_n.jpg"
photos_src = r"C:\Users\Ahmed Anter\Desktop\Digital Scrapbook\Personal Photo (File responses)-20260919T201711Z-1-001\Personal Photo (File responses)"

# 1. Process Logo
im = Image.open(logo_src).convert('RGBA')
data = im.getdata()
new_data = []
for item in data:
    if item[0] > 220 and item[1] > 220 and item[2] > 220:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
im.putdata(new_data)

bbox = im.getbbox()
if bbox:
    pad = 5
    bbox = (max(0,bbox[0]-pad),max(0,bbox[1]-pad),min(im.width,bbox[2]+pad),min(im.height,bbox[3]+pad))
    im = im.crop(bbox)

im.thumbnail((300, 300), Image.LANCZOS)
b = io.BytesIO()
im.save(b, 'PNG', optimize=True)
logo_b64 = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()

im.thumbnail((120, 120), Image.LANCZOS)
b2 = io.BytesIO()
im.save(b2, 'PNG', optimize=True)
mark_b64 = 'data:image/png;base64,' + base64.b64encode(b2.getvalue()).decode()

# 2. Copy and Rename Photos cleanly
dst_photos = os.path.join(open_day_dir, "photos")
os.makedirs(dst_photos, exist_ok=True)

photo_map = {
    "Hana Yasser": "m_Hana_Yasser.jpeg",
    "Youssef Abdelrazk": "m_Youssef_Abdelrazk.png",
    "Ziad Fadel": "m_Ziad_Fadel.jpg",
    "Ahmed Anter": "m_Ahmed_Anter.png",
    "Eyad Mohamed": "m_Eyad_Mohamed.jpg",
    "Basmala Talaat Belal": "m_Basmala_Talaat_Belal.jpg",
    "Marwan Mohammed": "m_Marwan_Mohammed.jpg",
    "Hamdy Mado": "m_Hamdy_Mado.jpg",
    "Rahma Ibrahim": "m_Rahma_Ibrahim.jpg",
    "Mohamed Hussien": "m_Mohamed_Hussien.jpg",
    "Maryam Yasser": "m_Maryam_Yasser.jpg",
    "Loujaina Alber": "m_Loujaina_Alber.jpeg",
    "Retaj Haitham": "m_Retaj_Haitham.jpeg",
    "Abdallh Diwan": "m_Abdallh_Diwan.jpeg",
    "Malak Ashraf": "m_Malak_Ashraf.jpg",
    "Khadega Mahmoud": "m_Khadega_Mahmoud1.jpg",
    "Ahmed Soliman": "m_Ahmed_Soliman.jpg",
    "Ammar Mohamed": "m_Ammar_Mohamed.jpg",
    "Darwin Alqmd": "m_Darwin_Alqmd.jpeg",
    "Malak Mohamed": "m_Malak_Mohamed.jpeg",
    "Mohamed San": "m_Mohamed_San.jpeg"
}

raw_files = os.listdir(photos_src)
for f in raw_files:
    ext = f.rsplit('.', 1)[-1]
    name_clean = ""
    if "Hana" in f: name_clean = "Hana Yasser"
    elif "Youssef" in f: name_clean = "Youssef Abdelrazk"
    elif "ziad" in f or "Ziad" in f: name_clean = "Ziad Fadel"
    elif "ANTER" in f: name_clean = "Ahmed Anter"
    elif "Eyad" in f: name_clean = "Eyad Mohamed"
    elif "Basmala" in f: name_clean = "Basmala Talaat Belal"
    elif "w" in f and "Mohamm" in f: name_clean = "Marwan Mohammed"
    elif "Hamdy" in f: name_clean = "Hamdy Mado"
    elif "Rahma" in f: name_clean = "Rahma Ibrahim"
    elif "Hussien" in f: name_clean = "Mohamed Hussien"
    elif "Maryam" in f: name_clean = "Maryam Yasser"
    elif "loujaina" in f: name_clean = "Loujaina Alber"
    elif "Retaj" in f or "retaj" in f: name_clean = "Retaj Haitham"
    elif "Abdallh" in f: name_clean = "Abdallh Diwan"
    elif "ashraf" in f: name_clean = "Malak Ashraf"
    elif "Khadega" in f: name_clean = "Khadega Mahmoud"
    elif "Soliman" in f: name_clean = "Ahmed Soliman"
    elif "ammar" in f: name_clean = "Ammar Mohamed"
    elif "darwin" in f: name_clean = "Darwin Alqmd"
    elif "Malak Mohamed" in f: name_clean = "Malak Mohamed"
    elif "San" in f: name_clean = "Mohamed San"
    
    if name_clean in photo_map:
        target_name = photo_map[name_clean]
        shutil.copy(os.path.join(photos_src, f), os.path.join(dst_photos, target_name))

# 3. Read template
with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Logos
html = html.replace('__LOGO_W__', logo_b64)
html = html.replace('__LOGO_P__', logo_b64)
html = html.replace('__MARK_W__', mark_b64)
html = html.replace('__MARK_P__', mark_b64)

# Replace Social Buttons
buttons_replacement = '''buttons: [
      { label: "سجّل معانا", url: "https://forms.gle/3vnymj7Jv8CungY56", primary: true },
      { label: "LinkedIn", url: "https://linkedin.com/company/enactus-innovation" },
      { label: "Facebook", url: "https://www.facebook.com/profile.php?id=61583239292720" },
      { label: "Instagram", url: "https://www.instagram.com/enactus_innovation/" },
      { label: "TikTok", url: "https://www.tiktok.com/@enactusinnovation" },
      { label: "Email", url: "mailto:enactusinnovationuniversity@gmail.com" }
    ]'''
html = re.sub(r'buttons:\s*\[.*?\]', buttons_replacement, html, flags=re.DOTALL)

# Font Legibility
html = re.sub(r'\.big-q\{font-family:var\(--ruq\)', '.big-q{font-family:var(--body)', html)
html = re.sub(r'\.hook-kicker\{font-size:1.9rem', '.hook-kicker{font-family:var(--body);font-weight:600;font-size:1.4rem', html)

# Members List In Exact PDF Order
members_list = [
    ("Hana Yasser", "President 👑", "m_Hana_Yasser.jpeg"),
    ("Youssef Abdelrazk", "Vice President", "m_Youssef_Abdelrazk.png"),
    ("Ziad Fadel", "Treasurer", "m_Ziad_Fadel.jpg"),
    ("Ahmed Anter", "Head of Tech Team", "m_Ahmed_Anter.png"),
    ("Eyad Mohamed", "Projects Team Head", "m_Eyad_Mohamed.jpg"),
    ("Basmala Talaat Belal", "Projects Team Vice Head", "m_Basmala_Talaat_Belal.jpg"),
    ("Marwan Mohammed", "Research Team Head", "m_Marwan_Mohammed.jpg"),
    ("Hamdy Mado", "Research Team Vice Head", "m_Hamdy_Mado.jpg"),
    ("Rahma Ibrahim", "Marketing Team Head", "m_Rahma_Ibrahim.jpg"),
    ("Mohamed Hussien", "Marketing Team Vice Head", "m_Mohamed_Hussien.jpg"),
    ("Maryam Yasser", "Multimedia Team Vice Head", "m_Maryam_Yasser.jpg"),
    ("Loujaina Alber", "Presentation Team Head", "m_Loujaina_Alber.jpeg"),
    ("Retaj Haitham", "Presentation Team Vice Head", "m_Retaj_Haitham.jpeg"),
    ("Abdallh Diwan", "PR Team Head", "m_Abdallh_Diwan.jpeg"),
    ("Malak Ashraf", "HR Team Head", "m_Malak_Ashraf.jpg"),
    ("Khadega Mahmoud", "Operations Team Head", "m_Khadega_Mahmoud1.jpg"),
    ("Ahmed Soliman", "Board Member", "m_Ahmed_Soliman.jpg"),
    ("Ammar Mohamed", "Board Member", "m_Ammar_Mohamed.jpg"),
    ("Darwin Alqmd", "Board Member", "m_Darwin_Alqmd.jpeg"),
    ("Malak Mohamed", "Board Member", "m_Malak_Mohamed.jpeg"),
    ("Mohamed San", "Board Member", "m_Mohamed_San.jpeg")
]

members_js = '''  members: {
    title: "الناس اللي ورا الحكاية",
    hint: "اضغط على الصورة عشان تشوف اللي بعدها",
    items: [
'''
for name, role, photo_fn in members_list:
    members_js += f'      {{ name: "{name}", role: "{role}", photo: "photos/{photo_fn}" }},\n'

members_js += '''    ],
    bridge: "جاهز تكون جزء من الحكاية؟"
  },'''

html = re.sub(r'members:\s*\{[\s\S]*?\n  \},', members_js, html)

# Remove unused CONTENT blocks (timeline, achievements, voices)
html = re.sub(r'timeline:\s*\{[\s\S]*?\n  \},', '', html)
html = re.sub(r'achievements:\s*\{[\s\S]*?\n  \},', '', html)
html = re.sub(r'voices:\s*\{[\s\S]*?\n  \},', '', html)

# Remove timeline, achievements, voices ADD calls safely
before_timeline = html.split('/* الرحلة */')[0]
after_voices = '  /* دورك */' + html.split('/* دورك */')[1]
html = before_timeline + after_voices

# Write final index.html in open-day directory
final_html_path = os.path.join(open_day_dir, 'index.html')
with open(final_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fresh build completed for open-day repository.")
