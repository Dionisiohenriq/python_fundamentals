# Exercices with functions

# Create a function that multiplies all not named arguments receiveds
# Return the total to a variable and show the value of the variable

# Create a function that tells if a number is odd or even
# Return the result

def multiplying(*args):
    total = 1
    for x in args:
        total *= x

    return total

result = multiplying(1,2,3,4,5,6)
print(result)
print(1*2*3*4*5*6)

def odd_or_even(number):
    if number % 2 == 0:
        return f'{number} is odd'
    
    return f'{number} is even'

print(odd_or_even(2))