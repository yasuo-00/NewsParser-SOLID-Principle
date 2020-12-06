# -*- coding: latin-1 -*-
from bs4 import BeautifulSoup

#retorna o conteudo da tag e o link respectivo
def get_title_link(tag_name, attributes, html_content):
	soup = BeautifulSoup(html_content, "lxml")
	dict_title_link = {}
	#para cada elemento encontrado com a tag_name
	for element in soup.find_all(tag_name, attrs={attributes}):
		#pega o link do titulo
		link =element.find_parent("a").get("href")
		dict_title_link[element.text]=link
	return dict_title_link

#escreve no arquivo de saida o tipo, elemento e o conteudo do elemento
def write_tag_title_link(type, dict, file_address):
	output_file=open(file_address,"a", encoding = "latin-1")
	for element in dict:
		output_file.write("{};{};{}".format(type,element, dict[element]))
		output_file.write("\n")
	output_file.close()

def write_news_headline(html_content, primary_title_tag, secondary_title_tag, file_address):
	output_file = open(file_address,"a", encoding = "latin-1")
	split_primary_title_tag = primary_title_tag.split('.')
	split_secondary_title_tag = secondary_title_tag.split('.')

	output_file.write("Tipo;Notícia;Link\n")
	output_file.close()

	dict_title_link = get_title_link(split_primary_title_tag[0],split_primary_title_tag[1], html_content)
	
	write_tag_title_link("Primário", dict_title_link, file_address)
	dict_title_link.clear()
	dict_title_link = get_title_link(split_secondary_title_tag[0],split_secondary_title_tag[1], html_content)
	write_tag_title_link("Secundário", dict_title_link, file_address)
