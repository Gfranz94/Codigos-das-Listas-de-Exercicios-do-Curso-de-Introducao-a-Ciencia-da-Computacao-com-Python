#Exercício 2 - Máximo com 3 parâmetros
#Reescreva a função 'maximo' do outro exercício,
#que devolve o maior valor dentre dois inteiros recebidos,
#para que ela passe a receber 3 valores inteiros como parâmetros e
#devolva o maior dentre eles.

def maximo(x, y, z):
    if x > y > z or x > z > y:
        return x
    elif y > x > z or y > z > x:
        return y
    else:
        return z
#testes da função a seguir:
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
