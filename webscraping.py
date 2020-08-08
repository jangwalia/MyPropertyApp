import requests
from bs4 import BeautifulSoup
def coastcapital():
    URL = 'https://www.coastcapitalsavings.com/rates/mortgages'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('table')
    """ html = '<table><tr><th>Feature</th></tr>'

    for index in range(8):
        html += str(results[index])
        if index % 2 == 1:
            html += '</tr><tr>'


    html += '</table>' """
    
    return results