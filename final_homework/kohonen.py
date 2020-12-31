import numpy as np

"""
KOHONEN

SIGMA = Gaussian radius. It is the neighborhood selector
ALPHA = Learning rate constant
"""
# SIGMA = 8
# ALPHA = 0.5
# n_epocas = 100

# w_arrays = np.array([[9, 4, 3],
#                      [3, 5, 8],
#                      [1, 3, 5]])
#
# entry = np.array([4, 7, 1])

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


    # print('w_arrays of the Neural Network')
    # print(w_arrays)
    # print('Entry')
    # print(entry)
    # print('-' * 50)

    for n_epoca in range(n_epocas):

        """
        Step 1: Euclidian distances between entries weight array and network weight arrays 
        """

        euclidian_distances_1, winner_1, min_distance_1 = calc_euclidian_distance(entry=entry, w_arrays=w_arrays)
        # print(euclidian_distances_1, winner_1, min_distance_1)

        """
        Step 2: Euclidian distances between the winner network weigth array and all network weigth arrays
        """

        euclidian_distances_2, winner_2, min_distance_2 = calc_euclidian_distance(entry=winner_1, w_arrays=w_arrays)
        # print(euclidian_distances_2, winner_2, min_distance_2)

        """
        Step 3: Neighborhood
        """

        neighborhood = calc_neighborhood(euclidian_distances=euclidian_distances_2)
        # print(neighborhood)

        """
        Step 4: Network weights updating
        """

        # print('\nNew weights')

        w_arrays_2 = calc_wight_updating(w_arrays=w_arrays, ALPHA=ALPHA, neighborhood=neighborhood, entry=entry)
        # print(w_arrays_2)
        w_arrays = w_arrays_2

    return w_arrays
