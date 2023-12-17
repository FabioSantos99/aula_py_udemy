

def soma(*args):
      
      total = 1
      for numero in args:

            total = total * numero
      return total
     
def imparPar():

      global multi_soma
      
      if multi_soma % 2 == 0:
            print(f'O resultado {multi_soma} é par')
      else:
            print(f'O resultado {multi_soma} é impar')


multi_soma = soma(5, 3, 6, 7, 5)
print(multi_soma)
imparPar()
