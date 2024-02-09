def create_multiplicator(multiplicator):
    def multiply(number):
        return multiplicator * number
    return multiply


duplicate = create_multiplicator(2)

print(duplicate(8))