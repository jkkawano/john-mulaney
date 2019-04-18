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



def get_special(special="new-in-town"):
    """
    Uses BeautifulSoup to parse an html file and extract the 'post-content' text
    """
    html_file = "data/html/" + special + ".html"
    out_file = "data/raw/raw-" + special
    write_bool = False
    with open(html_file) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    with open(out_file, "w") as f_out:
        f_out.write(soup.find('div', attrs={'class':'post-content'}).get_text())

def parse_new_in_town(special="new-in-town"):

    get_special(special)
    raw_file = "data/raw/raw-"+special
    out_file = "data/"+special
    
    write_bool = False
    with open(raw_file, "r") as fp:
        with open(out_file, "w") as fp_out:
            for l in fp:
                if l.startswith("(End)"):
                    write_bool = False
                if write_bool:
                    fp_out.write(l)
                if l.startswith("(Start)"):
                    write_bool = True

def parse_special(special):

    get_special(special)
    raw_file = "data/raw/raw-"+special
    out_file = "data/"+special

    with open(raw_file,"r") as fp:
        with open(out_file, "w") as fp_out:
            for l in fp:
                fp_out.write(l)
                    
if __name__ == "__main__":

    parse_new_in_town("new-in-town")
    parse_special("radio-city")
    parse_special("comeback-kid")

    print("street smarts!")
