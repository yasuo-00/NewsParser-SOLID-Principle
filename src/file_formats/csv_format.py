
#le um arquivo csv e retorna um dicionario com chave "endereco do site" contendo uma lista de tags 
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

#escreve o cabecalho no arquivo csv vazio
def write_csv_header(header, file_address):
	output_file=open(file_address,"a", encoding = "latin-1")
	#itera por todos os elementos da lista header menos o ultimo elemento
	for h in header[:-1]:
		output_file.write(h+";")
	output_file.write(header[-1]+"\n")
	output_file.close()

#escreve em um arquivo csv, o tipo, o conteudo da tag(do titulo de noticia), e o link
def write_csv(file_address, dict, type):
	output_file=open(file_address,"a", encoding = "latin-1")
	for dict_element in dict:
		output_file.write("{};{};{}".format(type, dict_element, dict[dict_element]))
		output_file.write("\n")
	output_file.close()
