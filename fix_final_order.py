import re

members_js = '''  members: {
    title: "الناس اللي ورا الحكاية",
    hint: "اضغط على الصورة عشان تشوف اللي بعدها",
    items: [
      { name: "Hana Yasser", role: "President", photo: "photos/m_Hana_Yasser.jpeg" },
      { name: "Youssef Mohamed", role: "Vice President", photo: "photos/m_Youssef_Abdelrazk.png" },
      { name: "Ziad Mohamed", role: "Treasurer", photo: "photos/m_Ziad_Fadel.jpg" },
      { name: "Eyad Mohamed", role: "Projects Team Head", photo: "photos/m_Eyad_Mohamed.jpg" },
      { name: "Basmala Talaat", role: "Projects Team Vice Head", photo: "photos/m_Basmala_Talaat_Belal.jpg" },
      { name: "Marwan Mohamed", role: "Research Team Head", photo: "photos/m_Màřwàñ_Mohammed.jpg" },
      { name: "Hamdy Rabee", role: "Research Team Vice Head", photo: "photos/m_Hamdy_Mado.jpg" },
      { name: "Rahma Ibrahim", role: "Marketing Team Head", photo: "photos/m_Rahma_Ibrahim.jpg" },
      { name: "Mohamed Hussien", role: "Marketing Team Vice Head", photo: "photos/m_Mohamed_Hussien.jpg" },
      { name: "Omar Ahmed", role: "Multimedia Team Head", photo: "photos/m_Ammar_Mohamed.jpg" },
      { name: "Maryam Yasser", role: "Multimedia Team Vice Head", photo: "photos/m_Maryam_Yasser.jpg" },
      { name: "Lina", role: "Multimedia Team Vice Head", photo: "photos/m_Malak_Mohamed.jpeg" },
      { name: "Mohamed Yousef", role: "Tech Team Head", photo: "photos/m_Mohamed_San.jpeg" },
      { name: "Ahmed Anter", role: "Tech Team Vice Head", photo: "photos/m_Ahmed_Anter.png" },
      { name: "Loujaina Alber", role: "Presentation Team Head", photo: "photos/m_Loujaina_Alber.jpeg" },
      { name: "Retaj Haythem", role: "Presentation Team Vice Head", photo: "photos/m_Retaj_Haitham.jpeg" },
      { name: "Abdallh Mohamed", role: "PR Team Head", photo: "photos/m_Abdallh_Diwan.jpeg" },
      { name: "Malak Ashraf", role: "HR Team Head", photo: "photos/m_Malak_Ashraf.jpg" },
      { name: "Ahmed Khaled", role: "HR Team Vice Head", photo: "photos/m_Ahmed_Soliman.jpg" },
      { name: "Khadega Mahmoud", role: "Operations Team Head", photo: "photos/m_Khadega_Mahmoud1.jpg" },
      { name: "Darwin Alqmd", role: "Board Member", photo: "photos/m_Darwin_Alqmd.jpeg" }
    ],
    bridge: "جاهز تكون جزء من الحكاية؟"
  },'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace members block entirely
html = re.sub(r'members:\s*\{[\s\S]*?\n  \},', members_js, html)

# Remove timeline, achievements, voices from CONTENT object
html = re.sub(r'timeline:\s*\{[\s\S]*?\n  \},', '', html)
html = re.sub(r'achievements:\s*\{[\s\S]*?\n  \},', '', html)
html = re.sub(r'voices:\s*\{[\s\S]*?\n  \},', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated members and cleaned up unused CONTENT blocks.")
