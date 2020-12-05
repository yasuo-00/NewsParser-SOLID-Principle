from bs4 import BeautifulSoup
import requests
from time import gmtime, strftime


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}

#recebe o html do site
html_content = requests.get('https://www.globo.com', headers=headers).text

strNow = strftime("%Y-%m-%d %H %M %S", gmtime()) 

#recebe o html do site
html_content = requests.get('https://www.globo.com', headers=headers).text
#realiza o parse do html utilizando lxml parser
soup = BeautifulSoup(html_content, "lxml")

output_file = open(strNow+"csvFile.csv", "a")
output_file.write("Tipo;Notícia;Link\n")

for title in soup.find_all("p", attrs={"hui-premium__title"}):
	output_file.write("Principal;{};".format(title.text))
	
	parent = title.find_parent("a")
	output_file.write("{}".format(parent.get("href")))
	output_file.write("\n")


