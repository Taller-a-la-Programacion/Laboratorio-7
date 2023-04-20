import Laboratorio7;
import pytest;

matriz = [[2,4,6,8,10], [1,3,5,7,9], [4,8,12,16,20], [0,0,0,0,0], [5,10,5,10,5]]

def test_cortarMatriz_1():
    assert Laboratorio7.cortarMatriz(matriz, 2, 3) == [[2,4,6], [1,3,5]]
    
def test_cortarMatriz_2():
    assert Laboratorio7.cortarMatriz(matriz, 2, 2) == [[2,4], [1,3]]
    
def test_cortarMatriz_3():
    assert Laboratorio7.cortarMatriz(matriz, 5, 5) == [[2,4,6,8,10], [1,3,5,7,9], [4,8,12,16,20], [0,0,0,0,0], [5,10,5,10,5]]
    
def test_cortarMatriz_4():
    assert  isinstance( str(Laboratorio7.cortarMatriz(matriz, 8, 5)), str) == isinstance('Error: los valores de la nueva matriz exceden las dimensiones actuales', str)
    
    
matriz = [[2,4,6,8,10], [1,3,5,7,9], [4,8,12,16,20], [10,20,30,40,50], [5,10,15,20,25]]

def test_cortarMatrizv2_1():
    assert Laboratorio7.cortarMatriz_v2(matriz, 2, 3, 2, 2) == [ [16,20], [40,50] ]
    
def test_cortarMatrizv2_2():
    assert Laboratorio7.cortarMatriz_v2(matriz, 2, 0, 2, 2) == [ [4,8], [10,20] ]
    
def test_cortarMatrizv2_3():
    assert Laboratorio7.cortarMatriz_v2(matriz, 0,0,5,5) == [[2,4,6,8,10], [1,3,5,7,9], [4,8,12,16,20], [10,20,30,40,50], [5,10,15,20,25]]
    
def test_cortarMatrizv2_4():
    assert  isinstance( str(Laboratorio7.cortarMatriz_v2(matriz, 2, 1, 6, 6), str) == isinstance('Error: los valores de la nueva matriz exceden las dimensiones actuales', str)
