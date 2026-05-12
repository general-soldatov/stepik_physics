import markdown
import os
import re

FOLDER = 'biotech-lection'
for name in os.listdir(path=FOLDER):
    path_data = os.path.join(FOLDER, name)
    with open(path_data, encoding='utf-8') as file:
        html = markdown.markdown(file.read())
    html = re.sub(r'\$(.+?)\$', r'\\( \1 \\)', html)
    path = os.path.join('html', f'{name.split('.')[0]}.html')
    with open(path, 'w', encoding='utf-8') as file:
        file.write(html)
    print('Create', path)
