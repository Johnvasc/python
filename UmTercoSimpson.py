import math

def fun(x):
    return x**2

def SimpUmTerco():
    x0 = float(input("Insira o limite inferior: "))
    xn = float(input("insira o limite superior: "))
    n = float(input("o numero de pontos: "))
    h = (xn-x0)/(2*n)
    i = 2
    posi = x0+h
    soma = 0
    while posi <= xn-h:
        if i%2 == 0:
            soma += 4*fun(posi)
        else:
            soma += 2*fun(posi)
        i += 1
        posi = posi+(h)
    soma += fun(x0)+fun(xn)
    soma = (soma)*(h/3)
    print("O valor eh: ", soma)
    
SimpUmTerco()
