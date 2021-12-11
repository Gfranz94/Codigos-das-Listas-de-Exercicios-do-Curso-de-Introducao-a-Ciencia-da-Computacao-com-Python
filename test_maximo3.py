#funções para o pytest do prog maximo3.py


def maximo(x, y, z):
    if x > y > z or x > z > y:
        return x
    elif y > x > z or y > z > x:
        return y
    else:
        return z
        
def test_maximox1():
    assert maximo(30, 14, 10) == 30

def test_maximox2():
    assert maximo(30, 14, 20) == 30

def test_maximoy1():
    assert maximo(30, 40, 10) == 40

def test_maximoy2():
    assert maximo(30, 40, 35) == 40

def test_maximoz1():
    assert maximo(30, 14, 50) == 50

def test_maximoz2():
    assert maximo(30, 40, 50) == 50
