questions = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5*5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2',
        'Opções' : ['4', '5', '2', '1'],
        'Resposta' : '5',
    },
]

score = 0

for question in questions: 
    print()
    print(f'Pergunta: {question['Pergunta']}')

    options = question['Opções']

    for i, option in enumerate(options):
        print(f'{i + 1}) {option}')
    
    answer = input("Escolha uma opção: ")
    
    int_answer = None
    scored = False
    qtd_options = options.__len__()

    if answer.isdigit():
        int_answer = int(answer)
    
    if int_answer is not None:
        if int_answer >= 0 and int_answer < qtd_options:
            if options[int_answer - 1] == question['Resposta']:
                scored = True
            
    if scored:
        print("Scored!")
        score += 1
    else:
        print("Missed!")

print(f'Acertou {score} de {len(questions)} perguntas')

