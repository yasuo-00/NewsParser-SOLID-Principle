from bs4 import BeautifulSoup
import requests
from time import gmtime, strftime


def get_title_link(tag_name, attributes, html_content):
	soup = BeautifulSoup(html_content, "lxml")
	dict_title_link = {}
	#para cada elemento encontrado com a tag_name
	for element in soup.find_all(tag_name, attrs={attributes}):
		#pega o link do titulo
		link =element.find_parent("a").get("href")
		dict_title_link[element.text]=link
	return dict_title_link

def write_title_link(type, dict, file_address):
	output_file=open(file_address,"a")
	for element in dict:
		output_file.write("{};{};{}".format(type,element, dict[element]))
		output_file.write("\n")
	output_file.close()

def write_on_file(html_content, primary_title_tag, secondary_title_tag, file_address):
	output_file = open(file_address,"a")
	split_primary_title_tag = primary_title_tag.split('.')
	split_secondary_title_tag = secondary_title_tag.split('.')

	output_file.write("Tipo;Notícia;Link\n")

	dict_title_link = get_title_link(split_primary_title_tag[0],split_primary_title_tag[1], html_content)
	
	write_title_link("Primário", dict_title_link, file_address)
	dict_title_link.clear()
	dict_title_link = get_title_link(split_secondary_title_tag[0],split_secondary_title_tag[1], html_content)
	write_title_link("Secundário", dict_title_link, file_address)
	output_file.close()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}


strNow = strftime("%Y-%m-%d %H %M %S", gmtime()) 

#recebe o html do site
html_content = requests.get('https://www.globo.com', headers=headers).text.encode("utf-8")
#realiza o parse do html utilizando lxml parser
soup = BeautifulSoup(html_content, "lxml")

file_address=strNow+"csvFile.csv"

write_on_file(html_content, "p.hui-premium__title", "p.hui-highlight-title", file_address)
