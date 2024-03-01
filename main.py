import csv
import string


import re
import emoji


words=[]
csv_contents = []
vocab=[]
def remove_links(texto_limpo):
    cleaned_text = re.sub(r'http\S+|www\S+', '', texto_limpo)
    return cleaned_text

def remove_usernames(texto_limpo):
    cleaned_text = re.sub(r'@\w+','',texto_limpo)
    return cleaned_text

def remove_emojis(texto_limpo):
    emoj = re.compile("["
                      u"\U0001F600-\U0001F64F"  # emoticons
                      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                      u"\U0001F680-\U0001F6FF"  # transport & map symbols
                      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                      u"\U00002500-\U00002BEF"  # chinese char
                      u"\U00002702-\U000027B0"
                      u"\U00002702-\U000027B0"
                      u"\U000024C2-\U0001F251"
                      u"\U0001f926-\U0001f937"
                      u"\U00010000-\U0010ffff"
                      u"\u2640-\u2642"
                      u"\u2600-\u2B55"
                      u"\u200d"
                      u"\u23cf"
                      u"\u23e9"
                      u"\u231a"
                      u"\ufe0f"  # dingbats
                      u"\u3030"
                      "]+", re.UNICODE)
    cleaned_text = re.sub(emoj,'', texto_limpo)
    return cleaned_text

def remove_hashtags(texto_limpo):
    cleaned_text = re.sub(r"#\w+", "", texto_limpo)
    return cleaned_text
def remove_comercial(texto_limpo):
    cleaned_text = re.sub(r"&\w+", "", texto_limpo)
    return cleaned_text
def remover_pontos(texto_limpo):
    cleaned_text = texto_limpo.translate(str.maketrans('','',string.punctuation))
    return cleaned_text

def remover_numeros(texto_limpo):
    cleaned_text = re.sub(r'\d+', '',texto_limpo)
    return cleaned_text

with open('1000posts_en.csv','r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',',quotechar='"')
    for row in csv_reader:
        row=row[0]
        row =row.lower()
        texto_limpo=remove_links(row)
        texto_limpo=texto_limpo.replace("’","").replace("taliban","").replace("adhd","").replace("sergey","").replace("lavrov","")
        texto_limpo=texto_limpo.replace("biden","").replace("zelensky","").replace("trump","").replace("google","").replace("⁦⁩","").replace("à","").replace("ukraine","").replace("eminem","")
        texto_limpo=texto_limpo.replace("putin","").replace("…","").replace("–","").replace("·","").replace("–","").replace("kyiv","").replace("russians","").replace("russias","").replace("dumbass","")
        texto_limpo=texto_limpo.replace("«","").replace("»","").replace("√","").replace("‘","").replace("—","").replace("“","").replace("”","").replace("£","").replace("natos","").replace("bitcoin","")
        texto_limpo = texto_limpo.replace ( "አልረሳውም።" , "" ).replace("እናስፍርበት","").replace("ህዝብ","").replace("እና","").replace("እንውረር","").replace("የመንን","").replace("ደቡብ","").replace ( "መቼም" , "" ).replace("ያለውን","")
        texto_limpo=remove_usernames(texto_limpo)
        texto_limpo = remove_emojis(texto_limpo)
        texto_limpo = remove_hashtags(texto_limpo)
        texto_limpo = remove_comercial(texto_limpo)
        texto_limpo=remover_pontos(texto_limpo)
        texto_limpo=remover_numeros(texto_limpo)
        csv_contents.append(texto_limpo)

print(csv_contents)


for post in csv_contents:

    palavras = post.split()
    words= words+palavras



with open ('words.txt') as txtfile:
    vocabulario=txtfile.readlines()
    for palavra in vocabulario:
        palavra=palavra.replace("\n","").replace("'","")
        palavra=palavra.lower()
        vocab.append(palavra)

with open ("palavrasadicionar.txt","w", encoding="utf-8") as file:
    for word in words:
        if word not in vocab:
            print(word)
            file.write(word+"\n")
