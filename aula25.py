"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Digite um número que irei dobrá-lo \n'
)

try:
    print(
        f'STR: {numero_str}'
    )
    numero_float = float(numero_str)
    print(
        f'FLOAT: {numero_float}'
    )
    print(
        f'O dobro de {numero_str} é {numero_float * 2:.2f}'
    )
except:
    print('Isso não é um número.')


