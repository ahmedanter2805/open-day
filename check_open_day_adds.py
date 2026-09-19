import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

count = 0
for i, line in enumerate(lines):
    if 'add(' in line or 'addCover(' in line:
        count += 1
        print(f"Line {i+1}: {line.strip()[:60]}")

print("Total add calls:", count)
