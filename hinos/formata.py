import os
import re

diretorio = "."  # Diretório atual

def processar_arquivos(diretorio):
    for filename in os.listdir(diretorio):
        if filename.endswith('.md'):
            filepath = os.path.join(diretorio, filename)
            with open(filepath, 'r') as file:
                linhas = file.readlines()

                if len(linhas) > 1:
                    match = re.match(r'^(\d+)\s*-\s*(.*)', linhas[0])
                    if match:
                        numero = match.group(1)
                        titulo = match.group(2)

                        linhas = linhas[2:] if linhas[1].strip() == '' else linhas[1:]

                        with open(filepath, 'w') as file:
                            file.write('---\n')
                            file.write(f"numero: {numero}\n")
                            file.write(f"titulo: {titulo}\n")
                            file.write('---\n')
                            file.write(''.join(linhas))
                    else:
                        print(f"Não foi possível extrair número e título de {filename}")

processar_arquivos(diretorio)
