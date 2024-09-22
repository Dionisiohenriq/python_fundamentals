def decorators_parameters(name):
    def decorator(func):
        print('Decorator:', name)

        def your_new_function(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {name}'
            return final
        return your_new_function
    return decorator

@decorators_parameters(name='second')
@decorators_parameters(name='first')
def sum(x, y):
    return x + y


ten_plus_five = sum(10, 5)
print(ten_plus_five)
