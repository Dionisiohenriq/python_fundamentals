# count é um iterador sem fim
from itertools import accumulate
from itertools import count

c1 = count(10, 8)
r1 = range(10, 100, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print()
print('count')
for i in c1:
    if i > 100:
        break

    print(i)

print()
print('range')
for i in range(next(c1), 100):
    print(i)


def breaking_records(scores):
    minbreak = accumulate(scores, min)
    maxbreak = accumulate(scores, max)

    return ((len(set(maxbreak))-1), len(set(minbreak))-1)
