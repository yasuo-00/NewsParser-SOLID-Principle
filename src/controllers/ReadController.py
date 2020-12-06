# -*- coding: latin-1 -*-

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

def read_csv_file(file_address):
	dict_site={}
	#abre o arquivo csv e ignora o header (primeira linha)
	with open(file_address) as input_file:
		next(input_file)
		#para cada linha no arquivo
		for line in input_file:
			#realiza o split para pegar as informacoes do site (endereco, tag_noticia_primaria, tag_noticia_secundaria)
			split_line = line.split(";")
			dict_site[split_line[0]]=[split_line[1], split_line[2].rstrip("\n")]
	input_file.close()
	return dict_site