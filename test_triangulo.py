import pytest
from triangulo import checktriangle

def test_case1_escaleno():
    assert checktriangle(6, 5, 10) == "Triangulo escaleno"

def test_case2_equilatero():
    assert checktriangle(6, 6, 6) == "Triangulo equilatero"

def test_case3_isosceles():
    assert checktriangle(3, 3, 4) == "Triangulo isosceles"

def test_case4_notriangulo1():
    assert checktriangle(4, 3, 0) == "No es un triangulo"

def test_case5_notriangulo2():
    assert checktriangle(8, 2, 4) == "No es un triangulo"

def test_case6_notriangulo3():
    assert checktriangle(2, 2, 5) == "No es un triangulo"

def test_case7_notriangulo4():
    assert checktriangle(2, 5, 2) == "No es un triangulo"

def test_case8_isosceles2():
    assert checktriangle(4, 5, 5) == "Triangulo isosceles"

def test_case9_isosceles3():
    assert checktriangle(5, 4, 5) == "Triangulo isosceles"