"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Digite seu nome: \n')
    print(f'Seu nome é {nome}')

    if nome == 'Sair':
        break
