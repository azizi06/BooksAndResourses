import pytest
import integration
import math
def f1(x):
    return math.cos(x**2) 
def testTrapez():
    a = 0
    b = 1
    n = 4
    assert 0.895 <= integration.trapez(f=f1,a=a,b=b,n=n) <= 0.896
def testReTrapez():
    a = 0
    b = 1
    n = 4
    assert 0.895 <= integration.re_trapez(f=f1,a=a,b=b,n=n) <= 0.896
    