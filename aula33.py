"""
Repetições
while (enquanto)
Executa uma ação enquanto um condição for verdadeira
Loop infinito -> Quando um código não tem fimi
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print(f'Não vou mostar o {contador}.')
        continue

    if contador >= 10 and contador <= 27:
        print(f'Não vou mostar o {contador}.')
        continue

    print(contador)

    if contador == 40:
        break
