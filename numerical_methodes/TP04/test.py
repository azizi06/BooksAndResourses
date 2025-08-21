import interpolationPolynomiale as ip
import pytest
def test_lagrange():
    x = 7
    points = [(1,1),(4,2),(9,3),(16,4)]
    assert 2.64     <= ip.lagrange(x=x,points=points) <=2.7
def test_newton():
    x = 7
    points = [(1,1),(4,2),(9,3),(16,4)]
    assert  2.64<= ip.newton(x=x,points=points) <=2.7
print("Test Donne")