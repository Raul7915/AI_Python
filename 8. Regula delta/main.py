# Gavrilescu Raul - Adrian
# Laborator 8 - Regula Delta

import numpy as np

patterns = np.array([[45.0, 85.0],
                    [50.0,  43.0],
                    [40.0,  80.0],
                    [55.0,  42.0],
                    [200.0, 43.0],
                    [48.0,  40.0],
                    [195.0, 41.0],
                    [43.0,  87.0],
                    [190.0, 40.0]])

iesirile_dorite = np.array([[1, -1, -1],
                            [-1, 1, -1],
                            [1, -1, -1],
                            [-1, 1, -1],
                            [-1, -1, 1],
                            [-1, 1, -1],
                            [-1, -1, 1],
                            [1, -1, -1],
                            [-1, -1, 1]])


patterns_data = np.copy(patterns)

M = 2    # Numarul de intrari (fara intrarea suplimentara)
K = 3    # Numarul de perceptroni
c = 0.1  # Constanta de instruire
E_max = 0.001  # Eroarea maxima


w = np.random.uniform(-1, 1, (K, M + 1))    # (-1, 1, (3, 3))
coloana = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1])

minim = np.min(patterns, axis=0)
maxim = np.max(patterns, axis=0)

patterns[:, 0] = (patterns[:, 0] - minim[0]) / (maxim[0] - minim[0])
patterns[:, 1] = (patterns[:, 1] - minim[1]) / (maxim[1] - minim[1])

patterns = np.hstack((patterns, coloana.reshape(-1, 1)))


def activare_fct(net):
    return 2 / (1 + np.exp(-net)) - 1


def instruire(w_val, data, valori):
    epoci_max = 1000
    for epoca in range(epoci_max):
        E = 0
        for i in range(len(patterns)):
            output = np.array([activare_fct(np.dot(data[i], w_val[0, :])),
                               activare_fct(np.dot(data[i], w_val[1, :])),
                               activare_fct(np.dot(data[i], w_val[2, :]))])

            for j in range(K):
                if output[j] != valori[i][j]:
                    w_val[j] += c * (valori[i][j] - output[j]) * (1 - output[j] ** 2) * data[i]
                E += np.sum((valori[i][j] - output[j]) ** 2)

        if E < E_max:
            print("_" * 40)
            print("\n" + " " * 4 + " ! ! !" + " " * 5 + " EROARE " + " " * 5 + " ! ! !\n")
            print("_" * 40)
            break

    return w_val


def identificare_obj(output):
    rezultat = None

    if np.array_equal(np.round(output), [1, -1, -1]):
        rezultat = "SCAUN"
    elif np.array_equal(np.round(output), [-1, 1, -1]):
        rezultat = "MASA"
    elif np.array_equal(np.round(output), [-1, -1, 1]):
        rezultat = "PAT"

    return rezultat


def testare(w_val, dataset):
    for data, i in zip(dataset, range(len(dataset))):
        output = np.array([
             activare_fct(np.dot(data, w_val[0, :])),
             activare_fct(np.dot(data, w_val[1, :])),
             activare_fct(np.dot(data, w_val[2, :]))])
        print(f'\nPattern-ul {i + 1}: {patterns_data[i, :M].astype(int)}')
        print(output, "--->", np.round(output).astype(int), "-", identificare_obj(output))
        print("_" * 64)


w = instruire(w, patterns, iesirile_dorite)
testare(w, patterns)
