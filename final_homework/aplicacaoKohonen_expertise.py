from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt

book = load_workbook('results_teste.xlsx')
sheet = book.active
from trabalho_final.kohonen import kohonen

i = 2
end = False

jobs_dict = dict()

while not end:
    if not sheet['A' + str(i)].value == None:
        # jobs_dict['A' + str(i)] = [int(sheet['A' + str(i)].value[2:].replace('.', '')), []]
        jobs_dict['A' + str(i)] = [float(sheet['A' + str(i)].value[2:].replace('.', '')) / 2000, []]
        j = 1

        while not sheet[chr(ord(chr(ord('B') + j))) + str(i)].value == None:
            jobs_dict['A' + str(i)][1].append(sheet[chr(ord(chr(ord('B') + j))) + str(i)].value)
            j += 1

        i += 1
    else:
        end = True

atributes = ['junior', 'pleno', 'senior']
initial_SIGMA = 1
initial_ALPHA = 0.5

n_epocas = 1

SIGMA_array = np.linspace(initial_SIGMA, 0.1, n_epocas)
ALPHA_array = np.linspace(initial_ALPHA, 1, n_epocas)

w_arrays = np.zeros((1000, 2))

for index, array in enumerate(w_arrays):
    # print(index, array)
    # w_arrays[index] = [np.random.randint(1000, 10000), np.random.random() * 2]
    w_arrays[index] = [np.random.random() * 10, np.random.random() * 10]


x = [array[1] for array in w_arrays]
y = [array[0] for array in w_arrays]
# plt.scatter(x=x, y=y, label='Pesos iniciais', color='black')
plt.scatter(x=x, y=y, label='Initial weights', color='gray', edgecolors='black', marker='.')
plt.legend()

plt.title('number of epochs: ' + str(n_epocas))
plt.xlabel('Expertise')
plt.ylabel('Salary (x2000)')
plt.savefig('initial weights')
plt.show()

entry = np.array([])

current_job = 0
for epoca in range(n_epocas):
    print('epoca: ', epoca)
    for key, value in jobs_dict.items():
        print(key, jobs_dict.__len__())
        # print('\n' + '-' * 30)
        # print(key, value)
        temp_atributes = []

        for elem in value[1]:
            if elem in atributes:
                temp_atributes.append(elem)

                for i in range(len(atributes)):
                    if elem == atributes[i]:

                        # print('Rede atualiza os pesos para o atributo: ', elem)

                        if elem == 'junior':
                            # entry = np.array([jobs_dict[key][0], 0])
                            entry = np.array([jobs_dict[key][0], 0])

                        elif elem == 'pleno':
                            entry = np.array([jobs_dict[key][0], 5])
                        elif elem == 'senior':
                            entry = np.array([jobs_dict[key][0], 10])

                        # w_arrays = kohonen(w_arrays=w_arrays, entry=entry, SIGMA=initial_SIGMA, ALPHA=initial_ALPHA, n_epocas=1)
                        w_arrays = kohonen(w_arrays=w_arrays, entry=entry, SIGMA=SIGMA_array[epoca], ALPHA=ALPHA_array[epoca], n_epocas=1)
                        # w_arrays = kohonen(w_arrays=w_arrays, entry=entry, SIGMA=SIGMA_array[epoca], ALPHA=initial_ALPHA, n_epocas=1)


                        # print('-' * 20)
                        # print('w_arrays atualizados')
                        # print(w_arrays)

        #  if not temp_atributes == []:
        #      print(temp_atributes)
        #
        # else:
        #     print('Atributos nao foram encontrados')

        current_job += 1

    current_job = 0

print(w_arrays)
x = [array[1] for array in w_arrays]
y = [array[0] for array in w_arrays]
plt.scatter(x=x, y=y, color='gray', edgecolors='black', marker='.')
plt.title('number of epochs: ' + str(n_epocas))
plt.xlabel('Expertise')
plt.ylabel('Salary (x2000)')
plt.savefig('final_network_weights.png')
plt.show()
