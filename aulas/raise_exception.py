def nao_aceita_zero(d):
    if(d == 0):
        raise ZeroDivisionError('Você está tentando dividir por 0!')

def tem_que_ser_numero(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'"{n}" deve ser int ou float '
            f'"{tipo_n.__name__}" enviado.'
        )

def soma(a, b):
    tem_que_ser_numero(a)
    tem_que_ser_numero(b)
    nao_aceita_zero(b)
    return a + b
    
print(soma(1, 0))

