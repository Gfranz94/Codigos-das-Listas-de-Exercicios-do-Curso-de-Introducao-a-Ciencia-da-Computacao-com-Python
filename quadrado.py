#Exercício 1 da Lista de exercícios 1 do curso Introdução à Ciência da Computação com Python Parte 1
#Este programa pede o lado de um quadrado e imprime o valor do perímetro e da área do quadrado

lado = int(input("Digite o valor correspondente ao lado de um quadrado: "))
perimetro = 4 * lado
area = lado ** 2
print("perímetro:", perimetro, "- área:", area)
