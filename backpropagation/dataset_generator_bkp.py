from random import random, seed, randrange

dict_dataset = {}

"""
A chave vai ser o entrada (conjunto das oito respostas)
O valor vai ser a saída
"""

list_pesosPerguntas = [3.326, 2.748, 3.495, 3.103, 1.635, 1.478, 1.091, 3.001]
numTotalExemplos = 2
numAlternativas = list_pesosPerguntas.__len__()
entrada, saida = [], []
grama, fogo, terra = 0, 0, 0

with open('dataset_treino.txt', 'w') as dataset_treino:
    dataset_treino.close()

with open('dataset_teste.txt', 'w') as dataset_teste:
    dataset_teste.close()

end = False


for i_exemplo in range(numTotalExemplos):
    seed()

    print('Exemplo: ', i_exemplo)
    entrada, saida = [], []
    grama, fogo, terra = 0, 0, 0

    for index, peso in enumerate(list_pesosPerguntas):
        alternativa = round((random() * 2) + 1)
        entrada.append(alternativa)
    # print('enntradas:', entrada)
    # print('pesos:    ', list_pesosPerguntas)

    for index, elem in enumerate(entrada):
        if elem == 1:
            grama += list_pesosPerguntas[index]

        elif elem == 2:
            fogo += list_pesosPerguntas[index]

        elif elem == 3:
            terra += list_pesosPerguntas[index]

    maximo = max(grama, fogo, terra)

    if maximo == grama: print('grama'); saida = [1, 0, 0]
    elif maximo == fogo: print('fogo'); saida = [0, 1, 0]
    elif maximo == terra: print('terra'); saida = [0, 0, 1]

    e = ""
    for elem in entrada:
        e += str(elem) + ';'

    e = e[:-1]

    s = ""
    for elem in saida:
        s += str(elem) + ';'

    s = s[:-1]

    dict_dataset[e] = s
    # print(grama, fogo, terra)
    # print(saida)

for key, value in dict_dataset.items():
    print(key, value)