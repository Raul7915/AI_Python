# Gavrilescu Raul - Adrian
# LABORATOR 6 - TEMA 1 - Regula Perceptronului

import numpy as np
import csv

def sgn(val):
    return 1 if val > 0 else -1


lista = []
test_lista = []

# MEDIUL DE INSTRUIRE
with open(r'A:\FACULTATE\AI\6. T1 - Regula perceptronului\iris - instruire.data') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if len(row) == 5:
            if row[4] == "Iris-setosa":
                lista.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), 1])

            if row[4] == "Iris-versicolor":
                lista.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), -1])


w = np.random.randint(-1, 1, size=4)  # Ponderile
c = 0.000001
epoci_max = 100
error = 0

x_train = np.array([row[:-1] for row in lista])
y_train = np.array([row[-1] for row in lista])


for epoci in range(epoci_max):
    total_error = 0

    for i in range(len(x_train)):
        net = np.dot(x_train[i], w)
        y_pred = sgn(net)

        w = w + c * (y_train[i] - y_pred) * x_train[i]

        total_error += (y_train[i] != y_pred)  # True +1, False +0

    print(f'Epoca {epoci + 1} - Erori descoperite: {total_error}')

    if epoci == 99:
        print("_" * 35)

    if total_error <= error:

        print("_" * 35)
        print(f'    Instruirea a functionat!  ')
        print("_" * 35)
        break


# MEDIUL DE TESTARE
with open(r'A:\FACULTATE\AI\6. T1 - Regula perceptronului\iris - testare.data') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if len(row) == 5:
            if row[4] == "Iris-setosa":
                test_lista.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), 1])

            if row[4] == "Iris-versicolor":
                test_lista.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), -1])

x_test = np.array([row[:-1] for row in test_lista])
y_test = np.array([row[-1] for row in test_lista])

clasificari_corecte = 0
for i in range(len(x_test)):
    net = np.dot(x_test[i], w)
    y_pred = sgn(net)
    if y_pred == y_test[i]:
        clasificari_corecte += 1

acuratete = clasificari_corecte / len(x_test) * 100
print(f'Numarul de clasificari corecte: {clasificari_corecte}')
print(f' Acuratete: {round(acuratete, 2)}%')
