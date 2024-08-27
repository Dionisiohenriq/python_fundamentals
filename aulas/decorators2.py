def decorators_factory(a=None, b=None, c=None):
    def function_factory(func):
        print('Decorator 1')

        def intern(*args, **kwargs):
            print('Intern')
            for arg in args:
                is_number(arg)

            res = func(*args, **kwargs)
            return res
        return intern
    return function_factory


def is_number(number):
    if not isinstance(number, int):
        raise TypeError("param must be an integer number.")


@decorators_factory(1, 2, 3)
def sum_numbers(x, y):
    return x + y


multiply = decorators_factory()(lambda x, y: x * y)

ten_plus_five = sum_numbers(10, 5)
ten_x_five = multiply(10, 5)
print(ten_plus_five)
print(ten_x_five)
