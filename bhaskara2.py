#Este programa calcula as raízes de uma equação quadrática
#É um exercício de execução condicional

from math import sqrt

#print("Olá, este programa resolve uma equação quadrática utilizando a fórmula de Bhaskara!!")
#print("Isto é, resolve uma equação na forma a*x**2 + b*x + c = 0")

a = float(input("Digite o valor do coeficiente 'a': "))
b = float(input("Digite o valor do coeficiente 'b': "))
c = float(input("Digite o valor do coeficiente 'c': "))

#print("A equação quadrática fica na forma", a,"*x**2 +", b,"*x +", c," = 0")

delta = b**2 - 4*a*c
if delta < 0:
    print("esta equação não possui raízes reais")
if delta == 0:
    x = -b/(2*a)
    print("a raiz desta equação é", x)
if delta > 0:
    x2 = (-b-sqrt(delta))/(2*a)
    x1 = (-b+sqrt(delta))/(2*a)
    if x1<x2:
        print("as raízes da equação são", x1,"e", x2)
    else:
        print("as raízes da equação são", x2,"e", x1)
