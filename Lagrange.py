''' Inspiração: canal para tudo tem um código '''
def Lagrange():
    v = float(input("insira o y a achar\n"))
    pts = int(input("insira a quantidade de pontos\n"))
    x, y = [], []
    for i in range(pts):
        var = float(input("insira o x \n"))
        x.append(var)
        var = float(input("insira o y relativo ao x\n"))
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
    print("o resultado da interpolacao: ", resul);
Lagrange()
