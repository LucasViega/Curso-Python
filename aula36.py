"""Calculadora com while"""

while True:
    numero_1 = input('Digite o primeiro número: \n')
    numero_2 = input('Digite o segundo número: \n')
    operador = input('Digite o operador (+-/*): \n')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou mais números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua operação. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} =', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} =', numero_1_float - numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float } =', numero_1_float / numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float } =', numero_1_float * numero_2_float)
    else:
        print('Jamais deveria chegar aqui.')

    sair = input('Quer sair? [s]im / [n]ão \n').lower().startswith('s')

    if sair:
        break
