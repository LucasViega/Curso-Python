"""
Formatação básica de strings

s - string
d - int
f - float
.<número de dígitos>f
x ou x - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.71293812398162:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
