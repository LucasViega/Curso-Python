frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
quantidade_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
        print(letra_atual)
        i += 1
        continue

    if quantidade_apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        quantidade_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual
  
    print(letra_atual, quantas_vezes_letra_apareceu)
    i += 1

print(f'A letra que mais apareceu foi "{letra_apareceu_mais_vezes}" que apareceu {quantidade_apareceu_mais_vezes} vezes')
