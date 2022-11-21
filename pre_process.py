import re
import os
import string
from lxml import html
from lxml.html.clean import clean_html,Cleaner
import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter



def file_preprocess(text):
    
    #remove all the html, css and javascript tags
    tag_clean = Cleaner(embedded=True, meta=True, page_structure=True, links=True, style=True, scripts=True, javascript=True,
                      comments=True, forms=True,
                      remove_tags = ['a', 'li', 'td', 'span', 'font', 'div', 'http'])
    
    file_cleaning = tag_clean.clean_html(text)             
    pattern = re.compile(r'[^a-zA-Z]')            
    
    #removed everything except character or words
    file_cleaning = pattern.sub(' ',file_cleaning)
    file_cleaning = file_cleaning.lower()
    #remove multiple spaces from text
    file_cleaning = re.sub( '\s+', ' ', file_cleaning).strip()    #removed multiple spaces
    doc_file = re.sub(r'\b\w\b', '', file_cleaning)
    
    tokens = word_tokenize(doc_file)                #tokenized the words
    stop_list = set(stopwords.words("english")) # setting up list of stop words
    file = [words for words in tokens if not words in stop_list]

    stemmer = PorterStemmer()                   #used code for porter stemmer
    stemmed = []
    for words in file:
        stemmed.append(stemmer.stem(words))
    text=''
    for i in stemmed:
        text = text +' '+ str(i)
    return text

def Query_preprocess(text):
    
    #text_cleaning = tag_clean.clean_html(text)
    pattern = re.compile(r'[^a-zA-Z]')            
    text_cleaning = pattern.sub(' ',text)
    text_cleaning = re.sub('<script>.*?</script>', '', text_cleaning)
    text_cleaning = ''.join(ch.isaplha() for ch in text_cleaning)
    text_cleaning = re.sub( '\s+', ' ', text_cleaning).strip()
    text_cleaning = ' '.join(text_cleaning.split())
    #removed everything except character or words
    text_cleaning = text_cleaning.lower()
    #remove multiple spaces from text
        #removed multiple spaces
    doc_file = re.sub(r'\b\w\b', '', text_cleaning)
    #doc_file = " ".join(Counter(doc_file.split()).keys())
    tokens = word_tokenize(doc_file)              #tokenized the uniques words
    stop_list = set(stopwords.words("english")) # setting up list of stop words
    file = [words for words in tokens if not words in stop_list]
    
    stemmer = PorterStemmer()                   #used code for porter stemmer
    stemmed = []
    for words in file:
        stemmed.append(stemmer.stem(words))
    
    return stemmed