import numpy as np
valores = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 1000, 11000]
"""
Classes: 6
1k < 2k
2k < 4k
4k < 6k
6k < 8k
8k < 10k
>=10k  

"""

# for value in valores:
#     print(value)
#
#     saida = np.array([0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0])
#
#     if value < 2000:
#         saida[0] = 1
#         print(saida)
#
#     elif 2000 <= value < 4000:
#         saida[1] = 1
#         print(saida)
#
#     elif 4000 <= value < 6000:
#         saida[2] = 1
#         print(saida)
#
#     elif 6000 <= value < 8000:
#         saida[3] = 1
#         print(saida)
#
#     elif 8000 <= value < 10000:
#         saida[4] = 1
#         print(saida)
#
#     elif value >= 10000:
#         saida[5] = 1
#         print(saida)

# camadaSaida = np.asarray([7.38194214e-57, 1.32482929e-44, 4.22102729e-39, 4.71125498e-26,
#                           3.02525635e-08, 1.23723655e-29])
# print(camadaSaida)
# for index, saida in enumerate(camadaSaida):
#     if index == np.argmax(camadaSaida):
#         camadaSaida[index] = 1
#     else:
#         camadaSaida[index] = 0
# print(camadaSaida)

# saidas = np.asarray([[1,0], [0,1]])
# y_esperado = []
# for saida in saidas:
#     print(np.argmax(saida) + 1)
#     y_esperado.append(np.argmax(saida) + 1)
#
# print(y_esperado)

print(np.linspace(1, 5, 5))