import Laboratorio4;
import pytest;
    
def test_convertirDecHex_1():
    assert Laboratorio4.convertirDecHex(5) == '5'
    
def test_convertirDecHex_2():
    assert Laboratorio4.convertirDecHex(10) == 'A'
    
def test_convertirDecHex_3():
    assert Laboratorio4.convertirDecHex(25) == '19'
    
def test_convertirDecHex_4():
    assert Laboratorio4.convertirDecHex(30) == '1E'
    
def test_convertirDecHex_5():
    assert Laboratorio4.convertirDecHex(300) == '12C'

def test_convertirHexDec_1():
    assert Laboratorio4.convertirHexDec('5') == 5
    
def test_convertirHexDec_2():
    assert Laboratorio4.convertirHexDec('A') == 10
    
def test_convertirHexDec_3():
    assert Laboratorio4.convertirHexDec('19') == 25
    
def test_convertirHexDec_4():
    assert Laboratorio4.convertirHexDec('1E') == 30
    
def test_convertirHexDec_5():
    assert Laboratorio4.convertirHexDec('12C') == 300
