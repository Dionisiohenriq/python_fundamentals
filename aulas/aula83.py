person = {
    'name': 'Henrique',
    'lastname': 'Ferreira',
}

person_data = {
    'age': 35,
    'height': 1.83,
}

complete_person = {**person, **person_data}

def show_dictionary(*args, **kwargs):

    print(args)

    for key, value in kwargs.items():
        print(key, value)


# kwargs - named arguments (keyword arguments)
show_dictionary(**complete_person)       

configurations = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}

show_dictionary(**configurations)