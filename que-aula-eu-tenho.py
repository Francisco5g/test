classesHandler = {
    "segunda": "Matemática",
    "terça": "Português",
    "quarta": "Física",
    "quinta": "Filosofia",
    "sexta": "Inglês",
}

def getClassesByDay(day: str):
    if not day in classesHandler.keys():
        print(f'dia "{day}" não reconhecido! Tente novamente')
        
        return
    
    print(f'Você tem aula de {classesHandler[day]} hoje!')
    

day = str(input('Que dia é hoje? ')).lower()

getClassesByDay(day)