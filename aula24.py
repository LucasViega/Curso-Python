"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuario para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Se o nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A útima letra do seu nome é {letra}
Se nada for digitado em nome ou idae:
    exiba:
        'Desculpe, você deixou campos vazios.'
"""

nome = input('Digite seu nome: \n')
idade = input('Digite sua idade: \n')

if nome and idade:
    print(
        f'Seu nome é {nome}.'
    )

    print(
        f'Seu nome invertido é {nome[::-1]}.'
    )

    if ' ' in nome:
        print(
            f'O nome possui espaço.'
        )
    else:
        print(
            f'O nome não possui espaços.'
        )

    print(
        f'Seu nome tem {len(nome)} caracteres incluindo espaços.'
        )

    print(
        f'A primeira letra do seu nome é: {nome[0]}'
    )


    print(
        f'O útima letra do seu nome é: {nome[-1]}'
    )

else:
    print(
        f'Desculpe, você deixou campos vazios.'
    )
