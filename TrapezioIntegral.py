import math

def fun(x):
    return x**2

def trapezio():
    x0 = float(input("Insira o limite inferior: "))
    xn = float(input("insira o limite superior: "))
    h = float(input("insira a distancia entre os pontos: "))
    result = 0
    intervalo = x0 + h
    interinf = fun(x0)
    intersup = fun(x0 + h)
    while intervalo < xn:
        result += (interinf+intersup)*h/2
        interinf = intersup
        intervalo += h
        intersup = fun(intervalo)
    print("O valor eh: ", result)
    
trapezio()
