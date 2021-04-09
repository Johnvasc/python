import numpy as np
import math


def newtoncotes(xi, yi, pts):
    kk = np.linspace(0, pts-1, pts)
    nint = 0
    integral = 0
    h = 0
    hant = xi[1]-xi[0]
    for k in kk:
        k = int(k)
        if k < pts-1:
            h = xi[k+1]-xi[k]
            if h==hant or (abs(h-hant)<1e-5):
                nint += 1
            else:
                if nint == 1:
                    print("trapezio")
                    integral += (hant/2)*(yi[k]+yi[k-1])
                    hant = h
                    nint = 1
                if nint == 2:
                    print("1/3 Simspson")
                    integral += (hant/3)*(4*yi[k-2]+2*yi[k-1]+yi[k])
                    hant = h
                    nint = 1
                if nint == 3:
                    print("3/8 Simspson")
                    integral += (3*hant/8)*(yi[k-3]+3*yi[k-2]+3*yi[k-1]+yi[k])
                    hant = h
                    nint = 1
        else:
            if nint == 1:
                print("trapezio")
                integral += (hant/2)*(yi[k]+yi[k-1])
                hant = h
                nint = 1
            if nint == 2:
                print("1/3 Simspson")
                integral += (hant/3)*(4*yi[k-2]+2*yi[k-1]+yi[k])
                hant = h
                nint = 1
            if nint == 3:
                print("3/8 Simspson")
                integral += (3*hant/8)*(yi[k-3]+3*yi[k-2]+3*yi[k-1]+yi[k])
                hant = h
                nint = 1
                
    return integral
def met():
    xi = []
    yi = []
    pts = int(input("insira o numero de pontos: "))
    for i in range(pts):
        var = float(input("insira o valor de xi: "))
        xi.append(var)
        var = float(input("insira o valor de yi equivalente: "))
        yi.append(var)
    result = newtoncotes(xi, yi, pts)
    print(result)
    
met()
