from openpyxl import load_workbook
import numpy as np
book = load_workbook('results_teste.xlsx')
sheet = book.active
from trabalho_final.kohonen import kohonen

i = 2
end = False

jobs_dict = dict()

while not end:
    if not sheet['A' + str(i)].value == None:
        jobs_dict['A' + str(i)] = [int(sheet['A' + str(i)].value[2:].replace('.', '')), []]
        j = 2

        while not sheet[chr(ord(chr(ord('B') + j))) + str(i)].value == None:
            jobs_dict['A' + str(i)][1].append(sheet[chr(ord(chr(ord('B') + j))) + str(i)].value)
            j += 1

        i += 1
    else:
        end = True

atributes = ['HTML','CSS']

for key, value in jobs_dict.items():
    print('\n' + '-'*30)
    print(key, value)
    temp_atributes = []
    for elem in value[1]:
        if elem in atributes:
            temp_atributes.append(elem)
            print('Rede atualiza os pesos para o atributo: ', elem)

    if not temp_atributes == []:
        print(temp_atributes)
    else:
        print('Atributos nao foram encontrados')
