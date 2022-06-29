from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt 
from PIL import Image
from os import path, getcwd
import numpy as np
import PyPDF2

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def get_soup(webpage):
    """ get data for web page"""
    r = requests.get(url) # request html from url 
    soup = BeautifulSoup(r.content, 'html.parser') # create a beautiful soup object 
    return soup 

def get_links(soup): 
    """ Get links from a web page """
    http_link_list = [] 
    current_link = ''
    for link in soup.find_all('a', href=True):
        current_link = link.get('href')
        if current_link.endswith('pdf'):
            http_link_list.append(current_link)
    return http_link_list 

def read_pdf(pdf_link): 
    pdfFileObject = open(pdf_link, 'rb') # create a pdf file object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject) # creating a pdf reader object 
    count = pdfReader.numPages
    count
# =============================================================================
#     for i in range(count):
#         page = pdfReader.getPage(i)
#         output = page.extractText()
#     output 
# =============================================================================
    
    
def get_episode_text(episode_list): 
    """get text from all episodes in list"""
    text_return = []
    for i in episode_list: 
        print(i)
        soup = get_soup(i)
        
# webpage
url = 'https://www.alieward.com/ologies-extras'

#gets word soup from website 
soupout = get_soup(url)

# get list of transcript links 
link_list = get_links(soupout)

# test pdf extraction 
pdf_text = read_pdf('Ologies+Aperiology.pdf')
pdf_text
