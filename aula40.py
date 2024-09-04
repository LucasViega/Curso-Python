"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in lexto
texto = iter('Lucas') # __iter__()

# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# iterator = iter(texto) # iterator

# while True:
#     try:
#         letra= next(iterator)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)


