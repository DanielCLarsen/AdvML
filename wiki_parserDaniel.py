import re
import csv

def clean_page(xml_page):

    try:
        if re.findall(r'<redirect[\s\S]*?/>', xml_page):
            return None,None
        title = re.findall(r'<title>([\s\S]*?)</title>', xml_page)[0]
        text = re.findall(r'<text xml:space="preserve">([\s\S]*?)</text>', xml_page)[0]
        text = re.sub(r'\[\[Fil[\s\S]*?\]\]\n','',text)
        text = re.split(r'== Referencer ==',text)[0]
        text = re.split(r'== Noter ==',text)[0]
        text = re.sub(r'&[\s\S]*?;','',text)
        text = re.sub(r'/ref', '', text)
        text = re.sub(r'{[\s\S]*?}','',text)
        text = re.sub(r'http[\s\S]*? ', '', text)
        text = re.sub('[^A-Za-zøæå]', ' ', text)
        text = re.sub('[\s]+',' ', text)
        text = text.lower()

        if text:
            return title,text
        else:
            return None,None
    except:
        return None,None



text_dict = {}
xml_content = ""
pages = []
page = ""
count = 0
first = True
file = open("wiki_dk_clean.csv","w", encoding="utf8")
w = csv.writer(file)
#max_art = 1000
for line in open("dawiki-articles.xml",'r',encoding="utf8"):
    if "<page>" in line:
        page = ""
        continue
    if "</page>" in line:
        title,text = clean_page(page)

        if title:
            count += 1
            w.writerow([title,text])
            #if count > max_art:
             #   break
        continue

    page += line

file.close()
print(count)