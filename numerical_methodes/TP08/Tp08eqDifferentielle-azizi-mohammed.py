import math
import time
# // ==== methode euler :
def euler(f, x0, y0, h, n , derivee_exacte ):
    print("\n========== Méthode d'Euler ==========")
    print(f"{'k':<3} | {'x':>8} | {'y':>12} | {'valeur exacte':>15} | {'erreur':>10}")
    print("-" * 58)
    x = x0
    y = y0
    for k in range(n):
        y = y + h * f(x, y)
        x = x + h
        exact = derivee_exacte(x)
        erreur = abs(exact - y)
        print(f"{k:<3} | {x:>8.4f} | {y:>12.6f} | {exact:>15.6f} | {erreur:>10.8f}")
    return y

def re_euler(f, x0, y0, h, n,derivee_exacte):
    if n == 0:
        return y0
    else:
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        exact = derivee_exacte(x0)
        erreur = abs(exact - y0)
        print(f"x = {x0:.4f} | y = {y0:.8f} | valeur exacte = {exact:.8f} | erreur = {erreur:.8f}")
        return re_euler(f, x0, y0, h, n-1,derivee_exacte)

# // ==== methode taylor :
def taylor(f, DfDx, DfDy, x0, y0, h, n ,derivee_exacte):
    print("\n========== Méthode de Taylor ==========")
    print(f"{'k':<3} | {'x':>8} | {'y':>14} | {'valeur exacte':>15} | {'erreur':>12}")
    print("-" * 64)
    x = x0
    y = y0
    for k in range(n):
        f_val = f(x, y)
        dfdx = DfDx(x, y)
        dfdy = DfDy(x, y)
        y = y + h * f_val + (h**2 / 2) * (dfdx + dfdy * f_val)
        x = x + h
        exact = derivee_exacte(x)
        erreur = abs(exact - y)
        print(f"{k:<3} | {x:>8.4f} | {y:>14.6f} | {exact:>15.6f} | {erreur:>12.6f}")
    return y



def re_taylor(f, DfDx, DfDy, x0, y0, h, n,derivee_exacte):
    if n == 0:
        return y0
    else:
        f_val = f(x0, y0)
        dfdx = DfDx(x0, y0)
        dfdy = DfDy(x0, y0)
        y0 = y0 + h * f_val + (h**2 / 2) * (dfdx + dfdy * f_val)
        x0 = x0 + h
        exact = derivee_exacte(x0)
        erreur = abs(exact - y0)
        print(f"x = {x0:.4f} | y = {y0:.8f} | valeur exacte = {exact:.8f} | erreur = {erreur:.8f}")
        return re_taylor(f, DfDx, DfDy, x0, y0, h, n-1,derivee_exacte)
    
# // ==== methode euler  modifiee:
def euler_modifiee(f, x0, y0, h, n,derivee_exacte):
    print("\n========== Méthode de euler modifie ==========")
    print(f"{'k':<3} | {'x':>8} | {'y':>14} | {'valeur exacte':>15} | {'erreur':>12}")
    for k in range(n):
        xk1 = x0 + h
        d1 = f(x0,y0)
        d2 = f(xk1,y0+h*d1)
        y0 = y0 + h/2*(d1+d2)
        exact = derivee_exacte(x0)
        erreur = abs(exact - y0)
        print(f"{k:<3} | {x0:>8.4f} | {y0:>14.6f} | {exact:>15.6f} | {erreur:>12.6f}")
        x0 = xk1
    return y0
def re_euler_mod(f, x, y, h, n,direvee_exacte):
    if n == 0:
        return y
    d1 = f(x, y)
    d2 = f(x + h, y + h * d1)
    y_next = y + (h / 2) * (d1 + d2)
    x_next = x + h
    exact = derivee_exacte(x)
    erreur = abs(exact - y)
    print(f"|x: {x:>8.4f} |y: {y:>14.6f} |exact: {exact:>15.6f} |erreur: {erreur:>12.6f}")

    return re_euler_mod(f, x_next, y_next, h, n - 1, direvee_exacte)

# // ==== methode  point milieu:
def point_milieu(f, x0, y0, h, n,derivee_exacte):
    print("\n========== Méthode de Point milieu ==========")
    print(f"{'k':<3} | {'x':>8} | {'y':>14} | {'valeur exacte':>15} | {'erreur':>12}")
    for k in range(n):
        xk1 = x0 + h
        d1 = f(x0,y0)
        y0 = y0 + h/2*f(x0+h/2,y0+h/2*d1)
        exact = derivee_exacte(x0)
        erreur = abs(exact - y0)
        print(f"{k:<3} | {x0:>8.4f} | {y0:>14.6f} | {exact:>15.6f} | {erreur:>12.6f}")
        x0 = xk1
    return y0
def re_point_milieu(f, x, y, h, n,direvee_exacte):
    if n == 0:
        return y
    d1 = f(x, y)
    x_mid = x + h / 2
    y_mid = y + (h / 2) * d1
    d2 = f(x_mid, y_mid)
    y_next = y + h * d2
    x_next = x + h
    exact = derivee_exacte(x)
    erreur = abs(exact - y)
    print(f"|x: {x:>8.4f} |y: {y:>14.6f} |exact: {exact:>15.6f} |erreur: {erreur:>12.6f}")

    return re_point_milieu(f, x_next, y_next, h, n - 1, direvee_exacte)
# // ==== methode rung kutta:
def rung_kutta(f, x0, y0, h, n,derivee_exacte):
    print("\n========== Méthode de rung  ==========")
    print(f"{'k':<3} | {'x':>8} | {'y':>14} | {'d1':>6} | {'d2':>6} | {'d3':>6} | {'d4':>6} | {'valeur exacte':>10} | {'erreur':>8}")
    for k in range(n):
        xk1 = x0 + h
        d1 = h*f(x0,y0)
        d2 = h*f(x0 + h/2,y0+d1/2)
        d3 = h*f(x0 + h/2,y0 +  d2/2)
        d4 = h*f(x0 + h,y0 + d3)
        y0 = y0 + (1 / 6) * (d1 + 2 * d2 + 2 * d3 + d4)
        exact = derivee_exacte(x0)
        erreur = abs(exact - y0)
        print(f"{k:<3} | {x0:>8.4f} | {y0:>14.6f} | {d1:>6.4f} | {d2:>6.4f} | {d3:>6.4f} | {d4:>6.4f} | {exact:>10.6f} | {erreur:>8.6f}")
        x0 = xk1
    return y0
def re_runge_kutta(f, x, y, h, n, direvee_exacte):
    if n == 0:
        return y
    d1 = h * f(x, y)
    d2 = h * f(x + h / 2, y + d1 / 2)
    d3 = h * f(x + h / 2, y + d2 / 2)
    d4 = h * f(x + h, y + d3)
    y_next = y + (1 / 6) * (d1 + 2 * d2 + 2 * d3 + d4)
    x_next = x + h
    exact = derivee_exacte(x)
    erreur = abs(exact - y)
    print(f"|x: {x:>8.4f} |y: {y:>14.6f} |d1: {d1:>6.4f} |d2: {d2:>6.4f} |d3: {d3:>6.4f} |d4: {d4:>6.4f} |exact: {exact:>10.6f} |erreur: {erreur:>8.6f}")

    return re_runge_kutta(f, x_next, y_next, h, n - 1, direvee_exacte)






def comparaison_general(f, DfDx, DfDy, derivee_exacte):
    print("\n========== Comparaison Générale ==========")
    methods = {
        "Euler": euler,
        "Euler Réc.":  re_euler,
        "Taylor": taylor,
        "Taylor Réc.":  re_taylor,
        "Euler Mod.":  euler_modifiee,
        "Euler Mod Rec":  re_euler_mod,
        "Pt Milieu":  point_milieu,
        "Pt Milieu Rec":  point_milieu,
        "Runge-Kutta":  rung_kutta,
        "Runge-Kutta rec":  re_runge_kutta,

    }
    print("-" * 70)
    print("-" * 90)
    compare = []
    x0 = float(input("Donner a (x0 ) : "))
    x = float(input("Donner b (x final) : "))
    y0 = float(input(f"Donner f({x0}) = "))
    h = 0.1
    n = abs(x - x0)/h

    for name, method in methods.items():
        
        try :
            h = float(input(f"donner la valeur de h pour la methode de {name}  : "))
        except :
            print("saisie fausee")
            h = float(input(f"donner la valeur de h pour la methode de {name}  : "))

        n = int(abs(x - x0)/h) 
        print(f"n = {n}")
        start = time.perf_counter()
        if "Taylor" in name:
            result = method(f, DfDx, DfDy, x0, y0, h, n, derivee_exacte)
        else:
            result = method(f, x0, y0, h, n, derivee_exacte)
        end = time.perf_counter()
        exact = derivee_exacte(x0 + n * h)
        erreur = abs(result - exact)

        compare.append(f"{name:<15} | {h:<10.4f} | {end - start:<10.6f} | {result:<12.6f} | {exact:<15.6f} | {erreur:<12.6f}")
    print("")
    print("="*40,"Comparaison entre les methodes : ")
    print(f"{'Méthode':<15} | {'h':<10} | {'Temps (s)':<10} | {'Résultat':<12} | {'Valeur exacte':<15} | {'Erreur':<12}")
    print('-'*100)
    for c in compare:
        print(c)

    

def donnee():
    n = int(input("Donner n (nombre d'itérations) : "))
    x0 = float(input("Donner x0 : "))
    x =  float(input("Donner x final : "))
    y0 = float(input("Donner y0 : "))
    h = (x - x0) / n
    return x0, x, y0, n, h
# //== exemple 01 :
def f1(x, y):
    return -y + x + 1
def DfDx1(x, y):
    return 1
def DfDy1(x, y):
    return -1
def exacte1(x):
    return math.exp(-x) + x

# //== exemple 02 :
def f2(x,y):
    return x + y
def DfDx2(x,y):
    return 1
def DfDy2(x,y):
    return 1
def exacte2(x):
    return -x -1 + 2*math.exp(x)

if __name__ == "__main__":
    x0 = 0
    x = 0
    y0 = 0
    n = 0
    h = 0

    print("\n======= Équation Différentielle =======")
    f = f1
    DfDx = DfDx1
    DfDy = DfDy1
    derivee_exacte = exacte1

    choix = 1
    while choix != -1:
        print("choisir l'exemple :")
        aff = """
            1 - f(x,y) = -y + x + 1
            2 - f(x,y) = x + y

            """
        print(aff)
        exemple = input("Saisie l'exemple :")
        if exemple == "1" :
            f = f1
            DfDx = DfDx1
            DfDy = DfDy1
            derivee_exacte = exacte1
        elif exemple == "2" :
            f = f2
            DfDx = DfDx2
            DfDy = DfDy2
            derivee_exacte = exacte2

        else : 
            print("err : choix incorrect")
            continue


            
    
        menu = """
    1 - Euler 
    2 - Euler (récursive)
    3 - Taylor
    4 - Taylor (récursive)
    5 - euler modifie
    6 - euler modifie recursive
    7 - point milieu
    8 - point milieu recursive
    9 - rung KuTTA
    10 - rung KuTTA recursive
    11 - comparaison egeneral
    (-1 pour quitter)
        """
        print(menu)
        choix = int(input("Choisir la méthode : "))
        if choix == -1:
            break
         

        if choix == 1:
            x0, x, y0, n, h = donnee()
            euler(f, x0, y0, h, n,derivee_exacte)
        elif choix == 2:
            print("\n========== Méthode d'Euler Récursive ==========")
            x0, x, y0, n, h = donnee()

            re_euler(f, x0, y0, h, n,derivee_exacte)
        elif choix == 3:
            x0, x, y0, n, h = donnee()
            taylor(f, DfDx, DfDy, x0, y0, h, n,derivee_exacte)
        elif choix == 4:
            print("\n========== Méthode de Taylor Récursive ==========")
            x0, x, y0, n, h = donnee()
            re_taylor(f, DfDx, DfDy, x0, y0, h, n,derivee_exacte)
        elif choix == 5 :
            x0, x, y0, n, h = donnee()
            euler_modifiee(f,x0,y0,h,n,derivee_exacte)
        elif choix == 6 :
            x0, x, y0, n, h = donnee()
            print
            print("\n========== Méthode de Euler Modifie Récursive ==========")
            re_euler_mod(f,x0,y0,h,n,derivee_exacte)
        elif choix == 7 :
            x0, x, y0, n, h = donnee()
            point_milieu(f,x0,y0,h,n,derivee_exacte)
        elif choix == 8 :
            x0, x, y0, n, h = donnee()
            print
            print("\n========== Méthode de Point Milieu Récursive ==========")
            re_point_milieu(f,x0,y0,h,n,derivee_exacte)
        elif choix == 9 :
            print
            x0, x, y0, n, h = donnee()
            rung_kutta(f,x0,y0,h,n,derivee_exacte)
        elif choix == 10 :
            x0, x, y0, n, h = donnee()
            print("\n========== Méthode de Rung Kutta Récursive ==========")
            re_runge_kutta(f,x0,y0,h,n,derivee_exacte)
        elif choix == 11 :
            comparaison_general(f, DfDx, DfDy,derivee_exacte)
        else:
            print("Choix invalide.")
    print("\n====== Fin du programme ======")
