from bs4 import BeautifulSoup
import requests

def get_soup(webpage):
    """ get data for web page"""
    r = requests.get(webpage) 
    soup = BeautifulSoup(r.content, 'html.parser')  
    return soup 

def get_links(soup): 
    """ Get links to transcripts from web page """
    http_link_list = [] 
    current_link = ''
    for link in soup.find_all(class_="audio-tool audio-tool-transcript"):
        http_link_list.append(link.a.get('href'))
    return http_link_list

def get_ptags(soup):
    """get <p> tags from web page"""
    http_link_list = [] 
    for link in soup.find_all('p'):
        http_link_list.append(link.get_text())
    return http_link_list 

def get_text(text_array): 
    """ get text from an array"""
    text = " ".join(text_array)
    return text

def get_episode_text(episode_url):
    text_return = ""
    soup = get_soup(episode_url)
    text_array = get_ptags(soup)
    return(text_array)


def get_all_episode_text(episode_list):
    """get text for all episodes in list""" 
    text_return = []
    for episode in episode_list: 
        soup = get_soup(episode)
        text_array = get_ptags(soup)
        #full_text = get_text(text_array)
        text_return.append(text_array)
    return text_return


# webpage 
url = "https://www.npr.org/podcasts/510338/all-guides"
episode_url = "https://www.npr.org/transcripts/1107456623"

#gets word soup from website 
soupout = get_soup(url)

# get list of transcript links 
link_list = get_links(soupout)

# get list of all episode text 
text_return = get_all_episode_text(link_list)
print(text_return[1])

