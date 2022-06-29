from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt 
from PIL import Image
from os import path, getcwd
import numpy as np
from urllib.request import unquote

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def get_soup(webpage):
    """ get data for web page"""
    r = requests.get(url) # request html from url 
    soup = BeautifulSoup(r.content, 'html.parser') # create a beautiful soup object 
    return soup 

def get_links(soup): 
    """ Get links from web page """
    http_link_list = [] 
    current_link = ''
    for link in soup.find_all('a', href=True):
        current_link = link.get('href')
        if current_link.endswith('pdf'):
            http_link_list.append(current_link)
    return http_link_list 

def get_episode_text(episode_list): 
    """get text from all episodes in list"""
    text_return = []
    pdf_url = 'https://www.alieward.com' + episode_list[0]
    print(pdf_url)
    
    # make HTTP GET request to fetch PDF bytes
    pdf_response = requests.get(pdf_url)
    print(pdf_response.content)
    
    
    # write PDF to local file
    #f.write(pdf_response.content)

     #   text_return.append(pdf_response)
    #return text_return

'''
def read_pdf(pdf_link): 
    pdfFileObject = open(pdf_link, encoding="utf8") # create a pdf file object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject) # creating a pdf reader object 
    num_pages = pdfReader.numPages
    text = ""
    page = pdfReader.getPage(0)
    text += page.extract_text() + "\n"


    for i in range(count):
        page = pdfReader.getPage(i)
        output = page.extractText()
     return output 
'''


        
# webpage
url = 'https://www.alieward.com/ologies-extras'

#gets word soup from website 
soupout = get_soup(url)

# get list of transcript links 
link_list = get_links(soupout)

# test pdf extraction 
pdf_text = get_episode_text(link_list)
