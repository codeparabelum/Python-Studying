"""variáveis dentro de strings"""
nome='arthur'
peso = 82
altura = 1.84
imc = peso/(altura**2)

"""para usar variáveis dentro de strings usa-se {x y z}"""
"""F-strings"""
linha1  = f'{nome} tem {altura} de altura'
linha2  = f'pesa {peso} em quilos e seu imc é:{imc:.2f}'

print(linha1)
print(linha2)





