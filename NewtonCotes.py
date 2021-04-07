import math

def fun(x):
    return x**2

def trapezio(yi, x0, h):
    print("metodo usado: trapezio")
    return (yi[x0]+yi[x0+1])*h/2
    
def SimpTresOito(yi, comeco, espaco):
    print("metodo usado: 3/8")
    return (3*espaco/8)*(yi[comeco]+yi[comeco+1]+yi[comeco+2]+3*yi[comeco+3])
    
def SimpUmTerco(yi, comeco, espaco):
    print("metodo usado: 1/3")
    return (espaco/3)*(yi[comeco]+2*yi[comeco+1]+4*yi[comeco+2])
    
def NewtonCotes():
    n = int(input("o numero de pontos: "))
    xi = []
    yi = []
    for a in range(n):
        var = float(input("insira o xi: "))
        xi.append(var)
        var = float(input("insira o yi: "))
        yi.append(var)
    espaco = xi[1]-xi[0]
    count = 0
    comeco = 0
    res = 0
    enter = 0
    c = 0
    for j in range(n-1):
        if (xi[j+1] - xi[j]) == espaco:
            count += 1
        else:
            enter = 1
        if (c%2 == 0 and c!=0) or enter == 1 :
            if count==1:
                res+= trapezio(yi, comeco, espaco)
            if count==2:
                res+= SimpUmTerco(yi, comeco, espaco)
            if count==3:
                res+= SimpTresOito(yi, comeco, espaco)
            espaco = xi[j+1] - xi[j]
            comeco = j
            c = 0
        enter = 0
        c += 1
    print(res)
NewtonCotes()
