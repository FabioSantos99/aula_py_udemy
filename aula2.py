string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')

x = 10 == 11
variavel = 'é verdadeiro' if x else 'é falso'

print(variavel)
print(*lista)
print(*string)
print(*tupla)

print('Valor' if False else 'Outro valor' if True else 'Fim')