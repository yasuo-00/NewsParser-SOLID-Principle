# NewsParser-SOLID-Principle
Ferramenta para encontrar e baixar títulos das notícias do dia, nos principais sites de notícias (G1, UOL, etc).

Para rodar, execute no terminal "python3 main.py" na pasta principal

A saída está configurada para serem escritas na pasta output.

Para adicionar mais sites, crie uma nova linha no arquivo input/siteList.csv seguindo o formato das linhas existentes (site;tag_primaria.class_da_tag;tag_secundaria.class_da_tag).

A pasta file_formats é destinada a métodos de leitura e escrita de formatos de arquivo diferentes.

A pasta src/controllers é destinada aos métodos de controle da aplicação. Possui um controlador de escrita, um de leitura e um principal.
