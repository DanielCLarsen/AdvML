import re
import csv
from utils.progress_bar import progress_bar
import os
import json

def parse_wiki( wiki_data_path=os.path.join("data","dawiki-articles.xml"),
                output_file_path = os.path.join("data","wiki_dk_clean.csv"),
                max_articles = None,
                overwrite=False):

        if not os.path.isfile(wiki_data_path):
            raise Exception("Path for wiki file is not valid: ",wiki_data_path)

        if os.path.isfile(output_file_path) and not overwrite:
            print("Output file already exist, skipping parsing wiki")
            print("output path:",output_file_path)
        else:
            out_file = open(output_file_path,"w",encoding="utf8")
            wiki_file = open(wiki_data_path,'r',encoding="utf8")
            writer = csv.writer(out_file)
            __process_data(wiki_file,writer,max_articles)
            out_file.close()

def parse_wiki_w2v(
                wiki_data_path=os.path.join("data","dawiki-articles.xml"),
                output_file_path = os.path.join("data","wiki_dk_clean_w2v.txt"),
                max_articles = None,
                overwrite=False):
    if not os.path.isfile(wiki_data_path):
        raise Exception("Path for wiki file is not valid: ", wiki_data_path)

    if os.path.isfile(output_file_path) and not overwrite:
        print("Output file already exist, skipping parsing wiki")
        print("output path:", output_file_path)
    else:
        out_file = open(output_file_path, "w", encoding="utf8")
        wiki_file = open(wiki_data_path, 'r', encoding="utf8")
        __process_data_w2v(wiki_file, out_file, max_articles)
        out_file.close()
        wiki_file.close()

def __process_data_w2v(wiki_file,output_file,max_articles):

    page = ""
    if not max_articles:
        max_articles = 344000

    pb = progress_bar(max_articles)

    for line in wiki_file:
        if "<page>" in line:
            page = ""
            continue
        if "</page>" in line:
            title, text = __clean_page(page)
            if title:
                #TODO windows proof this
                output_file.write(text)
                if pb():
                    break
            continue
        page += line

def __process_data(wiki_file,writer,max_articles):
    if not max_articles:
        max_articles = 344000

    pb = progress_bar(max_articles,title="processing wikipedia")
    writer.writerow([max_articles])
    page=""
    for line in wiki_file:
        if "<page>" in line:
            page = ""
            continue
        if "</page>" in line:
            title, text = __clean_page(page)
            if title:
                #TODO windows proof this
                writer.writerow([text])

                if pb():
                    break
            continue
        page += line
def __clean_page(xml_page):

    try:
        if re.findall(r'<redirect[\s\S]*?/>', xml_page):
            return None, None
        title = re.findall(r'<title>([\s\S]*?)</title>', xml_page)[0]
        text = re.findall(r'<text xml:space="preserve">([\s\S]*?)</text>', xml_page)[0]
        text = re.sub(r'\[\[Fil[\s\S]*?\]\]\n', '', text)
        text = re.split(r'== Referencer ==', text)[0]
        text = re.split(r'== Noter ==', text)[0]
        text = re.sub(r'&[\s\S]*?;', '', text)
        text = re.sub(r'/ref', '', text)
        text = re.sub(r'{[\s\S]*?}', '', text)
        text = re.sub(r'http[\s\S]*? ', '', text)
        text = re.sub('[^A-Za-zøæå0-9]', ' ', text)
        text = re.sub('[\s]+', ' ', text)
        text = text.lower()

        if text:
            return title, text
        else:
            return None, None
    except:
        return None, None

def __write_vocab(output_file_path,words :set):
    vocab = {}
    pb = progress_bar(len(words),title="generating vocabulary")
    i = 0
    for word in words:
        if word and len(word)>1:
            vocab.update({word:i})
            #print({word:i})
            i+=1
            pb()

    file = open(output_file_path+"_vocab.json",'w',encoding="utf8")
    file.write(json.dumps(vocab))
    file.close()


