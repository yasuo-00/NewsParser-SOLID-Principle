# -*- coding: latin-1 -*-
from bs4 import BeautifulSoup
import requests
from time import gmtime, strftime

def read_site_list(file_address):
	dict_site= {}
	with open(file_address) as input_file:
		next(input_file)
		for line in input_file:
			split_line = line.split(";")
			dict_site[split_line[0]]=[split_line[1], split_line[2].rstrip("\n")]
	input_file.close()
	return dict_site


def generate_file_name(extension):
	strNow = strftime("%Y-%m-%d %H %M %S", gmtime()) 
	file_name = strNow + "csvFile."+extension
	return file_name

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
	output_file=open(file_address,"a", encoding = "latin-1")
	for element in dict:
		output_file.write("{};{};{}".format(type,element, dict[element]))
		output_file.write("\n")
	output_file.close()

def write_on_file(html_content, primary_title_tag, secondary_title_tag, file_address):
	output_file = open(file_address,"a", encoding = "latin-1")
	split_primary_title_tag = primary_title_tag.split('.')
	split_secondary_title_tag = secondary_title_tag.split('.')

	output_file.write("Tipo;Notícia;Link\n")
	output_file.close()

	dict_title_link = get_title_link(split_primary_title_tag[0],split_primary_title_tag[1], html_content)
	
	write_title_link("Primário", dict_title_link, file_address)
	dict_title_link.clear()
	dict_title_link = get_title_link(split_secondary_title_tag[0],split_secondary_title_tag[1], html_content)
	write_title_link("Secundário", dict_title_link, file_address)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}

dict_site = read_site_list("src/siteList/siteList.csv")

for site in dict_site:
	#recebe o html do site
	html_content = requests.get(site, headers=headers).text.encode("utf-8")
	#realiza o parse do html utilizando lxml parser
	soup = BeautifulSoup(html_content, "lxml")
	file_address= generate_file_name("csv")
	write_on_file(html_content, dict_site[site][0], dict_site[site][1], file_address)
