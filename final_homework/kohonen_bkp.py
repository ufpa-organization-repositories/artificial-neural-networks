import numpy as np
import matplotlib.pyplot as plt

"""
KOHONEN

SIGMA = Gaussian radius. It is the neighborhood selector
ALPHA = Learning rate constant
"""
SIGMA = 8
ALPHA = 0.5
n_epocas = 3

w_arrays = np.array([[9, 4],
                     [3, 5],
                     [1, 3]])

entry = np.array([4, 7])

x = [array[0] for array in w_arrays]
y = [array[1] for array in w_arrays]
plt.scatter(x=x, y=y, label='Pesos iniciais',color='black')
plt.title('n_epocas: ' + str(n_epocas))

# x = entry[0]
# y = entry[1]
# plt.scatter(x=x, y=y, color='red')

plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.legend()
plt.plot()
# plt.title('Pesos inicializados aleatoriamente')
# plt.savefig('initial_network_weights.png')
# plt.show()
# plt.close()

def kohonen(w_arrays, entry, SIGMA, ALPHA, n_epocas):
    def calc_euclidian_distance(entry, w_arrays):
        euclidian_distances_aux = (entry - w_arrays) ** 2
        euclidian_distances_aux = sum(euclidian_distances_aux.T)
        euclidian_distances = euclidian_distances_aux ** (0.5)

        for i in range(euclidian_distances.__len__()):
            if euclidian_distances[i] == min(euclidian_distances):
                winner = w_arrays[i]
                min_euclidian_distance = euclidian_distances[i]
                return euclidian_distances, winner, min_euclidian_distance

    def calc_neighborhood(euclidian_distances):
        return np.e ** (-(euclidian_distances ** 2) / (2 * (SIGMA ** 2)))

    def calc_wight_updating(w_arrays, neighborhood,ALPHA, entry):
        return np.asarray([list(w_arrays[i] + ALPHA * (entry - w_arrays[i]) * neighborhood[i]) for i in range(len(w_arrays))])


    print('w_arrays of the Neural Network')
    print(w_arrays)
    print('Entry')
    print(entry)
    print('-' * 50)

    for n_epoca in range(n_epocas):

        """
        Step 1: Euclidian distances between entries weight array and network weight arrays 
        """

        euclidian_distances_1, winner_1, min_distance_1 = calc_euclidian_distance(entry=entry, w_arrays=w_arrays)
        print(euclidian_distances_1, winner_1, min_distance_1)

        """
        Step 2: Euclidian distances between the winner network weigth array and all network weigth arrays
        """

        euclidian_distances_2, winner_2, min_distance_2 = calc_euclidian_distance(entry=winner_1, w_arrays=w_arrays)
        print(euclidian_distances_2, winner_2, min_distance_2)

        """
        Step 3: Neighborhood
        """

        neighborhood = calc_neighborhood(euclidian_distances=euclidian_distances_2)
        print(neighborhood)

        """
        Step 4: Network weights updating
        """

        print('\nNew weights')

        w_arrays_2 = calc_wight_updating(w_arrays=w_arrays, ALPHA=ALPHA, neighborhood=neighborhood, entry=entry)
        # print(w_arrays_2)
        # w_arrays = w_arrays_2

        return w_arrays_2


for i in range (n_epocas):
    w_arrays = kohonen(w_arrays=w_arrays, entry=entry, SIGMA=SIGMA, ALPHA=ALPHA, n_epocas=n_epocas)
    print(w_arrays)

x = [array[0] for array in w_arrays]
y = [array[1] for array in w_arrays]
plt.scatter(x=x, y=y, label='Pesos finais',edgecolors='black', color='yellow')
plt.legend()
plt.plot()

x = entry[0]
y = entry[1]
plt.scatter(x=x, y=y, label='Entrada', color='red')
plt.legend()

plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
# plt.title('Pesos inicializados aleatoriamente')

plt.savefig('final.png')
plt.show()
plt.close()
