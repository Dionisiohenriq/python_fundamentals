def create_function(func):
    def intern(*args, **kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f"Your result was {result}")
        return result
    return intern

@create_function
def string_invert(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('"param" must be a string')



inverted = string_invert('Henrique')
print(inverted)