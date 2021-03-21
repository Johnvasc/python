'''= [] + '''

def interpolNewton():
    v = float(input("Insira o valor a estimar: "))
    pts = int(input("Insira o numero de pontos\n"))
    x, y = [],[]
    difdiv = []
    for i in range(pts):
        var = float(input('insira o x: '))
        x.append(var)
        var = float(input('insira o y relativo ao x: '))
        y.append(var)
    difdiv.append(y)
    var = 1
    for n in range(pts-1):
        d = []
        for n2 in range(len(difdiv[n])-1):
            resul = ((difdiv[n][n2+1]-difdiv[n][n2])/(x[n2+var]-x[n2]))
            d.append(resul)
        difdiv.append(d)
        var += 1
    app = 0
    grau = 0
    res = 0
    for n3 in range(pts):
        ok = difdiv[n3][0]
        for n4 in range(grau):
            ok *= (v - x[n4])
        grau += 1
        res += ok
    print("Aproximacao encontrada: ", res)
interpolNewton()
