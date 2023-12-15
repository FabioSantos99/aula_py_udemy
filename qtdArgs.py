# x, y, * resto = 1, 2, 3, 4
# print(x, y, resto)




def soma(*args):
      total = 0
      for numero in args:
            print('Total', total, numero)
            total = total + numero
      return total
      #       print("Total", total)
      # print(total)

soma_1_2_3 = soma(1, 2, 4)
print(soma_1_2_3)

numeros = 1,2, 5, 2, 5, 51, 6, 11, 55, 31
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))

