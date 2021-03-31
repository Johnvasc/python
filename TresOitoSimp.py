 import math

def fun(x):
    return 4/(1+x**2)

def SimpTresOito():
    x0 = float(input("Insira o limite inferior: "))
    xn = float(input("insira o limite superior: "))
    n = float(input("o numero de pontos: "))
    h = (xn-x0)/(3*n)
    i = 1
    posi = x0+h
    soma = 0
    while posi <= xn:
        if i%3 == 0:
            soma += 2*fun(posi)
        else:
            soma += 3*fun(posi)
        i += 1
        posi = posi+(h)
    soma += fun(x0)
    soma = (soma)*(3*h/8)
    print("O valor eh: ", soma)
    
SimpTresOito()
