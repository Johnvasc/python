import math

def trapezio(xs, resps, pts):
    result = 0
    j = 2
    h = (xs[pts - 1] - xs[0])/(pts-1)
    intervalo = xs[0] + h
    interinf = resps[0]
    intersup = resps[1]
    while intervalo <= xs[pts-1]:
        result += (interinf+intersup)*h/2
        interinf = intersup
        intervalo += h
        if(j<pts):
            intersup = resps[j]
        j += 1
    print("O valor parcial: ", result)
    return result
def caller():
    controle = 1
    while 1 == 1:
        pts = int(input("insira o numero de pontos: "))
        xs = []
        resps = []
        res = 0
        for i in range(pts):
            v = float(input("Insira o x: "))
            xs.append(v)
            v = float(input("Insira o valor retornado por x na funcao: "))
            resps.append(v)
        res = res + trapezio(xs, resps, pts)
        controle = int(input("continuar?1 - Sim 0 - Nao "))
        if controle == 0:
            break
    print("O resultado eh: ", res)
caller()
