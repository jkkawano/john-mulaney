## Julia Kawano
## A script to scrape some websites for John Mulaney content

"""
This is going to do something related to John Mulaney! (maybe. can't scrape the site I want...)

Much code for making the request is from the tutorial at:
https://realpython.com/python-web-scraping-practical-introduction/

"""

from requests import get
from requests.exceptions import RequestException
from contextlib import closing

from bs4 import BeautifulSoup

def basic_get(url):
    """
    Attempts to get content from 'url' by making HTTP GET request
    If the request goes through, it returns the content. Otherwise returns None and prints error message
    """
    try:
        with closing(get(url)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Helper method for basic_get
    Returns True if the response seems to be HTML, False otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)



def get_new_in_town(html_file="/data/html/new-in-town.html", out_file="/data/raw-new-in-town"):
    """
    Uses BeautifulSoup to parse an html file and extract the 'post-content' text
    """
    write_bool = False
    with open(html_file) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    with open(out_file, "w") as f_out:
        f_out.write(soup.find('div', attrs={'class':'post-content'}).get_text())

def parse_new_in_town():

    get_new_in_town()
    
    write_bool = False
    with open("data/raw-new-in-town", "r") as fp:
        with open("data/new-in-town", "w") as fp_out:
            for l in fp:
                if l.startswith("(End)"):
                    write_bool = False
                if write_bool:
                    fp_out.write(l)
                if l.startswith("(Start)"):
                    write_bool = True

if __name__ == "__main__":

    print("street smarts!")
    #    get_new_in_town()
    parse_new_in_town()

    #    url = "https://scrapsfromtheloft.com/2017/09/25/john-mulaney-new-in-town-2012-full-transcript/"
    #    print(basic_get(url))

               
