class Aluno:
    def __init__(self, matricula, nome, n1, n2):  #__init__ é o construtor
        self.matricula = matricula
        self.nome = nome
        self.n1 = n1
        self.n2 = n2

    def calcular_media(self): 
    
        return (self.n1 + self.n2) / 2    
    
    def situacao(self):
        media = self.calcular_media()

        if media >= 7:
            return 'Aprovado(a)!'
        elif 5 <= media <= 6.9:
            return 'Em recuperação!'
        else:
            return 'Reprovado(a)!'        

