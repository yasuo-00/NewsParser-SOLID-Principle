# -*- coding: latin-1 -*-
#--------------------------------------------
#CONTROLADOR PRINCIPAL
#--------------------------------------------
from bs4 import BeautifulSoup
from time import gmtime, strftime
import requests

from src.controllers.WriteController import write_news_headline
from src.controllers.ReadController import read_site_list

#gera um arquivo com a extensao desejada, no local desejado (endereco deve existir)
def generate_file_name(extension, address):
	strNow = strftime("%Y-%m-%d %H %M %S", gmtime()) 
	if address =="" or address is None:
		file_name = strNow + extension+ "File."+extension
	else:
		file_name = address + "/" +strNow + extension+ "File."+extension
	return file_name


def run():
	#header para simular requisicao de um browser
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
	    'Content-Type': 'text/html',
	}

	#endereco a partir do main
	FILE_ADDRESS = "input/siteList.csv"
	file = open(FILE_ADDRESS)
	dict_site = read_site_list(FILE_ADDRESS)

	#para cada site no arquivo
	for site in dict_site:
		print(site)
		#recebe o html do site
		html_content = requests.get(site, headers=headers).text.encode("utf-8")
		#realiza o parse do html utilizando lxml parser
		soup = BeautifulSoup(html_content, "lxml")
		#gera um arquivo para escrita com a extensao desejada
		file_address= generate_file_name("csv", "output")
		#escreve o titulo e o link da noticia no arquivo
		write_news_headline(html_content, dict_site[site][0], dict_site[site][1], file_address)
