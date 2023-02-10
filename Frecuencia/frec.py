import re
from pdfminer.high_level import extract_text
from nltk.corpus import stopwords
from math import ceil
def frequency(path='2591-0.txt', encoding="utf-8-sig"):
    stop_words = set(stopwords.words('english'))
    with open(path, 'r') as text:
        words = re.split(r'\W+', text.read().lower())
        filtered_words = []
        for w in words:
            if w not in stop_words:
                filtered_words.append(w)
        print(f"Palabras sin Stopwords {filtered_words[100:200]}")
        unique_words = set(filtered_words)
        dic={}
        for words in unique_words :
            #print('Frequency of ', words , 'is :', filtered_words.count(words))
            dic[filtered_words.count(words)] =words 
    return sorted(dic.items(),reverse=True)
    