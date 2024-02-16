def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')

def gen2(gen):
    print("COMEÇOU GEN2")
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')

def gen3():
    print("COMEÇOU GEN3")
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')

g1 = gen2(gen1)
g2 = gen2(gen3)

for number in g1:
    print(number)

for number in g2:
    print(number)