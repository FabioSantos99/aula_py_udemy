pessoa = {
      'nome': "Fabio",
      'sobrenome': 'Santos',
      'idade': 30,
      'cidade': 'São Paulo',
      'endereços': [
                  {'rua': 'Dionisio de Souza', 'numero': 369},
                  {'rua': 'das Flores', 'numero': 9000}
      ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
      print(chave, pessoa[chave])


# pessoa = dict(nome='Fabio', sobrenome='Santos')

