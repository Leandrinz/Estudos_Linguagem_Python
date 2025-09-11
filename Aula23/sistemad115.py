from d115.interface.lib.init import *
from d115.interface.Arquivo import *
import time


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
   criarArquivo(arq)
    

cabeçalho("SISTEMA ARQUIVO v1.0")
while True:
    resposta = menu(["Ver pessoas cadastradas", "Casdastrar novas pessoas", "Sair do Programa"])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print(f"\033[31mErro!!! Digite uma opção válida\033[31m")
    time.sleep(2)
