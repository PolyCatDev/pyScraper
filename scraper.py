from bs4 import BeautifulSoup
import requests

class WebDown:
    def __init__(self):
        
        with open('memory/web_link.txt') as file:
            link = file.read()
        
        page_source = requests.get(link)
        soup = BeautifulSoup(page_source.content, "html.parser").prettify()

        with open('website.html', 'w') as file:
            file.write(soup)
