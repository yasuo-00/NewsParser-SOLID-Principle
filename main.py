from bs4 import BeautifulSoup
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}

html_content = requests.get('https://www.globo.com', headers=headers).text

soup = BeautifulSoup(html_content, "lxml")
print(soup.prettify())