# Gavrilescu Raul - Adrian
# Laborator 11 - Algoritmul “Backpropagation of error”


import numpy as np

# Datele de instruire
patterns = np.array([
    [45, 85, -1],
    [50, 43, -1],
    [40, 80, -1],
    [187, 107, -1],
    [55, 42, -1],
    [200, 43, -1],
    [48, 40, -1],
    [195, 41, -1],
    [43, 87, -1],
    [192, 105, -1],
    [190, 40, -1],
    [188, 100, -1]
], dtype=float)

patterns1 = np.array([
    [45, 85, -1],
    [50, 43, -1],
    [40, 80, -1],
    [187, 107, -1],
    [55, 42, -1],
    [200, 43, -1],
    [48, 40, -1],
    [195, 41, -1],
    [43, 87, -1],
    [192, 105, -1],
    [190, 40, -1],
    [188, 100, -1]
], dtype=float)

op_val_global = None
dp_val_global = None


# Functia de activare continua bipolara
def activare(neta):
    return (2 / (1 + np.exp(-neta))) - 1


# Derivata functiei de activare
def derivata_activare(y):
    return 0.5 * (1 - y ** 2)


# Algoritmul de backpropagation
def backpropagation(x, d, v, w, c, e_max, epoci):
    global op_val_global
    global dp_val_global

    J = len(v)
    K = len(w)
    E = 0

    op_val_global = np.zeros(len(x))  # Initializeaza array pentru a stoca toate valorile op
    dp_val_global = np.zeros(len(x))  # Initializeaza array pentru a stoca toate valorile dp

    for epoca in range(epoci):
        for p in range(len(x)):
            # Propagarea inainte
            y1 = activare(np.sum(np.dot(v[0], x[p])))
            y2 = activare(np.sum(np.dot(v[1], x[p])))
            y3 = activare(np.sum(np.dot(v[2], x[p])))
            yp = np.array([y1, y2, y3, -1])
            op = activare(np.sum(np.dot(w, yp)))

            # Calcularea erorii
            delta_o = (d[p] - op) * derivata_activare(op)
            delta_y = 0.5 * (1 - yp ** 2) * np.sum(np.dot(delta_o, w))

            # Actualizarea ponderilor pentru stratul ascuns
            for j in range(J):
                v[j] += c * delta_y[j] * x[p]

            # Actualizarea ponderilor pentru stratul de iesire
            for k in range(K):
                w[k] += c * delta_o * yp[k]

            # Calcularea erorii cumulate
            E += 0.5 * (d[p] - op) ** 2

            # Actualizarea valorilor globale
            op_val_global[p] = op
            dp_val_global[p] = d[p]

        print(f'Epoca {epoca + 1}, Eroare: {E}')

        if E < e_max:
            break
        E = 0

    return v, w


# Normalizarea datelor
npArray = patterns[:, :2]
minim = np.min(npArray, axis=0)
maxim = np.max(npArray, axis=0)
npArray = (npArray - minim) / (maxim - minim)
patterns[:, :2] = npArray

# Iesirile dorite
iesiri_dorite = np.array([1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1])

# Initializare parametri retea
J = 3
K = 1
v_val = np.random.rand(J, len(patterns[0]))
w_val = np.random.rand(K, J + 1)
c = 0.1
e_max = 0.01
epoci = 5000

# Antrenare retea
ponderi_ascunse_finale, ponderi_iesire_finale = backpropagation(patterns, iesiri_dorite, v_val, w_val, c, e_max, epoci)


# Afisare valorilor obtinute pentru op si dp pentru fiecare pattern
print("")
print("_" * 80)

for p in range(len(patterns)):
    print(f'Pattern {p + 1:2d}: {str(patterns1[p]):<20} -->  iesirea: {op_val_global[p]:.4f}  '
          f'-  iesirea dorita: {dp_val_global[p]:.1f}')

print("_" * 80)

# Afisare ponderi finale pentru stratul ascuns si de iesire
print("\n  Ponderi finale pentru stratul ascuns:")
print(ponderi_ascunse_finale)
print("\n  Ponderi finale pentru stratul de iesire:")
print("\t", ponderi_iesire_finale)
