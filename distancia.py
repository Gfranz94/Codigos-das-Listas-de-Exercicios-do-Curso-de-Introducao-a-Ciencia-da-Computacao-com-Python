#Exercício 1 - Distância entre dois pontos
#Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
#Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
#longe
#na saída. Caso o contrário, quando a distância for menor que 10, imprima
#perto

from math import sqrt

x1 = float(input("Digite o valor da coordenada x do primeiro ponto: "))
y1 = float(input("Digite o valor da coordenada y do primeiro ponto: "))
x2 = float(input("Digite o valor da coordenada x do segundo ponto: "))
y2 = float(input("Digite o valor da coordenada y do segundo ponto: "))

d = sqrt((x1-x2)**2 + (y1-y2)**2)

if d >= 10:
    print("longe")
else:
    print("perto")
