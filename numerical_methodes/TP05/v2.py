import os
import SystemsEquationLinear as sel

def aff_points(points: list[tuple]):
    print("--")
    n = len(points)
    for i in range(n):
        print(f"x : {points[i][0]}, y = {points[i][1]}")

def aff_solution(x: float, y: float):
    print(f"\033[96m F({x}) = {y} \033[0m \n")

def aff_matrice(m: list[list]):
    n = len(m)
    for i in range(n):
        print(m[i])

def lire_points() -> list[tuple]:
    n = int(input("Donner Le nomber des points :  "))
    points: list[tuple] = []
    for i in range(n):
        s = input(f"point n{i} :  ").split(" ")
        t = (float(s[0]), float(s[1]))
        points.append(t)
    return points

def lagrange(points: list[tuple[float, float]], x: float):
    n = len(points) + 1 
    for i in range(n):
        if x == points[i][0]:
            p = points[i][1]
            return p
    D: list = []
    for i in range(n):
        d = 1
        for j in range(n):
            if i != j:
                d = d * (points[i][0] - points[j][0])
        D.append(d)
    num = 1
    for i in range(n):
        num = num * (x - points[i][0])
    p = 0
    for i in range(n):
        q = num / (x - points[i][0])
        p = p + points[i][1] * q / D[i]
    print("------les bases de lagrange ----------")
    aff_matrice(D)
    print("----------------")
    return p

def difference_divisee(points, i, j):
    if i == j:
        return points[i][1]
    else:
        return (difference_divisee(points, i + 1, j) - difference_divisee(points, i, j - 1)) / (points[j][0] - points[i][0])

def newton_recursive(x, points) -> float:
    n = len(points)
    p = points[0][1]
    termes_produits = 1
    for i in range(1, n):
        termes_produits *= (x - points[i - 1][0])
        p += termes_produits * difference_divisee(points, 0, i)
    return p

def newton_matrice(points: list[tuple[float, float]]) -> list[float]:
    n = len(points)
    D = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        D[i][0] = points[i][1]
    for j in range(1, n):
        for i in range(j, n):
            D[i][j] = (D[i][j - 1] - D[i - 1][j - 1]) / (points[i][0] - points[i - j][0])
    f: list[float] = []
    for i in range(n):
        f.append(D[i][i])
    print("\t ---- matrice de newton ----")
    aff_matrice(D)
    print("------------------------------")
    return f

def newton_valeur(x: float, points: list[tuple[float, float]], f: list[float]) -> float:
    n = len(f)
    p = f[-1]
    aff_points(points=points)
    for i in range(n - 2, -1, -1):
        p = p * (x - points[i][0]) + f[i]
    return p

def newton(x: float, points: list[tuple[float, float]]) -> float:
    f: list[float] = newton_matrice(points)
    y = newton_valeur(x=x, points=points, f=f)
    return y, f

def nouveu_f(points: list[tuple[float, float]], nouveau_point: tuple[float, float], f: list[float]) -> list[float]:
    points.append(nouveau_point)
    n = len(points)
    xn, yn = nouveau_point
    dn = yn
    for i in range(n - 1):
        dn = (dn - f[i]) / (xn - points[i][0])
    f.append(dn)
    return f, points

def ajouter_point(points, f):
    while True:
        choix = input("Voulez vous ajouter une nouvelle point (o, n)?")
        if choix == 'o' or choix == 'O':
            s = input(f"nouveau point  :  ").split(" ")
            nouveau_point = (float(s[0]), float(s[1]))
            f, points = nouveu_f(points=points, nouveau_point=nouveau_point, f=f)
            aff_points(points=points)
            x = float(input("Donner La valeur de X :  "))
            y = newton_valeur(x=x, points=points, f=f)
            aff_solution(x=x, y=y)
        elif choix == 'n':
            return f

def vdet(m: list[list]) -> float:
    d = 1
    n = len(m)
    for i in range(n):
        for j in range(i):
            d *= (m[i][j] - m[i][j])
    return d

def puissance(t: float, n: int) -> float:
    if n < 0:
        return
    r = 1
    for i in range(n):
        r *= t
    return r

def vandermonde_polynomme(t: float, order: int) -> list:
    l = []
    for i in range(order + 1):
        l.append(puissance(t, i))
    return l

def vandermonde_matrix(points: list[tuple[float, float]]):
    n = len(points)
    vmatrice = []
    for i in range(n):
        vmatrice.append(vandermonde_polynomme(points[i][0], n - 1))
    return vmatrice

def calculer_px(x: float, coef: list[float]):
    s = 0
    for i in range(len(coef)):
        s += puissance(x,i) * coef[i]
    return s

def systeme_linear(x: float, points: list[tuple[float, float]]):
    n = len(points)
    vmatrice = vandermonde_matrix(points)
    fx = [i[1] for i in points]
    coef = sel.EliminationGaussPivotNonNull(vmatrice, fx)
    print(" ----------  les  coeffesion ---------------")
    aff_matrice(coef)
    print("-----------------------------")
    return calculer_px(x=x, coef=coef)

def main():
    p1 = [(1, 1), (4, 2), (9, 3), (16, 4)]
    p2 = [(-2, -27), (0, -1), (1, 0)]
    p3 = [(-2, -14), (-1, -11 / 4), (2, -8), (4, -29)]
    points = p3

    x = 7
    os.system("cls")
    while True:
        print("------------     I   NTERPOLATION POLYNOMIALE       -------------------")
        print("1 - lire les points d'apuits")
        print("2 - appficher les points appuits")
        print("3 - Interpolation Lagrange")
        print("4 - Interpolation Newton")
        print("5 - Systeme linear")
        print("6 - Quitter")
        choix = int(input("Donner Voter Choix  "))
        if choix == 1:
            points = lire_points()
        elif choix == 2:
            aff_points(points)
        elif choix == 3:
            x = float(input("Donner La valeur de X : "))
            y = lagrange(x=x, points=points)
            aff_solution(x=x, y=y)
        elif choix == 4:
            print("a - methode iterative ")
            print("b - methode recursive  ")
            choix2 = input("Donner voter methode preferer  ")
            if choix2 == 'a':
                x = float(input("Donner La valeur de X :  "))
                y, f = newton(x=x, points=points)
                aff_solution(x=x, y=y)
                f = ajouter_point(points=points, f=f)
            elif choix2 == 'b':
                x = float(input("Donner La valeur de X :  "))
                y = newton_recursive(x=x, points=points)
                aff_solution(x=x, y=y)
        elif choix == 5:
            x = float(input("Donner La valeur de X :  "))
            y = systeme_linear(x=x, points=points)
            aff_solution(x=x, y=y)
        elif choix == 6:
            break
    print("Fin")

if __name__ == "__main__":
    main()