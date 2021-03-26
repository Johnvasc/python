import numpy as np
def Lagrange():
    v = np.poly1d([1,0])
    pts = int(input("insira o numero de pontos: "))
    x, y = [], []
    for i in range(pts):
        var = float(input("insira o x: "))
        x.append(var)
        var = float(input("insira o y relativo ao x: "))
        y.append(var)
    coefs = []
    for n in range(pts):
        resul = 1
        for j in range(pts):
            if n!=j:
                resul *= ((v-x[j])/(x[n]-x[j]))
        coefs.append(resul)
    resul = 0
    for n2 in range(pts):
        resul = resul + y[n2]*coefs[n2]
    print("o resultado da interpolacao:\n", resul);
Lagrange()
