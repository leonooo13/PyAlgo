import re

s = "A 对不同网络之间的互联、互通进行安全保护  B  对不同定级系统之间的互联、互通进行安全保护 C dedefe deede D frefgrg"
pattern = r'([A-Z])\s+(.+?)\s+(?=[A-Z]|$)'
result = re.sub(pattern, r'\1 \2\n', s)

print(result)
