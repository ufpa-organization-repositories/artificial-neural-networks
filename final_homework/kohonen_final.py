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

atributes = ['junior', 'pleno', 'senior']
SIGMA = 8
ALPHA = 0.1
n_epocas = 100

# w_arrays = np.array([[9, 4, 3],
#                      [3, 5, 8],
#                      [1, 3, 5]])
#

w_arrays = np.array(10 *
                    [[np.random.randint(1000, 10000), np.random.random() * 2]])
# entry = np.array([4, 7, 1])

print('w_arrays')
print(w_arrays)

for key, value in jobs_dict.items():
    print('\n' + '-'*30)
    print(key, value)
    temp_atributes = []

    for elem in value[1]:
        if elem in atributes:
            temp_atributes.append(elem)

            for i in range(len(atributes)):
                if elem == atributes[i]:

                    print('Rede atualiza os pesos para o atributo: ', elem)
                    if elem == 'junior':
                        entry = np.array([jobs_dict[key][0], 0])
                    elif elem == 'pleno':
                        entry = np.array([jobs_dict[key][0], 1])
                    elif elem == 'senior':
                        entry = np.array([jobs_dict[key][0], 2])

                    w_arrays = kohonen(w_arrays=w_arrays, entry=entry, SIGMA=SIGMA, ALPHA=ALPHA, n_epocas=1)
                    print('-' * 20)
                    print('w_arrays atualizados')
                    print(w_arrays)

    if not temp_atributes == []:
        print(temp_atributes)
    else:
        print('Atributos nao foram encontrados')
