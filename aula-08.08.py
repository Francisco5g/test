# ATENÇÃO!!
# Instalar biblioteca "inquirer"
# > pip install inquirer
import inquirer

class Aluno:
    def __init__(self, nome: str, disciplinas, serie: int, tempo: int):
        self.nome = nome
        self.disciplinas = disciplinas
        self.serie = serie
        self.tempo = int(tempo)
        self.dificuldade = []

        self.tempo_estudo_normal = 0.25 # 15min
        self.tempo_estudo_dificuldade = 0.75 # 45min

    def add_disciplina_dificuldade(self, disciplina):
        self.dificuldade.append(disciplina)

    def organizar(self):
        horas = 0

        for mat in self.dificuldade:
            tempo_dific = self.tempo_estudo_dificuldade

            horas += tempo_dific * 60
            print(f'Estude {int(tempo_dific * 60)}min para {mat}')

        for mat in self.disciplinas:
            if mat not in self.dificuldade:
                    
                tempo = self.tempo_estudo_normal

                horas += tempo * 60
                print(f'Estude {int(tempo * 60)}min para {mat}')



        print(f'Você estudurá {int(horas)}min no total. Ainda sobrará {self.tempo * 60 - int(horas)}min livres!')


print('Quais matérias você tem? ')
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