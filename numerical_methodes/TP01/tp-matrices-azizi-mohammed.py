def lire_matrice_carre() -> list[list] :
    taille : int =  int(input("donner la taille du matrice : "))
    matrice : list[list] = []
    for i in range(taille) :
        row : list= []
        print()
        for j in range(taille) :
            a = int(input(f"Donner La valeur a({i},{j}) : " ))
            row.append(a)
        matrice.append(row)
    return matrice

def affiche_matrice(matrix : list[list]):
    for i in range(len(matrix)) :
        print()
        for j in range(len(matrix[i])) :
            print(f" {matrix[i][j]}",end=" ")
        {}

def afficher_matrice_identite():
    order =  int(input("donner l order de la matrice d identite"))
    for i in range(order):
        print()
        for j in range(order):
            if i == j :
                print("1",end=" ")
            else  :
                print("0",end=" ")            
def  produit_matrice_par_scalaire (num: int ,order : int):
    matrice = []
    for i in range(order):
        line =[]
        for j in range(order):
            if i == j :
                line.append(num)
            else  :
                line.append(0)
        matrice.append(line)
    return matrice

  
def somme_matrice(matrix1 : list[list],matrix2 : list[list]) -> list[list]:
    matrix1_rows : int = len(matrix1)
    matrix1_cols : int = len(matrix1[0])

    matrix2_rows : int = len(matrix1)
    matrix2_cols : int = len(matrix2[0])

    if(matrix1_rows != matrix2_rows or matrix1_cols != matrix2_cols) :
        raise Exception("Diffrent Taille de Matrices")
        exit()      
    somme : list[list] = []
    for i in range(matrix1_rows) :
        row : list = []
        for j in range(matrix1_cols) :
            element =  matrix1[i][j] + matrix2[i][j]
            row.append(element)
        somme.append(row)
    return somme

def produit_deux_vecteures(matrix1 : list[list],row : int,matrix2 : list[list],col : int) -> int :
    sum  = 0
    for i in range(len(matrix1)) :
        sum += matrix1[row][i] * matrix2[i][col]
    return sum  
        
    
def produit_matrice(matrix1 : list[list],matrix2 : list[list]) -> list[list]:
    matrix1_cols : int = len(matrix1[0])
    matrix2_rows : int = len(matrix2)
    if(matrix1_cols != matrix2_rows):
        raise Exception("Le nomber des lignes de la matrice 1 different de le nomber des colonnes de la matrice 2 ")            
        exit()
    produit: list[list] = []   
    for i in range(matrix2_rows):
        row : list = []
        for j in range(matrix1_cols) :
            row.append(produit_deux_vecteures(matrix1.copy(),i,matrix2.copy(),j))
        produit.append(row)
    return produit

def transposee(matrix : list[list]) -> list[list] :
    transposee : list[list] = [] 
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)) :
            row.append(matrix[j][i])
        transposee.append(row)
    return transposee
                  
def est_traingulaire_sup(matrix : list[list]) -> bool :
    if len(matrix) != len(matrix[0]) :
        raise Exception("la matrice doit etre Carre ")
    taille_de_matrice = len(matrix)
    for row in range(taille_de_matrice) :
        col =  0
        while(col < row):
            if(matrix[row][col] != 0):
                return False
            col +=1
    return True
def est_traingulaire_inf(matrix : list[list]) -> bool :
    if len(matrix) != len(matrix[0]) :
        raise Exception("la matrice doit etre Carre ")
    taille_de_matrice = len(matrix)
    for row in range(taille_de_matrice) :
        col = row+1
        while(col < taille_de_matrice):
            if(matrix[row][col] != 0):
                return False
            col +=1
    return True
def est_Carree(matrix : list[list]) -> bool :
    if len(matrix) == len(matrix[0]) :
        return True
    return False

def est_caree_et_diagonale(matrix : list[list]) -> bool :
    if not est_Carree(matrix) :
        return False
    if(not (est_traingulaire_sup(matrix) or est_traingulaire_inf(matrix) )) :
        return False
    for i in range(len(matrix)) :
        if matrix[i][i] != 0 :
            return True
    return False 
def est_de_meme_taille(matrix1 :list[list],matrix2 : list[list]):
    matrix1_rows : int = len(matrix1)
    matrix1_cols : int = len(matrix1[0])
    matrix2_rows : int = len(matrix2)
    matrix2_cols : int = len(matrix2[0])
    if(matrix1_rows == matrix2_rows and matrix1_cols == matrix2_cols) :
        return True
    return False
       


def est_egaux(matrix1 :list[list],matrix2 : list[list]) -> bool :
    if not est_de_meme_taille(matrix1 ) :
        return False
    for i in range(len(matrix1)) :
        for j in range(len(matrix1[0])) :
            if matrix1[i][j] != matrix2[i][j] :
                return False
    return True


    
def est_symetrique(matrix :list[list])-> bool :
    a =  transposee(matrix) 
    if est_egaux(matrix,a) :
        return True
    return False

def DeterminantOrder2(matrix : list[list]) :
    if not est_Carree(matrix) or len(matrix) != 2 :
        raise Exception("ce n est pas caree d order 2")
    return matrix[0][0]*matrix[1][1] - matrix[0][1] *matrix[1][0]

def SousMatrice(row : int,col : int,matrix : list[list]) -> list[list] :
    sub_matrix = []
    for i in range(len(matrix)) :
        if i == row : continue
        line = []
        for j in range(len(matrix[0])) :
            if j == col : continue
            line.append(matrix[i][j])
        sub_matrix.append(line) 
    return sub_matrix

def Determinant(matrix : list[list]) -> int:
    print("1")
    if len(matrix) == 2 :
        return DeterminantOrder2(matrix)
    det = 0
    mul = 1 
    for j in range(len(matrix[0])) :
        sub_matrix = SousMatrice(0,j,matrix)
        
        det += mul*matrix[0][j]*Determinant(sub_matrix)
        mul=(-mul)
    return det

#
   
"""
1- Calucluer le déterminant d une matrice
2- Calculer l inverse d une matrice
3- Résoudre une equation matricielle

"""
def matrice_cofacteurs(matrix : list[list]):
    if not est_Carree(matrix.copy()) : 
        raise Exception("cette n est pas caree")
    c_matrix = []
    mul = 1
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[0])):
            submatrix = SousMatrice(i,j,matrix.copy())
            submatrix_det = Determinant(submatrix)
            line.append(mul*submatrix_det)
            mul = (-mul)
            pass
        c_matrix.append(line)
    return c_matrix
def matrice_inverse(matrix : list[list]) :
    det = Determinant(matrix)
    if det == 0 :
        raise Exception("determinant de la matrice est 0 ")
    inverse = []
    matrice_c = matrice_cofacteurs(matrix)
    matrice_c_t =  transposee(matrice_c)
    matrice_identite_avec_det = produit_matrice_par_scalaire(1/det,len(matrix) )
    inverse = produit_matrice(matrice_identite_avec_det,matrice_c_t)
    return inverse
#AX = B
def resoudre_systeme_equation(matrice1,matrice2):
    inverse_matrice1 = matrice_inverse(matrice1)
    solution = produit_matrice(inverse_matrice1,matrice2)
    return solution
def menu():
    matrix = lire_matrice_carre()
    affiche_matrice(matrix)
    matrix2 =  [[ 8 ,1 , 1],[ 9  ,2 ,1],[0  ,1  ,2]]
    print()
    print("Operations sur les marices")
    print("1 : ’afficher la matrice d’identité d’ordre N")
    print("2 : calculer la somme de deux matrices de même taille")
    print("3 : calculer le produit de deux matrices")
    print("4 : calculer la transposée d’une matrice")
    print("5 : tester si une matrice est triangulaire supérieure")
    print("6 : tester si une matrice est triangulaire inférieure")
    print("7 : tester si une matrice carrée est diagonale")
    print("8 : tester si une matrice carrée est symétrique")
    print("9 : calculer le determinant d une matrice carree")
    print("10 : calculer la matrice   de cofacteur")
    print("11 : calculer l inverse de  matrice")
    print("12 : resoudre un systeme d equation")


    operation = int(input("Donner le code d operation : "))
    if(operation == 1) :
        afficher_matrice_identite()
    elif(operation == 2) :
        matrix2  = lire_matrice_carre()
        print()
        sum = somme_matrice(matrix,matrix2)
        print()
        affiche_matrice(sum)
    elif operation == 3 :
        matrix2  = lire_matrice_carre()
        print()
        produit = produit_matrice(matrix,matrix2)
        affiche_matrice(produit)
    elif(operation == 4) :
        t = transposee(matrix)
        affiche_matrice(t)
    elif(operation == 5) :
        if est_traingulaire_sup(matrix) :
            print("cette matrice est triangulaire supérieure")
        else : print("cette matrice n est pas triangulaire supérieure")
    elif(operation == 6) :
        if est_traingulaire_inf(matrix) :
            print("cette matrice est triangulaire inférieure")
        else : print("cette matrice n est pas triangulaire inférieure")
    elif(operation == 7) :
        if est_caree_et_diagonale(matrix) :
           print("cette matrice carrée est diagonale")
        else :
           print("cette matrice n est pas carrée  est diagonale")    
    elif(operation == 8) :
        if est_symetrique(matrix) :
           print("cette matrice est carrée et symétrique")
        else :
           print("cette matrice n est pas carrée  est  symétrique")
    elif(operation == 9) :
        det = Determinant(matrix)
        print(f"Le determinant de la matrice est {det}")
    elif(operation == 10) :
        result = matrice_cofacteurs(matrix)
        print("La matrice de cofacteur est :")
        affiche_matrice(result)
    elif(operation == 11) :
        result = matrice_inverse(matrix)
        print("L inverse de matrice  est :")
        affiche_matrice(result)
    elif(operation == 12) :
        result = resoudre_systeme_equation(matrix,matrix2)
        print("la solution de systeme d equation est  : ")
        affiche_matrice(result)
    print()
    print("Fin")


if __name__ == "__main__" :
    menu()

