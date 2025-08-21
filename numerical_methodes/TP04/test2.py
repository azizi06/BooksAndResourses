def newton_matrice(points: list[tuple[float, float]]) -> list[float]:
    n = len(points)
    D = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        D[i][0] = points[i][1]  # Stocker les valeurs y des points dans la première colonne
    for j in range(1, n):
        for i in range(j, n):
            D[i][j] = (D[i][j - 1] - D[i - 1][j - 1]) / (points[i][0] - points[i - j][0])
    f: list[float] = []
    for i in range(n):
        f.append(D[i][i])
    print(D)
    return f

def newton_valeur(x: float, points: list[tuple[float, float]], f: list[float]) -> float:
    n = len(f)
    p = f[-1]
    for i in range(n - 2, -1, -1):
        p = p * (x - points[i][0]) + f[i]
    return p

def newton(x: float, points: list[tuple[float, float]]) -> float:
    f: list[float] = newton_matrice(points)
    y = newton_valeur(x=x, points=points, f=f)
    return y

def ajouter_point(points: list[tuple[float, float]], nouveau_point: tuple[float, float], f: list[float]) -> list[float]:
    points.append(nouveau_point)
    n = len(points)
    xn, yn = nouveau_point

    # Recalculer les différences divisées pour le nouveau point
    new_coeff = yn
    for i in range(n - 1):
        new_coeff = (new_coeff - f[i]) / (xn - points[i][0])
    f.append(new_coeff)
    
    return f

# Exemple d'utilisation
points = [(1, 1), (2, 4), (3, 9), (4, 16)]
x = 2.5
f = newton_matrice(points)
y = newton_valeur(x, points, f)
print("Valeur interpolée pour x =", x, "est", y)

# Ajout d'un nouveau point
nouveau_point = (5, 25)
f = ajouter_point(points, nouveau_point, f)
x = 2.5
y = newton_valeur(x, points, f)
print("Valeur interpolée après ajout du point pour x =", x, "est", y)
