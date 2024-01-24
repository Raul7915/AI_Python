# Gavrilescu Raul - Adrian
# LABORATOR 5 - Algoritmul "Câștigătorul ia tot"

import numpy as np
import matplotlib.pyplot as plt

# Initializare prototipuri
w1 = np.random.rand(2) * 100
w2 = np.random.rand(2) * 100
w3 = np.random.rand(2) * 100

plt.scatter(w1[0], w1[1], color='lightcoral', marker='*', s=200, zorder=2)
plt.scatter(w2[0], w2[1], color='skyblue', marker='*', s=200, zorder=2)
plt.scatter(w3[0], w3[1], color='palegreen', marker='*', s=200, zorder=2)

print(w1, w2, w3)

# Definirea constantelor
c = 0.2
numar_epoci = 150

# Definirea pattern-urilor de instruire
puncte = np.array([[45, 85],
                   [50, 43],
                   [40, 80],
                   [55, 42],
                   [200, 43],
                   [48, 40],
                   [195, 41],
                   [43, 87],
                   [190, 40]])

# Instruirea castigatorul ia tot
for epoca in range(numar_epoci):
    for xi in puncte:
        # Determinarea castigătorului
        distante = [abs(np.linalg.norm(w1 - xi)), abs(np.linalg.norm(w2 - xi)), abs(np.linalg.norm(w3 - xi))]
        castigator = np.argmin(distante)

        # Actualizarea prototipului câștigător
        if castigator == 0:
            w1 = w1 + c * (xi - w1)
            plt.scatter(w1[0], w1[1], color='lightcoral', marker='4', s=80, zorder=1)
        elif castigator == 1:
            w2 = w2 + c * (xi - w2)
            plt.scatter(w2[0], w2[1], color='skyblue', marker='4', s=80, zorder=1)
        elif castigator == 2:
            w3 = w3 + c * (xi - w3)
            plt.scatter(w3[0], w3[1], color='palegreen', marker='4', s=80, zorder=1)

# Afișarea rezultatelor
print("Prototipul w1:", w1)
print("Pattern-uri asociate lui w1:")
for xi in puncte:
    if np.argmin([np.linalg.norm(xi - w1), np.linalg.norm(xi - w2), np.linalg.norm(xi - w3)]) == 0:
        print(xi)

print("\nPrototipul w2:", w2)
print("Pattern-uri asociate lui w2:")
for xi in puncte:
    if np.argmin([np.linalg.norm(xi - w1), np.linalg.norm(xi - w2), np.linalg.norm(xi - w3)]) == 1:
        print(xi)

print("\nPrototipul w3:", w3)
print("Pattern-uri asociate lui w3:")
for xi in puncte:
    if np.argmin([np.linalg.norm(xi - w1), np.linalg.norm(xi - w2), np.linalg.norm(xi - w3)]) == 2:
        print(xi)

# Afișare grafică
plt.scatter(puncte[:, 0], puncte[:, 1], s=40, label='Punctele', zorder=3)
plt.scatter(w1[0], w1[1], color='red', marker='*', s=200, label='Prototip w1', zorder=4)
plt.scatter(w2[0], w2[1], color='blue', marker='*', s=200, label='Prototip w2', zorder=4)
plt.scatter(w3[0], w3[1], color='green', marker='*', s=200, label='Prototip w3', zorder=4)

plt.legend()
plt.xlabel(' X ---> ')
plt.ylabel(' Y ---> ')
plt.title('Algoritmul "Castigatorul ia tot"')
plt.show()
