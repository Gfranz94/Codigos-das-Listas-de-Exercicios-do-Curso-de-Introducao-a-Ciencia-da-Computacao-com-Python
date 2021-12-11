#Exercício 2: Triângulos semelhantes
#Ainda na classe Triangulo, escreva um método semelhantes(triangulo)
#que recebe um objeto do tipo Triangulo como parâmetro e verifica se o
#triângulo atual é semelhante ao triângulo passado como parâmetro.
#Caso positivo, o método deve devolver True. Caso negativo, deve devolver False
#Um triângulo é semelhante a outro triângulo se a razão (divisão)
# entre os comprimentos dos seus lados forem iguais.

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        if self.a // triangulo.a == self.b // triangulo.b:
            return True
        else:
            return False
