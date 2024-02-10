def execute(function, *args):
    return function(*args)


print(
    execute(
        lambda x, y: x + y,
        2, 3
    )
)

def sum(x, y):
    return x + y

def create_multiplyer(multiplyer):
    def multiply(number):
        return multiplyer * number
    return multiply



duplicate = execute(
        lambda multiplyer: lambda number: multiplyer * number,
        2
    )

print(duplicate(4))

