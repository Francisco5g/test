# ATENÇÃO!!
# Instalar biblioteca "inquirer"
# > pip install inquirer
from ast import List
from re import A
import inquirer


class Aluno:
    def __init__(self, nome: str, disciplinas, serie: int, tempo):
        self.nome = nome
        self.disciplinas = disciplinas
        self.serie = serie
        self.tempo = tempo

    def add_disciplina_dificuldade(self, disciplina):
        print('Você tem dificuldade nisso', disciplina, self.disciplinas)

    def organizar(self):
        pass


print('Quais matérias você tem?')
print('Se for mais que uma separe por espaços.')

disciplinasTodas = str(input('> ')).split(' ')

perguntas_dificuldade_msg = 'Em quais dessas matérias você tem dificuldade? \nEspaço para selecionar ou desmarcar'
perguntas_dificuldade = [inquirer.Checkbox('dificuldades', message=perguntas_dificuldade_msg, choices=disciplinasTodas)]

disciplinasDificuldade = inquirer.prompt(perguntas_dificuldade)['dificuldades']

perguntas_aluno = [
    inquirer.Text('nome', 'Qual seu nome? '),
    inquirer.Text('tempo', 'Em média, quantas horas você tem livre por dia? '),
    inquirer.Text('serie', 'Qual a sua série? '),
]
perguntas_aluno_res = inquirer.prompt(perguntas_aluno)

aluno = Aluno(
    nome=perguntas_aluno_res['nome'], 
    disciplinas=disciplinasTodas, 
    tempo=perguntas_aluno_res['tempo'], 
    serie=perguntas_aluno_res['serie']
)

for disci in disciplinasDificuldade:
    aluno.add_disciplina_dificuldade(disci)

aluno.organizar()