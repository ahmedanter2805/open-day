import os, re, shutil

def fix_repo(repo_path):
    photos_dir = os.path.join(repo_path, 'photos')
    if os.path.exists(photos_dir):
        for f in os.listdir(photos_dir):
            if 'Màřwàñ' in f or 'à' in f or 'ř' in f or 'ñ' in f:
                old_p = os.path.join(photos_dir, f)
                new_p = os.path.join(photos_dir, 'm_Marwan_Mohammed.jpg')
                if old_p != new_p:
                    if os.path.exists(new_p): os.remove(new_p)
                    os.rename(old_p, new_p)
                    
    items_js = '''  members: {
    title: "الناس اللي ورا الحكاية",
    hint: "اضغط على الصورة عشان تشوف اللي بعدها",
    items: [
      { name: "Hana Yasser", role: "President", photo: "photos/m_Hana_Yasser.jpeg" },
      { name: "Youssef Abdelrazk", role: "Vice President", photo: "photos/m_Youssef_Abdelrazk.png" },
      { name: "Ziad Fadel", role: "Treasurer", photo: "photos/m_Ziad_Fadel.jpg" },
      { name: "Ahmed Anter", role: "Head of Tech Team", photo: "photos/m_Ahmed_Anter.png" },
      { name: "Eyad Mohamed", role: "Projects Team Head", photo: "photos/m_Eyad_Mohamed.jpg" },
      { name: "Basmala Talaat Belal", role: "Projects Team Vice Head", photo: "photos/m_Basmala_Talaat_Belal.jpg" },
      { name: "Marwan Mohammed", role: "Research Team Head", photo: "photos/m_Marwan_Mohammed.jpg" },
      { name: "Hamdy Mado", role: "Research Team Vice Head", photo: "photos/m_Hamdy_Mado.jpg" },
      { name: "Rahma Ibrahim", role: "Marketing Team Head", photo: "photos/m_Rahma_Ibrahim.jpg" },
      { name: "Mohamed Hussien", role: "Marketing Team Vice Head", photo: "photos/m_Mohamed_Hussien.jpg" },
      { name: "Maryam Yasser", role: "Multimedia Team Vice Head", photo: "photos/m_Maryam_Yasser.jpg" },
      { name: "Loujaina Alber", role: "Presentation Team Head", photo: "photos/m_Loujaina_Alber.jpeg" },
      { name: "Retaj Haitham", role: "Presentation Team Vice Head", photo: "photos/m_Retaj_Haitham.jpeg" },
      { name: "Abdallh Diwan", role: "PR Team Head", photo: "photos/m_Abdallh_Diwan.jpeg" },
      { name: "Malak Ashraf", role: "HR Team Head", photo: "photos/m_Malak_Ashraf.jpg" },
      { name: "Khadega Mahmoud", role: "Operations Team Head", photo: "photos/m_Khadega_Mahmoud1.jpg" },
      { name: "Ahmed Soliman", role: "Board Member", photo: "photos/m_Ahmed_Soliman.jpg" },
      { name: "Ammar Mohamed", role: "Board Member", photo: "photos/m_Ammar_Mohamed.jpg" },
      { name: "Darwin Alqmd", role: "Board Member", photo: "photos/m_Darwin_Alqmd.jpeg" },
      { name: "Malak Mohamed", role: "Board Member", photo: "photos/m_Malak_Mohamed.jpeg" },
      { name: "Mohamed San", role: "Board Member", photo: "photos/m_Mohamed_San.jpeg" }
    ],
    bridge: "جاهز تكون جزء من الحكاية؟"
  },'''

    html_path = os.path.join(repo_path, 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(r'members:\s*\{[\s\S]*?\n  \},', items_js, html)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Fixed {repo_path}")

fix_repo(r"c:\Users\Ahmed Anter\Documents\antigravity\test-repo")
fix_repo(r"c:\Users\Ahmed Anter\Documents\antigravity\quick-mendel\open-day")
