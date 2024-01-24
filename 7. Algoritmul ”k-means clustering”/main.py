# Gavrilescu Raul - Adrian
# LABORATOR 7 - TEMA 2 - Algoritmul "K-Means Clustering"

import numpy as np
import matplotlib.pyplot as plt

puncte = np.array([[45, 85],
                   [50, 43],
                   [40, 80],
                   [55, 42],
                   [200, 43],
                   [48, 40],
                   [195, 41],
                   [43, 87],
                   [190, 40]])

# culori = ['yellow', 'lime', 'orange']

global tabel_val  # Variabila definita global pentru a scapa de "WARNING-ul":
# "Local variable 'tabel_val' might be referenced before assignment"

def k_means_clustering(punctele, k_val, max_iteratii=100):
    global tabel_val
    centroizi_val = np.random.rand(k_val, 2) * 100

    plt.scatter(puncte[:, 0], puncte[:, 1], s=70, color='blue', label='Punctele', zorder=1)
    plt.scatter(centroizi_val[:, 0], centroizi_val[:, 1], color='red', marker='*', s=200,
                label='Centroizi initiali', zorder=2)

    for val in range(max_iteratii):
        distanta = np.linalg.norm(punctele - centroizi_val[:, np.newaxis], axis=2)
        # plt.scatter(centroizi_val[:, 0], centroizi_val[:, 1], color=culori[val-1], marker='4', s=100,
        # label=f'Pasul {val+1}', zorder=6)
        tabel_val = np.argmin(distanta, axis=0)

        centroizi_last = centroizi_val.copy()

        for j in range(k_val):
            clustere_val = punctele[tabel_val == j]
            if len(clustere_val) > 0:
                centroizi_val[j] = np.mean(clustere_val, axis=0)

        if np.all(centroizi_last == centroizi_val):
            break

    return centroizi_val, tabel_val


k = 3
centroizi, tabel = k_means_clustering(puncte, k)


print("")
# Afisarea rezultatelor
for i in range(k):
    clustere = puncte[tabel == i]
    print(f'Cluster {i + 1} - Centroid:', np.round(centroizi[i], 2), f'\n Puncte:\n {clustere}')
    print("_" * 40)

plt.scatter(centroizi[:, 0], centroizi[:, 1], marker='*', s=120, color='green', label='Centroizi', zorder=5)
plt.xlabel(' X ---> ')
plt.ylabel(' Y ---> ')
plt.title('Algoritmul "K-Means Clustering"')
plt.legend()
plt.show()
