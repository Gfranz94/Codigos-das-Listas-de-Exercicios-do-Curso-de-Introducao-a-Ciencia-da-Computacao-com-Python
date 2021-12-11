#exercicio adicional 2 da lista de exercicios 1 do curso Introdução à Ciência da Computação com Python parte 1

segtotal = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dia = segtotal // 86400
hora = (segtotal % 86400) // 3600
minuto = ((segtotal % 86400) % 3600) // 60
seg = (((segtotal % 86400) % 3600) % 60)

print(dia, "dias,", hora, "horas,", minuto, "minutos e", seg, "segundos.")
