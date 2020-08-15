import requests
from bs4 import BeautifulSoup
def coastcapital():
    URL = ' https://www.ratehub.ca/banks/bank-mortgage-rates '
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('table')
    print(result)
    