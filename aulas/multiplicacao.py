def create_multiplicator(multiplicator):
    def multiply(number):
        return multiplicator * number
    return multiply


duplicate = create_multiplicator(2)
triplicate = create_multiplicator(3)
quadruplicate = create_multiplicator(4)

print(duplicate(8))
print(triplicate(8))
print(quadruplicate(8))