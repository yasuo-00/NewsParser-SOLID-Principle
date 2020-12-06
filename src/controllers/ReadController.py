# -*- coding: latin-1 -*-
#--------------------------------------------
#CONTROLADOR DE LEITURA
#--------------------------------------------
from src.file_formats.csv_format import read_csv_file


#leitura do arquivo com a lista de sites
def read_site_list(file_address):
	#dicionario de sites com chave = endereco
	#contendo a lista com a tag primaria e a tag secundaria
	dict_site= {}
	#pega a extensao do arquivo
	extension = file_address.split(".")[1]

	#verifica o tipo de arquivo
	if(extension == 'csv'):
		dict_site=read_csv_file(file_address)
	return dict_site

