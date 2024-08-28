"""
Faca um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print('Bem vindo ao primeiro programa.')
print(30 * '-')

numero_digitado = input('Digite um número inteiro: \n')

if numero_digitado.isdigit():
    numero_digitado_int = int(numero_digitado)
    par_impar = numero_digitado_int % 2 == 0
    par_impar_texto = "Ímpar"

    if par_impar:
        par_impar_texto = 'par'
    
    print(f'O número {numero_digitado_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro.')

print(30 * '-')
print(30 * '-')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex
Bom da 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
print('Bem vindo ao segundo programa.')
print(30 * '-')

horario_string = input('Digite o horário de agora: \n')
horario_inteiro = int(horario_string)

if horario_inteiro >= 0 and horario_inteiro <= 11:
    print(f'Bom dia agora são {horario_inteiro} horas.')
elif horario_inteiro >= 12 and horario_inteiro <= 17:
    print(f'Boa tarde agora são {horario_inteiro} horas.')
elif horario_inteiro >= 18 and horario_inteiro <= 23:
    print(f'Boa noiote agora são {horario_inteiro} horas.')
else:
    print("Você não digitou um horário válido")

print(30 * '-')
print(30 * '-')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maiand que 6 escreva "Seu nome é muito grande".
"""
print('Bem vindo ao terceiro programa.')
print(30 * '-')

primeiro_nome = input('Digite seu primeiro nome: \n')
tamanho_nome = len(primeiro_nome)

if tamanho_nome <= 4:
    print(f'O nome "{primeiro_nome}" é um nome curto')
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print(f'O nome "{primeiro_nome}" é um nome nomal')
else:
    print(f'O nome "{primeiro_nome}" é um nome muito grande.')
