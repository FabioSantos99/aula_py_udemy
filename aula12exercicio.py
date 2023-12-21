
# def criar_multiplicador(multiplicador):
#       def multiplicar(numero):
#             return numero * multiplicador
#       return multiplicar

# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# quadruplicar = criar_multiplicador(4)

# print(duplicar(5))
# print(triplicar(6))
# print(quadruplicar(3))


def calculadorDeNumeros(num):
      def calc(sum, sub, mult, div):

            return sum + num, sum - sub, sum * mult, sum / div
      
      return calc

numeroparametro = calculadorDeNumeros(10)

print(numeroparametro(300, 7, 3, 10))