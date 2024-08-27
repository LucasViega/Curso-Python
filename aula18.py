"""
Operadores lógicos
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeira.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
São considerdoos falso (que você já viu)
0 0.0 '' False
Também existe o tipo None que é usado para representar um não valor
"""

entrada = input('[E]ntrar [S]sair: \n')
senha_digitada = input('SENHA: \n')

senha_permitida = '123456'
if entrada.upper() == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
 