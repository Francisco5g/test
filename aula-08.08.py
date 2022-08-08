# ATENÇÃO!!
# Instalar biblioteca inquirer
# > pip install inquirer
import inquirer


class Aluno:
    def __init__(self, nome: str, disciplinas, serie: int, tempoLivre):
        self.nome = nome
        self.disciplinas = disciplinas
        self.serie = serie
        self.tempoLivre = tempoLivre


print('Quais matérias você tem?')
print('Se for mais que uma separe por espaços.')
disciplinas = str(input('> ')).split(' ')

perguntas_dificuldade_msg = 'Em quais dessas matérias você tem dificuldade? \nEspaço para selecionar ou desmarcar'
perguntas_dificuldade = [
    inquirer.Checkbox(
        'dificuldades', message=perguntas_dificuldade_msg, choices=disciplinas)
]

materias_com_dificuldade = inquirer.prompt(
    perguntas_dificuldade
)['dificuldades']
