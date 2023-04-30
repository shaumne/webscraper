import requests
from bs4 import BeautifulSoup
import time


def scrapeData(url:str, element:str ,class_:str):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    }


    page = requests.get(url, headers)


    soup = BeautifulSoup(page.content, "html.parser")

    test = soup.find(element, class_=class_)

    print(test.text)

    return test.text

# scrapeData("https://www.livechart.me/anime/11084", "div", "expandable-text-body")