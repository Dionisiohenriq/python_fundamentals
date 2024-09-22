import sys
sys.setrecursionlimit(1004)

def recursiva(inicio=0, fim=4):

    if inicio >= fim:
        return fim
    
    print(inicio, fim)
    
    inicio +=1
    return recursiva(inicio, fim)


print(recursiva(0, 1000))


def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n-1)

print(fatorial(1000))
