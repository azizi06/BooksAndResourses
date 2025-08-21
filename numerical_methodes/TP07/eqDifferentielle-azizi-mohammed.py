import math

def euler(f, x0, y0, h, n):
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
        print(f"{k:<3} | {x:>8.4f} | {y:>12.8f} | {exact:>15.8f} | {erreur:>10.8f}")

def taylor(f, DfDx, DfDy, x0, y0, h, n):
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
        print(f"{k:<3} | {x:>8.4f} | {y:>14.8f} | {exact:>15.8f} | {erreur:>12.8f}")
    return y

def re_euler(f, x0, y0, h, n):
    if n == 0:
        return y0
    else:
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        exact = derivee_exacte(x0)
        erreur = abs(exact - y0)
        print(f"x = {x0:.4f} | y = {y0:.8f} | valeur exacte = {exact:.8f} | erreur = {erreur:.8f}")
        return re_euler(f, x0, y0, h, n-1)

def re_taylor(f, DfDx, DfDy, x0, y0, h, n):
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
        return re_taylor(f, DfDx, DfDy, x0, y0, h, n-1)

def donnee():
    n = int(input("Donner n (nombre d'itérations) : "))
    x0 = float(input("Donner x0 : "))
    x = float(input("Donner x final : "))
    y0 = float(input(f"Donner f({x0}) = "))
    h = (x - x0) / n
    return x0, x, y0, n, h

def f(x, y):
    return -y + x + 1

def DfDx(x, y):
    return 1

def DfDy(x, y):
    return -1

def derivee_exacte(x):
    return math.exp(-x) + x

if __name__ == "__main__":
    print("\n======= Équation Différentielle =======")
    choix = 1
    while choix != -1:
        print("\nL'équation utilisée est : f(x, y) = -y + x + 1")
        menu = """
    1 - Euler 
    2 - Euler (récursive)
    3 - Taylor
    4 - Taylor (récursive)
    (-1 pour quitter)
        """
        print(menu)
        choix = int(input("Choisir la méthode : "))
        if choix == -1:
            break
        x0, x, y0, n, h = donnee()

        if choix == 1:
            euler(f, x0, y0, h, n)
        elif choix == 2:
            print("\n========== Méthode d'Euler Récursive ==========")
            re_euler(f, x0, y0, h, n)
        elif choix == 3:
            taylor(f, DfDx, DfDy, x0, y0, h, n)
        elif choix == 4:
            print("\n========== Méthode de Taylor Récursive ==========")
            re_taylor(f, DfDx, DfDy, x0, y0, h, n)
        else:
            print("Choix invalide.")
    print("\n====== Fin du programme ======")
