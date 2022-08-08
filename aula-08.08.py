class Aluno:
    def __init__(self, nome: str, disciplinas, serie: int, tempoLivre):
        self.nome = nome;
        self.disciplinas = disciplinas;
        self.serie = serie
        self.tempoLivre = tempoLivre
        
# disciplinas = str(input('Disciplinas que você tem(separe por ","): '))
input_disciplinas = 'matemática, português, química'.split(',')
disciplinas = [i.strip() for i in input_disciplinas]

dificuldade_diciplinas = []

for dis in disciplinas:
    dificuldade = str(input(f'Você tem dificuldade em {dis}? (s/n)')).lower()
    
    dificuldade_diciplinas.append({ 
        "disciplina": dis, 
        "dificuldade": True if dificuldade == 's' else False  
    })
