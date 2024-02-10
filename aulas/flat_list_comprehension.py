numbers = [[number, number ** 2] for number in range(10)]
flat = [y for x in numbers for y in x]

print(numbers)
print(flat)