import sys

iterable = ['Me', 'Have', '__iter__']
iterator = iter(iterable)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# Generator functions that know how to pause
list = [ n for n in range(1000000)]
generator = (n for n in range(1000000))
print(sys.getsizeof(generator))
print(sys.getsizeof(list))

for n in generator:
    print(n)

