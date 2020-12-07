#--------------------------------------------
#CONTROLADOR DE ESCRITA
#--------------------------------------------
from bs4 import BeautifulSoup

from src.file_formats.csv_format import write_csv, write_csv_header


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

#receve a categoria, um dicionario com chave "elemento" e o endereco do arquivo
#escreve no arquivo de saida o tipo, elemento e o conteudo do elemento
def write_tag_title_link(type, dict, file_address):
	file_type = file_address.split(".")[1]

	if(file_type=="csv"):
		write_csv(file_address,dict, type)
#escreve no arquivo de saída o conteudo das tag primaria e secundaria (formato tag.class)
def write_news_headline(html_content, primary_title_tag, secondary_title_tag, file_address):
	output_file = open(file_address,"a")
	split_primary_title_tag = primary_title_tag.split('.')
	split_secondary_title_tag = secondary_title_tag.split('.')
	header  = ["Tipo", "Notícia", "Link"]
	file_type = file_address.split(".")[1]

	if(file_type == "csv"):
		write_csv_header(header, file_address)

		dict_title_link = get_title_link(split_primary_title_tag[0],split_primary_title_tag[1], html_content)
		
		write_tag_title_link("Primário", dict_title_link, file_address)
		dict_title_link.clear()
		dict_title_link = get_title_link(split_secondary_title_tag[0],split_secondary_title_tag[1], html_content)
		write_tag_title_link("Secundário", dict_title_link, file_address)
