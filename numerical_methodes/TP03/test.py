import TP05.SystemsEquationLinear as eql
import pytest
def test_laDecente():
    A = [
        [-2,0,0],
        [-1,3,0],
        [4,1,3]
    ]
    B = [4,-1,0]
    X = [-2,-1,3]
    assert X == eql.descente(A,B)

    A = [
        [2,0,0,0],
        [-1,2,0,0],
        [4,-1,3,0],
        [1,3,-3,2],
    ]
    B = [-4,6,-1,-15]
    X = [-2,2,3,-5]

    assert X == eql.descente(A,B)

def test_remontee():
    A = [
        [3,2,5],
        [0,1,-3],
        [0,0,1]
    ]
    B = [4,-2,1]
    X = [-1,1,1]
    assert X == eql.remonte(A,B)

    A = [
        [4,1,-1,-2],
        [0,3,-2,1],
        [0,0,1,-1],
        [0,0,0,1]
    ]
    B = [0,5,1,-1]
    X = [-1,2,0,-1]
    assert  X == eql.remonte(A,B)

    A = [
        [10,5,5,0],
        [0,4,6,4],
        [0,0,-4,2],
        [0,0,0,-0.25]
    ]
    B= [-25,-4,4,-2.5]
    X =  [4.0, -17.0, 4.0, 10.0]
    assert   [4.0, -17.0, 4.0, 10.0] == eql.remonte(A,B)

def test_triangulization():
    A = [
        [10,5,5,0],
        [2,5,7,4],
        [4,4,1,4],
        [-2,-2,1,-3]
    ]
    B = [25,2,12,-10]
    A_ = [
        [10,5,5,0],
        [0,4,6,4],
        [0,0,-4,2],
        [0,0,0,-0.25]
    ]
    B_ = [-25,-4,4,-2.5]
    assert A_,B_ == eql.triangulization(A,B)
def test_EliminationGaussPivotNonNull():
    A = [
        [10,5,5,0],
        [2,5,7,4],
        [4,4,1,4],
        [-2,-2,1,-3]
    ]
    B = [25,2,12,-10]
    assert [9.375,-18.25,4.5,10.75 ] ==  eql.EliminationGaussPivotNonNull(A,B)
def test_EliminationGaussPivotPartiel():
    A = [
      [1,6,9],
      [2,1,2],
      [3,6,9]
    ]
    B = [1,2,3]
    X = [1,0,0]
    assert X ==  eql.EliminationGaussPivotPartiel(A,B)
def test_EliminationGaussPivotTotal():
    A = [
        [1,3,3],
        [2,2,5],
        [3,2,6]
    ]
    B = [-2,7,12]
    X = [4,-3,1]
    assert [1.003, -3.001, 3.995] == eql.EliminationGaussPivotTotal(A,B) 
def test_Identitie():
    n = 4
    I = [
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1],
    ]
    assert I == eql.matriceIdentite(n)
    n = 2
    I = [
        [1,0],
        [0,1],
    ]
    assert I == eql.matriceIdentite(n)
def test_DecomposotionLU() :
    A = [
        [1,2,3],
        [1,1,2],
        [1,1,1],
    ]
    B =[2,0,1]
    _L = [
        [1,0,0],
        [1,1,0],
        [1,1,1]
    ]
    _U = [
        [1,2,3],
        [0,-1,-1],
        [0,0,-1],
    ]
    assert _U,_L == eql.DecomposotionLU(A,B)
def test_SolveDecomposotionLU():
    A = [
        [1,2,3],
        [1,1,2],
        [1,1,1],
    ]
    B =[2,0,1]
    X = [-1,3,-1]
    X == eql.SolveDecomposotionLU(A,B)
    pass
def test_Jacobi():
    A = [
        [10,1,1],
        [1,10,1],
        [1,1,10], 
    ]
    B = [6,12,3]
    VectInitiall = [0,0,0]
    stop = 4
    X3 = [0,9532,0,9722,0,99306]
    X= [0.47222222, 1.13888889 ,0.13888889]
#    assert X == eql.Jacobi(A=A,B=B,VectIn
# itiall=VectInitiall,stop=stop)
def test_GaussSeidel():
    pass