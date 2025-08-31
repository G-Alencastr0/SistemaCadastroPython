from aluno import Aluno


def cadastrar(alunos):
    try:
        matricula = int(input('Digite a matrícula:'))

        #para verificar se a matrícula já existe dentro da função
        for i in alunos:
            if i.matricula == matricula:
                print('A matrícula {matricula} já existe!')
                return False  #False indica que o cadastro deu errado

        nome = input('Digite o nome do(a) aluno(a): ')
        n1 = float(input('Digite a primeira nota do(a) aluno(a): '))
        n2 = float(input('Digite a segunda nota do(a) aluno(a): '))

        #para verificar notas
        if not (0 <= n1 <= 10) or not (0 <= n2 <= 10):  #Se n1 não está entre 0 e 10 ou n2 não está entre 0 e 10
            print('Nota deve estar entre 0 a 10!')
            return False

        aluno1 = Aluno(matricula, nome, n1, n2)  #criei um objeto da classe Aluno
        alunos.append(aluno1)                    #adicionei o objeto na lista alunos
        print(f'Aluno(a) {nome} cadastrado(a) com sucesso!')
        return True

    except ValueError:
        print('Erro: digite números válidos.')



def listar(alunos):
    if not alunos: #se não tiver alunos
        print('Nenhum aluno cadastrado ainda...')
        return

    print('\n----- Lista de alunos cadastrados -----')
    for i in alunos:
        media = i.calcular_media()
        situacao = i.situacao()
        print(f'Matrícula: {i.matricula} | Nome: {i.nome} | Nota1: {i.n1} | Nota2: {i.n2} | Média: {media:.2f} | Situação: {situacao}')




def alterar(alunos):
    try:
        matricula = int(input('Digite a matrícula do aluno que deseja alterar o cadastro: '))

        for i in alunos:
            if i.matricula == matricula:
                print(f'Aluno(a) encontrado(a): {i.nome}')

                novo_nome = input('Novo nome (deixe vazio se não deseja alterar): ').strip()
                if novo_nome:
                    i.nome = novo_nome

                nova_n1 = input('Nova n1 (deixe vazio se não deseja alterar): ').strip()
                if nova_n1:
                    i.n1 = float(nova_n1)

                nova_n2 = input('Nova n2 (deixe vazio se não deseja alterar): ').strip()
                if nova_n2:
                    i.n2 = float(nova_n2)

                print(f'Dados do(a) aluno(a) {i.nome} alterados com sucesso!')
                return

        print('Aluno(a) não encontrado(a).')

    except ValueError:
        print('Erro: digite valores válidos.')



def excluir(alunos):
    try:
        matricula = int(input('Digite a matrícula do aluno que deseja excluir o cadastro: ')) 

        for i in alunos:
            if i.matricula == matricula:
                print(f'Aluno(a) encontrado(a): {i.nome}')
                confirmacao = input(f'Deseja mesmo excluir o cadastro do(a) aluno(a) {i.nome}? Confirmar (s/n): ').lower().strip()

                if confirmacao == 's':
                    alunos.remove(i)
                    print(f'Exclusão do cadastro do(a) aluno(a) {i.nome} concluída.')
                    return True
                
                else:
                    print(f'Exclusão do cadastro do(a) aluno(a) {i.nome} cancelada.')
                    return False

        print('Aluno(a) não encontrado(a).')
        return False
        
    except ValueError:
        print('Digite uma matrícula válida.')    
