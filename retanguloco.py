#Exercício 2
#Refaça o exercício 1 imprimindo os retângulos sem preenchimento,
#de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

saltalinha = 1
while saltalinha <= altura:
    linha = 1
    while linha <= largura:
        if saltalinha == 1 or saltalinha == altura or linha == largura or linha == 1:
            print("#", end = "")
        else:
            print(" ", end = "")
        linha += 1
    saltalinha += 1
    print()


####
#  #
####
