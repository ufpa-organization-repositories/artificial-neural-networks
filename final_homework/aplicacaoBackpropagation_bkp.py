from trabalho_final.backpropagation_final import train_backpropagation, apply_backpropagation

from openpyxl import load_workbook
import numpy as np

book = load_workbook('results_teste.xlsx')
sheet = book.active

def get_jobs_dict_from_xls_file(sheet):
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

    return jobs_dict

def get_tecnologies_from_jobs_dict(jobs_dict):
    tecnologies = dict()
    for args in jobs_dict.values():
        # print(args[1][2:])

        for tecnology in args[1][2:]:


            try:

                if type(tecnologies[tecnology]) == int:
                    tecnologies[tecnology] += 1

                elif tecnologies[tecnology] == tecnology:
                    tecnologies[tecnology] = 1

            except:

                tecnologies[tecnology] = tecnology


    return tecnologies



jobs_dict = get_jobs_dict_from_xls_file(sheet=sheet)
tecnologies = get_tecnologies_from_jobs_dict(jobs_dict=jobs_dict)
print(tecnologies)

atributes = [key for key in tecnologies.keys()]
print(atributes)

entries = []
saidas = []

for key, value in jobs_dict.items():
    print('\n' + '-'*30)
    print(key, value)

    atributes_temp = value[1][2:]

    entry = dict()

    for tec in tecnologies:
        entry[tec] = 0

    for tec in atributes_temp:
        entry[tec] = 1

    print('atributes: ', atributes)



    entries.append(list(entry.values()))

    print(atributes)

    print('entry: ', entry)

    saidas.append(value[0])

print('\n' * 5)

entradas = np.asarray(entries)
saidas = np.asarray(saidas)
saidas = saidas.reshape(120,1)
print(entries)
print(saidas)

for e, s in zip(entries, saidas):
    print(s, e)

n_neuronios_camadaOculta = 8
epocas =10000
taxaAprendizagem = 0.5
momento = 1

# entradas = np.array([[0, 0],
#                      [0, 1],
#                      [1, 0],
#                      [1, 1]])
n_entradas = entradas[0].__len__()

# saidas = np.array([[0], [1], [1], [0]])
# n_saidas = saidas[0].__len__()
n_saidas = 10

# camadaSaida = np.zeros([epocas])

pesos0 = 2 * np.random.random((n_entradas, n_neuronios_camadaOculta)) - 1
pesos1 = 2 * np.random.random((n_neuronios_camadaOculta, n_saidas)) - 1

camadaSaida = np.zeros([epocas])
error_array = []

for entrada, saida in zip(entradas, saidas):
    pesos0, pesos1, camadaSaida, error_array = train_backpropagation(epocas=epocas,
                                                              entradas=entrada, pesos0=pesos0,
                                                              saidas=saida, pesos1=pesos1,
                                                              taxaAprendizagem=taxaAprendizagem, momento=momento)

apply_backpropagation(entradas=entradas, pesos0=pesos0,
                      pesos1=pesos1,
                      error_array=error_array)


# import numpy as np
# atributes = ['x', 'y', 'z']
#
# n_vagas = 1
# entry = []
#
# entry.append(atributes[:])
# print(entry)

#
# import numpy as np
# tecnologies_list = ['React Native', 'ReactJS', 'JavaScript', 'HTML', 'CSS', 'Ionic', 'Angular', '.NET', 'SQL Server', 'C#', 'AWS S3', 'AWS RDS (Relational Database Service)', 'Node.js', 'MongoDB', 'MySQL', 'Vue.js', 'PHP', 'Laravel', 'jQuery', 'RESTful', 'Java', 'SQL', 'Ruby on Rails', 'Git', 'Testes automatizados', 'Spring', 'Kotlin', 'JSON', 'Android', 'NoSQL', 'Docker', 'Swift', 'iOS', 'API', 'Python']
# atributes = ['PHP', 'MySQL', 'JavaScript']
#
# entry = dict()
#
# for tec in tecnologies_list:
#     entry[tec] = 0
#
# for tec in atributes:
#     entry[tec] = 1
#
# print(atributes)
# # print(entry)

# import numpy as np
#
# atributes = [['a', 'b', 'c'], ['x', 'y', 'z']]
# atributes = [array for array in atributes]
# atributes = np.asarray(atributes)
#
# print(atributes)