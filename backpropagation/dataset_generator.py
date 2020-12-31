from random import random, seed, randrange

dict_dataset = {}

"""
A chave vai ser o entrada (conjunto das oito respostas)
O valor vai ser a saída
"""

list_pesosPerguntas = [3, 2, 3, 3, 1, 1, 1, 3]
# list_pesosPerguntas = [350, 200, 150, 250, 100, 400, 300, 50]
numTotalExemplos = 6000
numAlternativas = list_pesosPerguntas.__len__()
entrada, saida = [], []
grama, fogo, terra = 0, 0, 0

with open('dataset.txt', 'w') as dataset_file:
    dataset_file.close()

with open('dataset_teste.txt', 'w') as dataset_file:
    dataset_file.close()

end = False
count = 0
cont_seed = 0
while count < numTotalExemplos:


    entrada, saida = [], []
    grama, fogo, terra = 0, 0, 0

    for index, peso in enumerate(list_pesosPerguntas):
        validating = True

        while validating:
            seed()
            alternativa = round((random() * 2) + 1)
            if 0 < index < list_pesosPerguntas.__len__() - 1:
                if not alternativa == entrada[index - 1]:
                    entrada.append(alternativa)
                    valid = True
                else:
                    valid = False

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

    if not e in dict_dataset.keys():
        print('Exemplo: ', count)
        dict_dataset[e] = s
        count += 1
    # print(grama, fogo, terra)
    # print(saida)

    cont_seed += 1

dict_teste = {}

with open('dataset.txt', 'a') as dataset_file:
    dataset_file.write('V1;V2;V3;V4;V5;V6;V7;V8;N1;N2;N3\n')
    for key, value in dict_dataset.items():
        # print(key, value)
        egg = key + ';' + value + '\n'
        print(egg)
        dataset_file.write(egg)



    dataset_file.close()




    # with open('dataset_teste.txt', 'a') as dataset_file:
    #     dataset_file.write('V1;V2;V3;V4;V5;V6;V7;V8;N1;N2;N3\n')
    #     for key, value in dict_teste.items():
    #         egg = key + ';' + value + '\n'
    #         print(egg)
    #         dataset_file.write(egg)
    #
    #     dataset_file.close()

# n = 4
# lista = [1, 2, 3, 4]
# a = int(n / 2)
# print(lista[:a])
# print(lista[a:])
#
# for elem in lista[:a]:
#     print(elem)
# print("-" *10)
# for elem in lista[a:]:
#     print(elem)


# d = {1:'um', 2:'dois', 3:'tres', 4:'quatro'}
#
# for index, [key, value] in enumerate(d.items()):
#     print(index, key, value)


# d = {1:2}
# print(2 in d.keys())