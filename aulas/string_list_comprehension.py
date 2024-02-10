string = 'Henrique Dionisio Ferreira'

number_of_characters = 1

list_string = '.'.join([string[index:index + number_of_characters] for index in range(0, len(string), number_of_characters)]) 
print(list_string)

names = ['luiz', 'maria', 'helena', 'joana', 'felipe']

new_names = [f'{name[:-1].lower()}{name[-1].upper()}' for name in names]

print(new_names)