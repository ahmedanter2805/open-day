import base64, io
from PIL import Image

try:
    im = Image.open('innovation_university_logo.jpg').convert('L')
    im = im.resize((800,800),Image.LANCZOS)
    lo,hi=95,235
    a = im.point(lambda v: 255 if v<=lo else 0 if v>=hi else 255 - int((v-lo)*255/(hi-lo)))
    bbox = a.getbbox()
    if bbox:
        pad = 12
        bbox = (max(0,bbox[0]-pad),max(0,bbox[1]-pad),min(800,bbox[2]+pad),min(800,bbox[3]+pad))
        a = a.crop(bbox)
    
    w,h = a.size
    s = 360/max(w,h)
    a = a.resize((int(w*s),int(h*s)),Image.LANCZOS)
    
    def mk(rgb):
        o = Image.new('RGBA',a.size,rgb+(0,))
        o.putalpha(a)
        b = io.BytesIO()
        o.save(b,'PNG',optimize=True)
        return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    
    logo_w = mk((255,255,255))
    logo_p = mk((58,42,114))
    
    m = a.copy()
    m.thumbnail((128,128),Image.LANCZOS)
    def mk_mark(rgb):
        o = Image.new('RGBA',m.size,rgb+(0,))
        o.putalpha(m)
        b = io.BytesIO()
        o.save(b,'PNG',optimize=True)
        return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    
    mark_w = mk_mark((255,255,255))
    mark_p = mk_mark((58,42,114))
    
    with open('template.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('__LOGO_W__', logo_w)
    html = html.replace('__LOGO_P__', logo_p)
    html = html.replace('__MARK_W__', mark_w)
    html = html.replace('__MARK_P__', mark_p)
    
    with open('index_3d.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Done!')
except Exception as e:
    print('Error:', e)
