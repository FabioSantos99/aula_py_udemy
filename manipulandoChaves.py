pessoa = {}

chave = 'nome'


pessoa[chave] = 'Fabio'
pessoa['sobrenome'] = 'Santos'

lista = []
del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None :
      print('NÃO EXISTE')

      




