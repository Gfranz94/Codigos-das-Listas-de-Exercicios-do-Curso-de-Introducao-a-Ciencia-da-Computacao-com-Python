#xercício 1: Triângulos retângulos
#Escreva, na classe Triangulo, o método retangulo() que devolve True
#se o triângulo for retângulo, e False caso contrário.

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        else:
            return False
