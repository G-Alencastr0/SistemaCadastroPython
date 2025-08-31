from funcoes import cadastrar
from funcoes import listar
from funcoes import alterar
from funcoes import excluir

alunos = []

while True:
    print('\n------ PÁGINA INICIAL ------')
    print('1 - Cadastrar alunos')
    print('2 - Listar alunos')
    print('3 - Alterar cadastro')
    print('4 - Excluir cadastro')
    print('5 - Sair do sistema')

    opcao = input('\nVocê está no sistema de cadastro Boletim EduSimples! Qual opção deseja utilizar?')
    
    match opcao:
        case '1':
            cadastrar(alunos)
        case '2':
            listar(alunos)   
        case '3':
            alterar(alunos)
        case '4':
            excluir(alunos)
        case '5':
            print('---> Saindo do sistema...')
            break
        case _:  #pega opções não listadas
            print('Opção inválida! Tente novamente.') 