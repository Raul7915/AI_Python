# Gavrilescu Raul - Adrian
# LABORATOR 2 - Preliminarii

from itertools import product
import numpy as np

myList = []
ex = 0


def i_exercitiu():
    global ex
    ex += 1
    print("\n" + "-" * 21 + f" EXERCITIU {ex} " + "-" * 21 + "\n")


def sgn(val):
    return 1 if val >= 0 else 0


def sgn1(val):
    return 1 if val >= 0 else -1


# EXERCITIUL 1
i_exercitiu()

x = np.array([2, 1, 2])
y = np.array([1, -1, 4])
x_lungime = 0
y_lungime = 0

produs_scalar = np.dot(x, y)

for val_x, val_y in zip(x, y):
    x_lungime += val_x ** 2
    y_lungime += val_y ** 2

x_lungime = np.sqrt(x_lungime)
y_lungime = np.sqrt(y_lungime)

cos = produs_scalar / (x_lungime * y_lungime)

print("Produs Scalar: ", produs_scalar)
print("Lungimea vectorului x: ", x_lungime)
print("Lungimea vectorului y: ", np.round(y_lungime, 2))
print("Cosinusul unghiului dintre x și y: ", np.round(cos, 2))

# EXERCITIUL 2
i_exercitiu()

pondere = np.array([1, 1, 1])
varfuri_cub = np.array([
    [-1, -1, -1],
    [-1, -1, 1],
    [-1, 1, -1],
    [-1, 1, 1],
    [1, -1, -1],
    [1, -1, 1],
    [1, 1, -1],
    [1, 1, 1]
])

suma_ponderata = np.sum(varfuri_cub * pondere, axis=1)

print("Clasificator realizat cu o singura unitate:")

for i, suma in enumerate(suma_ponderata):
    if suma > 0:
        print(f" P{i + 1}: sum_pond:  {suma} ---> sgn{varfuri_cub[i]}:  {sgn1(suma)} ---> Clasa 1")
    elif suma < 0:
        print(f" P{i + 1}: sum_pond: {suma} ---> sgn{varfuri_cub[i]}: {sgn1(suma)} ---> Clasa 2")

# EXERCITIUL 3
i_exercitiu()

# a/ Verificați care este răspunsul neuronului pentru datele de antrenare.
print("A. ")
ponderi = np.array([-0.14, 0.06, -0.28, -0.93, -0.08, 0.28, -0.64, 0.47, -0.85])

matrix_3x3 = np.array([
    [1, 1, 1, 1, 0, 1, 1, 1, 1],    # 0
    [0, 1, 0, 1, 0, 1, 0, 1, 0],    # 0
    [0, 1, 0, 0, 1, 0, 0, 1, 0],    # 1
    [1, 1, 0, 0, 1, 0, 0, 1, 0],    # 1
])

suma_ponderata = np.sum(matrix_3x3 * ponderi, axis=1)
print(suma_ponderata)

for i, suma in enumerate(suma_ponderata):
    print(f" Matricea {i + 1}: {sgn(suma)} ")

# b/ Folosiți acest neuron pentru a face predicții cu variante perturbate ale cifrelor 0 și 1.
#    Care este rata de clasificare corectă?
print("\nB. ")
# Matrici care reprezinta cifra 0
matrix_0 = np.array([               # 111  010
    [1, 1, 1, 1, 0, 1, 1, 1, 1],    # 101  101
    [0, 1, 0, 1, 0, 1, 0, 1, 0]])   # 111  010

# Matrici care reprezinta cifra 1
matrix_1 = np.array([               # 010  110
    [0, 1, 0, 0, 1, 0, 0, 1, 0],    # 010  010
    [1, 1, 0, 0, 1, 0, 0, 1, 0]])   # 010  010


def procentaj_asemanare(matrice1, matrice2, matrice3):
    elemente_identice = np.sum(matrice1 == matrice2, axis=1)
    total_elemente = matrice1.size
    procentaj0 = [round(val, 2) for val in ((elemente_identice / total_elemente) * 100)]
    elemente_identice = np.sum(matrice1 == matrice3, axis=1)
    total_elemente = matrice1.size
    procentaj1 = [round(val, 2) for val in ((elemente_identice / total_elemente) * 100)]
    # print(procentaj0, procentaj1)
    if procentaj0 > procentaj1:
        return 0  # Matricea este clasificata ca un 0, deoarece procentajul este mai mare pentru matrix_0
    else:
        return 1  # Matricea este clasificata ca un 1, deoarece procentajul este mai mare pentru matrix_1


# matriceX = np.array([0, 1, 1, 1, 0, 1, 1, 1, 1])
# procentaj_asemanare(matriceX, matrix_0, matrix_1)

combinatii_1_0 = np.array(list(product([0, 1], repeat=9)))

X = 0
Y = 0

for i in range(2 ** 9):
    matrice_rand = combinatii_1_0[i]
    result = procentaj_asemanare(matrice_rand, matrix_0, matrix_1)
    suma_ponderata = np.sum(matrice_rand * ponderi)
    if result == sgn(suma_ponderata):  # Verifica egalitatea dintre variantele perturbate clasificate ca cifrele
        X = X + 1  # 0 și 1 si functia de activare treapta dupa clasificarea sumei ponderate
    else:  # obtinute din datele de intrare * ponderile alese aleator
        Y = Y + 1

print("Variantele egale: ", X)
print("Variantele ''eronate'': ", Y)

rata_clasificare_corecta = X / (X + Y)
print(f'\nRata de clasificare corecta: {rata_clasificare_corecta * 100:.2f}%')


# EXERCITIUL 4
i_exercitiu()

def retea_memorie(o1, o2, o3, idx):
    if o1 == 0:
        o1 = -1
    if o2 == 0:
        o2 = -1
    if o3 == 0:
        o3 = -1
    suma_ponderata1 = o2 * 1 + o3 * (-1)
    suma_ponderata2 = o1 * 1 + o3 * (-1)
    suma_ponderata3 = o1 * (-1) + o2 * (-1)

    out1 = sgn1(suma_ponderata1)
    out2 = sgn1(suma_ponderata2)
    out3 = sgn1(suma_ponderata3)
    if suma_ponderata1 == 0:
        out1 = o1
    if suma_ponderata2 == 0:
        out2 = o2
    if suma_ponderata3 == 0:
        out3 = o3

    print(f"Iesirea urmatoare din cazul {idx}:", out1, out2, out3)
    return out1, out2, out3


def iesire_stabila(o1, o2, o3):
    output1 = retea_memorie(o1, o2, o3, 1)
    output2 = retea_memorie(-o1, o2, o3, 2)
    output3 = retea_memorie(o1, -o2, o3, 3)
    output4 = retea_memorie(o1, o2, -o3, 4)

    if output1 == output2 == output3 == output4:
        print("-" * 40)
        print("** Iesire stabila a memoriei **")
        print("-" * 40)


for index, point in enumerate(varfuri_cub, start=0):
    print(f"\nPunctul {index} -   P{index} {point}")
    iesire_stabila(*point)
