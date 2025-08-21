import os
banner = """
\033[96m 
███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██╗   ██╗██████╗     ██████╗ ███████╗       
██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██║   ██║██╔══██╗    ██╔══██╗██╔════╝       
███████╗██║   ██║██║    ██║   ██║█████╗  ██║   ██║██████╔╝    ██║  ██║█████╗         
╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██║   ██║██╔══██╗    ██║  ██║██╔══╝         
███████║╚██████╔╝███████╗╚████╔╝ ███████╗╚██████╔╝██║  ██║    ██████╔╝███████╗       
╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝       
                                                                                     
███████╗██╗   ██╗███████╗████████╗███╗   ███╗███████╗                                
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝████╗ ████║██╔════╝                                
███████╗ ╚████╔╝ ███████╗   ██║   ██╔████╔██║█████╗                                  
╚════██║  ╚██╔╝  ╚════██║   ██║   ██║╚██╔╝██║██╔══╝                                  
███████║   ██║   ███████║   ██║   ██║ ╚═╝ ██║███████╗                                
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝     ╚═╝╚══════╝                                
                                                                                     
                    ███████╗ ██████╗ ██╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
                    ██╔════╝██╔═══██╗██║   ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
                    █████╗  ██║   ██║██║   ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
                    ██╔══╝  ██║▄▄ ██║██║   ██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
                    ███████╗╚██████╔╝╚██████╔╝██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
                    ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                     
██╗     ██╗███╗   ██╗ █████╗ ██╗██████╗ ███████╗                                     
██║     ██║████╗  ██║██╔══██╗██║██╔══██╗██╔════╝                                     
██║     ██║██╔██╗ ██║███████║██║██████╔╝█████╗                                       
██║     ██║██║╚██╗██║██╔══██║██║██╔══██╗██╔══╝                                       
███████╗██║██║ ╚████║██║  ██║██║██║  ██║███████╗                                     
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝                                     
\033[0m
\n\n\n
"""


def aff_solution(X : list):
    if len(X) == 0:
        print("pas de solution")
    print("--la solution est : ")
    for i in range(0,len(X)):
        print(f"X{i} : {X[i]}")

def Jacobi(A: list[list[float]], B: list[float], VectInitial: list[float], stop: int) -> list[float]:
    n = len(A)
    X = [[0 for _ in range(n)] for _ in range(stop + 1)]
    X[0] = VectInitial
    for i in range(n):
        if A[i][i] == 0:
            raise ValueError(f"Diagonal element A[{i}][{i}] cannot be zero.")
    for k in range(stop):
        for i in range(n):
            X[k + 1][i] = round(1 / A[i][i], 3) * (B[i] - sum(A[i][j] * X[k][j] for j in range(n) if j != i))
    return X[-1]
def GaussSeidel(A: list[list[float]], B: list[float], VectInitial: list[float], stop: int) -> list[float]:
    n = len(A)
    X = VectInitial[:]
    
    for k in range(0,stop):
        X_old = X[:]
        for i in range(n):
            sum_avant = sum(A[i][j] * X[j] for j in range(i))
            sum_apres = sum(A[i][j] * X_old[j] for j in range(i + 1, n))
            X[i] = (B[i] - sum_avant - sum_apres) / A[i][i]
        
        diff = max(abs(X[i] - X_old[i]) for i in range(n))
    return X


def triangulization(A : list,B : list)-> tuple[list[list],list] :
    n = len(B)
    print("---------------------  Triangulization --------------------")
    for k in range(0,n):
        #aff_systeme(A,B)
        pivot = A[k][k]
        if pivot != 0 :
            for i in range(k+1,n):
                q = A[i][k] 
                A[i][k] = 0
                B[i] = B[i] - (q/pivot) * B[k]
                for j in range(k+1,n):
                    A[i][j] = A[i][j] - A[k][j] * (q/pivot)
        else :
            raise Exception("Le Pivot est Null : Choisire une autre method")
    return A,B

def EliminationGaussPivotNonNull(A : list,B : list):
    _A,_B = triangulization(A.copy(),B.copy())
    return remonte(_A,_B)
def triangulizationPivotPartiel(A : list,B : list)-> tuple[list[list],list] :
    print("---------------------  Triangulization  Pivot Partiel --------------------")
    n = len(A)
    for k in range(0,n) :
        #aff_systeme(A,B)
        pivot = A[k][k]
        l = k
        for i in range(k,n):
            if abs(A[i][k]) > pivot :
                pivot = A[i][k]
                l = i
        if l != k :
            tmpB = B[k]
            B[k] = B[l]
            B[l] = tmpB
            for j in range(k,n) :
                temp = A[k][j]
                A[k][j] = A[l][j]
                A[l][j] = temp
        for i in range(k+1,n):
            q = A[i][k]
            A[i][k] = 0
            B[i] = B[i] - B[k]*(q/pivot)
            for j in range(k+1,n) :
                A[i][j] = A[i][j] - A[k][j]*(q/pivot)
    return A,B
    

def EliminationGaussPivotPartiel(A : list,B : list):
    _A,_B = triangulizationPivotPartiel(A.copy(),B.copy())
    aff_systeme(_A,_B)
    return remonte(_A,_B)
def triangulizationPivotTotal(A : list,B : list)-> tuple[list[list],list] :
    print("---------------------  Triangulization  Pivot Total--------------------")
    n : int = len(A)
    for k in range(0,n-1):
        #aff_systeme(A,B)
        #pivot = (max(abs(A[i][j]) for j in range(k,n) for i in range(k,n)))
        pivot = A[k][k]
        col = k
        row = k
        for i in range(k,n):
            for j in range(k,n):
                if abs(pivot) < abs(A[i][j]) :
                    pivot = A[i][j]
                    row = i
                    col = j

        print(f"Pivot : {pivot} row : {row} col:{col}\n")
        if row != k :
            tmpB = B[k]
            B[k] = B[row]
            B[row] = tmpB
            for j in range(k,n) :
                temp = A[k][j]
                A[k][j] = A[row][j]
                A[row][j] = temp
        aff_systeme(A,B)
        
        if col != k :
            for i in range(k,n) :
                temp = A[i][k]
                A[i][k] = A[i][col]
                A[i][col] = temp
        aff_systeme(A,B)
        for i in range(k+1,n):
            aff_systeme(A,B)
            c = round(A[i][k]/pivot,3)
            B[i] = B[i] - c*B[k]
            A[i][k] = 0
            for j in range(k+1,n):
                A[i][j] = A[i][j] - c*A[k][j] 
    return A,B

        
    
def EliminationGaussPivotTotal(A : list,B : list):
    _A,_B = triangulizationPivotTotal(A.copy(),B.copy())
    aff_systeme(_A,_B)
    return remonte(_A,_B)
    
def matriceIdentite(n : int)->list[list] :
    I = []
    for i in range(0,n):
        l = []
        for j in range(0,n):
            if i == j :
                l.append(1)
            else :
                l.append(0)
        I.append(l)
    return I

def DecomposotionLU(A : list,B : list):
    n = len(A)
    U = A.copy()
    L = matriceIdentite(n)
    for k in range(0,n) :
        pivot = A[k][k]
        for i in range(k+1,n):
            q = U[i][k]
            U[i][k] = 0
            L[i][k] = round((pivot/q),3)
            for j in range(k+1,n):
                U[i][j] = U[i][j] - U[k][j]*round((pivot/q),3)
    return U,L

def SolveDecomposotionLU(A : list,B : list):
    U,L = DecomposotionLU(A,B.copy())
    Y = descente(L,B)
    return remonte(U,Y)
def lire_systeme()->tuple[list[list],list]:
    A = []
    taille =  int(input("Donner la taille de la matrice A : "))
    print("Donner les valeurs De la matrice A : x  x  x")
    for i in range(0,taille):
        line = []
        valeurs = input(f"Donner les valeeurs de la ligne {i} :").split(" ")
        if len(valeurs) != taille :
            i = i-1
            print("Le nombre des valeurs inccorect")
            continue
            
        for j in range(0,taille) :
            line.append(int(valeurs[j]))
        A.append(line)
    B = []
    print("Donner les valeurs De la matrice B : x")
    for i in range(0,taille):
        b = int(input(f"Donner la valeur de B[{i}] : "))
        B.append(b)
    return A,B
def aff_systeme2(A : list[list],b : list):
    for i in range(0,len(A)) :
        for j in range(0,len(A[0])) : print(A[i][j],end="  ")
        print(" |",end=" ")
        print(b[i])
def aff_systeme(A: list[list], b: list):
    print()
    max_width = 5 #max(max(len(str(num)) for row in A for num in row), max(len(str(num)) for num in b))
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f"{A[i][j]:>{max_width}}", end="  ")
        print(" |", end=" ")
        print(f"{b[i]:>{max_width}}")

def descente(A : list[list],B :list)->list:
    print("-----------------------  Descente  ------------------------")
    if len(A) != len(B) or len(A[0]) != len(A):
        raise Exception("Probleme Dans La taille de la matrice A ou matice B")
    #Exception La matrice A n'est pas triangulaire inferiure
    X = []
    X.append(B[0]/A[0][0]) 
    for i in range(1,len(B)):
        #aff_systeme(A,B)
        sum = 0
        for j in range(i-1,-1,-1):
            sum += A[i][j]*X[j]
        X.append((B[i] - sum)/A[i][i])
    return X
def remonte(A : list[list],B : list):
    print("-----------------------  Remontee  ------------------------")
    if len(A) != len(B) or len(A[0]) != len(A):
        raise Exception("Probleme Dans La taille de la matrice A ou matice B")
    
    n= len(B) 
    X = [0]*n
    X[n-1] = round(B[n-1]/(A[n-1][n-1]),3) 

    for i in range(n-2,-1,-1):
        #aff_systeme(A,B)
        sum = 0
        for j in range(i+1,n):
            sum += A[i][j]*X[j]
            #print(f"i {i} j {j}")
        X[i] = round((B[i] - sum)/A[i][i],3)
    return X
def remonte2(A, b):
    n = len(b)
    x = [0] * n  
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]  
    for i in range(n - 2, -1, -1):
        somme = 0
        for j in range(i + 1, n):
            somme += A[i][j] * x[j]
        x[i] = (b[i] - somme) / A[i][i]
    return x
    

    
def main():
    print(banner)

    a1 = [
        [-2,2,4],
        [-1,4,4],
        [4,1,3]
    ]
    b1 = [4,-1,0]
    a2 = [
        [1,2,3],
        [1,1,2],
        [1,1,1],
    ]
    b2 =[2,0,1]
    a3 = [
        [4,1,-1],
        [2,7,1],
        [1,-3,12],
    ]
    b3 = [3,19,31]
    A = a3
    B = b3
    while True:
        print("--------------------Menu---------------------")
        print("1 - Lire marrice  ")
        print("2 - Affiche matrice")
        print("3 - Methodes Direct")
        print("4 - Methodes Iteratives")
        print("0 - Quitter")
        choix = int(input("Donner Voter Choix :  "))
        if choix == 1 :
            A,B = lire_systeme()
            print("Le systeme est enregister.")
        elif choix == 2 :
            aff_systeme(A,B)
        elif choix == 3 :
            
            print("3.1 1 - Elimination de gauss avec pivot != 0")
            print("3.2 2 - Elimination de gauss avec pivot partiel")
            print("3.3 3 - Elimination de gauss avec pivot total")
            print("3.4 4 - Factorisation LU")
            choix = float(input("Donner Voter Choix :  "))
            print("Choisir Le Type De La methode")
            print("A - methode iterative")
            print("B - methode recursive")
            t = input("Choisir Le type de la methode : ")

            if (choix == 1) and  t == 'A' :
                print("-- Elimination Gauss Pivot Non Null --")
                X = EliminationGaussPivotNonNull(A,B)
                aff_solution(X)
            elif (choix == 2) and  t == 'A' :
                X = EliminationGaussPivotPartiel(A,B)
                aff_solution(X)
            elif (choix == 3) and  t == 'A' :
                X = EliminationGaussPivotTotal(A,B)
                aff_solution(X)
            elif (choix == 4) and  t == 'A' :
                X = SolveDecomposotionLU(A,B)
                aff_solution(X)
        elif choix == 4 :
            print("4.1 1 - Jacobi")
            print("4.2 2  Gauss‐Seidel")
            choix = float(input("Donner Voter Choix :  "))
            print("Choisir Le Type De La methode")
            print("A - methode iterative")
            print("B - methode recursive")
            t = input("Choisir Le type de la methode : ")
            if (choix == 1) and  t == 'A' :
                print("------------------------- JACOBI -----------------------\n")
                V = []
                stop = int(input("Donner Le Nombre D'eterations"))
                valeurs = input(f"Donner les valeeurs du vecteur initiall ( X  X  X) :").split(" ")
                for j in range(0,len(A)) :
                    V.append(int(valeurs[j]))
                X = Jacobi(A.copy(),B.copy(),stop=stop,VectInitial=V)
                aff_solution(X)
            if (choix == 2) and  t == 'A' :
                print("------------------------- GaussSeidel  -----------------------\n")
                V = []
                stop = int(input("Donner Le Nombre D'eterations"))
                valeurs = input(f"Donner les valeeurs du vecteur initiall ( X  X  X) :").split(" ")
                for j in range(0,len(A)) :
                    V.append(int(valeurs[j]))
                X = GaussSeidel(A.copy(),B.copy(),stop=stop,VectInitial=V)
                aff_solution(X)

        elif choix == 0 :
            break
        else : 
            print("Choix incorrect")
       
    print("Fin")

    


if __name__ == "__main__" :
    main()