import re

# Исходная строка с формулами
text = "Некоторые формулы: $\\vec{S}$ и $\\vec{A}$"

# Регулярное выражение для замены
pattern = r'\$\s*\\vec{(.*?)}\s*\$'
replacement = r'\\( \vec{\1} )'

# Преобразование текста
new_text = re.sub(r'\$(.+?)\$', r'\\( \1 \\)', text)

print(new_text)
