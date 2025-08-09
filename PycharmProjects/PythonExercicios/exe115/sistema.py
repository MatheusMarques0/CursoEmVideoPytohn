from exe115.lib.Interface import *
from time import sleep
from exe115.lib.arquivo import *

arq = 'CursoEmVideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de Cadastrar uma nova pessoa.
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = str(input('Idade: '))
        Cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31m[ERRO] Digite uma opção válida!\033[m')
    sleep(1)