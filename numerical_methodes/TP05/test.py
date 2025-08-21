import interpolationPolynomiale as ip
import pytest

def test_puissace():
    assert 25 == ip.puissance(5,2)
    assert 32 == ip.puissance(2,5) 
    assert 1 == ip.puissance(2,0)

def test_vandermonde_polynomme():
    assert [1,2,4] == ip.vandermonde_polynomme(2,2)

def test_vandermonde_matrix():
    points = [(-2,-27),(0 ,-1),(1,0)]
    vmatrice = [[1,-2,4],
                [1,0,0],
                [1,1,1]]
    assert vmatrice == ip.vandermonde_matrix(points=points)

def test():
    points = [(-2,-14),(-1,-11/4),(2,-8),(4,-29)]
    vmatrice = ip.vandermonde_matrix(points=points)
def test_systemeLinear():
    p1 = [(-2,-14),(-1,-11/4),(2,-8),(4,-29)]
    points = p1
    vmatrice = ip.vandermonde_matrix(points=points)
    assert   == ip.systeme_linear(points=points)


   
   
   
   
    



