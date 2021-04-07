import math

def fun(x):
    return 1/((1+x**2)*(1-(x**2)/2))

def SimpUmTerco(xn, x0, n):
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
    return soma

def ZeroToInf(x0, n):
    hZi = ((1/x0))/(2*n)
    i = 2
    posiZi = hZi
    res = 0
    while posiZi <= (1/x0):
        if i%2 == 0:
            res += 4*(fun(1/posiZi)*(1/fun(posiZi)**2))
        else:
            res += 2*(fun(1/posiZi)*(1/fun(posiZi)**2))
        i += 1
        posiZi = posiZi+(hZi)
    res += 0.93908226
    res = (res)*(hZi/3)
    return res

def Caller():
    result = 0
    x0 = float(input("Insira o limite inferior: "))
    xn = input("insira o limite superior: ")
    n = 20
    if xn == "inf":
        if x0 == 0:
            result += SimpUmTerco(1, 0, n)
            x0 = 1
        result += ZeroToInf(x0, n)
        
    else:
        xn = float(xn)
        result += SimpUmTerco(xn, x0, n)
    print("resultado:", result)
    
Caller()
