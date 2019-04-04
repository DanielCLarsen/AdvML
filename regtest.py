
import re

with open("regtest.txt") as f:
    xml = f.read()

print(xml)
page = re.findall(r'<page>[\s\S]*?</page>',xml)

print(len(page))
print(page)