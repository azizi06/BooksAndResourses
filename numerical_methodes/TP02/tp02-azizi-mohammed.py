import math
def Dichotomie(fonction ,a,b,epsilon):
    if fonction(a)*fonction(b) > 0 :
        print("On nr peut pas resoudre cette equation par la methode de Dichotomiee! ")
    c = (a+b)/2
    i = 0
    while(b-a)>epsilon :
        print(f"i : {i} b-a {b-a}  f({c}) == {fonction(c)}")
        c = (a+b)/2
        if fonction(a)*fonction(c) <= 0 :
            b = c
        else : 
            a = c
        i += 1
    print("\n")
    
    return c

def PointFix(g ,x0,epsilon):
    xold = x0
    xnew = 0
    i = 0
    while True :
        xnew = g(xold)
        print(f" i :{i}, Xn : {xold},Xn+1 :{xnew}     ,|Xn+1 - Xn | :{abs(xnew - xold)}      f({xnew}) == {g(xnew)}")
        if abs(xnew - xold) < epsilon :
            print("\n")
            return xnew
        i+=1
        xold = xnew
def Newton(function,derivee ,x0,epsilon):
    xold = x0
    xnew = 0
    i = 0
    while True :
        xnew  = xold - function(xold)/derivee(xold)
        print(f" i :{i}, Xn : {xold},Xn+1 :{xnew}      ,|Xn+1 - Xn | :{abs(xnew - xold)}      f({xnew}) == {function(xnew)}")
        if abs(xnew - xold) < epsilon :
            print("\n")
            return xnew
        xold = xnew
        i +=1
def f1(x):
    return x**3 + 4*x - 2 
def f2(x):
    return  math.exp(x) - 2*x -1
def f3(x) :
    return   x - math.cos(x)
def derivee1(x):
    return 3*x**2 + 4
def g(x) : 
    return (-1*x**3 + 2) / 4
def derivee2(x):
    return math.exp(x) - 2
def main():
    print("Choisissez la methode pour résoudre l'equation : ")
    print("1. Méthode de dichotomie ")
    print("2. Méthode du point  fixe")
    print("3. Méthode de Newton    ")
    choix = int(input("Votre Choix :  "))

    if choix == 1:
        s1 = Dichotomie(f1,0,1,0.00000001)
        print(f"    x**3 + 4*x - 2 = 0  => x= {s1}")
        print("\n")

        s2 = Dichotomie(f2,1,2,0.0001)
        print(f"  math.exp(x) - 2*x -1  => x= {s2}")
        print("\n")

        s3 =Dichotomie(f3,0,1,0.0001) 
        print(f"   x - math.cos(x) = 0  => x= {s3}")
        print("\n")


    elif choix == 2:
        s4 = PointFix(g,0.6,0.00000001)
        print(f"   x**3 + 4*x - 2 = 0  => x= {s4}  f({s4}) = {f1(s4)}")

    elif choix == 3:
        s5 = Newton(f1,derivee1,0.5,0.00000001)
        print(f"   x**3 + 4*x - 2 = 0  => x= {s5}  f({s5}) = {f1(s5)}")
        print("\n")


        s6 = Newton(f2,derivee2,1.5,1e-4)
        print(f"   math.exp(x) - 2*x -1  => x= {s6}  f({s6}) = {f2(s6)}")

    print("Fin")
if __name__ == '__main__' :
    main()
