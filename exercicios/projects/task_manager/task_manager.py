# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar
# todo = [ ] -> lista de tarefas
# todo = ['fazer café] -> adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> adicionar caminhar
# desfazer = ['fazer café', ] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['fazer café', 'caminhar']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


def menu():
    print('Comandos:')
    print('1 - Adicionar tarefa')
    print('2 - Desfazer')
    print('3 - Refazer')
    print('4 - Listar tarefas')
    print('5 - Sair')


todo = []
undo_stack = []


def add_task(task):
    todo.append(task)
    undo_stack.clear()


def undo():
    if todo:
        task = todo.pop()
        undo_stack.append(task)


def redo():
    if undo_stack:
        task = undo_stack.pop()
        todo.append(task)


def list_tasks():
    if todo:
        print("\nTarefas:")
        for index, task in enumerate(todo, start=1):
            print(f"{index}. {task}")
    else:
        print("\nNenhuma tarefa na lista.")
    print()


while True:
    menu()
    command = input("\nDigite o número do comando: ")

    if command == '1':
        task = input("Digite a tarefa a ser adicionada: ")
        add_task(task)
        print(f"Tarefa '{task}' adicionada.")
    elif command == '2':
        undo()
        print("Ação desfeita.")
    elif command == '3':
        redo()
        print("Ação refeita.")
    elif command == '4':
        list_tasks()
    elif command == '5':
        print("Saindo do programa.")
        break
    else:
        print("Comando inválido. Por favor, tente novamente.")
