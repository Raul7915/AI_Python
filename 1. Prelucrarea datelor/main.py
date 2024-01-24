# Gavrilescu Raul - Adrian
# LABORATOR 1 - Prelucrarea Datelor

import csv
import numpy as np
myList = []
i = 0

def i_exercitiu():
    global i
    i += 1
    print("\n" + "-" * 18 + f" EXERCITIU {i} " + "-" * 18 + "\n")


def p_separator(arr, separator=" | "):
    print("[", f"{separator.join(map(str, arr))}", "]")


# EXERCITIUL 1
i_exercitiu()
with open(r'A:\FACULTATE\AI\1. Prelucrarea Datelor\iris.data') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if len(row) == 5:
            myList.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])
csvfile.close()

print("Fișierul de date Iris a fost incarcat.")


# EXERCITIU 2
i_exercitiu()
npArray = np.array(myList)
minim = np.min(npArray, axis=0)
maxim = np.max(npArray, axis=0)
medie = np.mean(npArray, axis=0)
mediana = np.median(npArray, axis=0)

print("Minimul pe fiecare coloana: ")
p_separator(minim, " | ")
print("Maximul pe fiecare coloana: ")
p_separator(maxim, " | ")
print("Valoarea medie pe fiecare coloana: ")
p_separator([round(val, 2) for val in medie], " | ")
print("Mediana pe fiecare coloana: ")
p_separator(mediana, " | ")


# EXERCITIU 3
i_exercitiu()
Xnorm = (npArray - minim) / (maxim - minim)
print("Valorile normalizate pe fiecare coloana: ")
for row in Xnorm:
    p_separator([f'{val:.4f}' for val in row], " | ")


# EXERCITIU 4
i_exercitiu()
ponderi = np.array([0.2, 1.1, -0.9, 1])

suma_ponderata = np.sum(npArray * ponderi, axis=1)
Coloana_sumei_ponderate = np.column_stack((npArray, suma_ponderata))

print('   DATELE DIN IRIS       |   Coloana sumei ponderate')
print('____________________________________________________')
for row in Coloana_sumei_ponderate:
    print("  ".join([f'{val:.2f}' for val in row[:4]]) + "   |           " + f'{row[4]:.2f}')


# Salvarea datelor din fisierul "iris.data", tip tabel:`    `
existing_data = np.genfromtxt("iris.data", delimiter=",", dtype="str")
suma_ponderata = np.round(suma_ponderata, 2)

# Adaugarea coloanei sumei ponderate intr-un fisier de tip tabel "iris_update.data"
new_data = np.column_stack((existing_data, suma_ponderata))
output_file = 'iris_updated.data'
np.savetxt(output_file, new_data, fmt='%s', delimiter=',')

print("\nColoana sumei ponderate a fost adaugată si salvata in tabelul 'iris_updated.data'.")


# EXERCITIU 5
i_exercitiu()
with open(r"A:\FACULTATE\AI\1. Prelucrarea Datelor\optdigits-orig.tra", "r") as file:
    lines = file.readlines()
data = []

i = 0
while i < len(lines):
    if lines[i].strip().isdigit():
        matrix = [list(map(int, line.strip()[:32])) for line in lines[i + 1:i + 33]]
        tabel = int(lines[i].strip())
        data.append((matrix, tabel))
        i = i + 33
    else:
        i = i + 1

scaled_data = []

for matrix, tabel in data:
    scaled_matrix = np.zeros((16, 16), dtype=np.uint8)

    for i in range(0, 32, 2):
        for j in range(0, 32, 2):
            fereastra_glisanta = [row[j:j + 2] for row in matrix[i:i + 2]]
            zero_count = sum(row.count(0) for row in fereastra_glisanta)

            if zero_count == 3 or zero_count == 4:
                scaled_matrix[i // 2, j // 2] = 0
            else:
                scaled_matrix[i // 2, j // 2] = 1

    scaled_data.append((scaled_matrix, tabel))

# Salvarea datelor intr-un nou fisier:
with open("matrix-16x16_output.tra", "w") as output_file:
    for scaled_matrix, tabel in scaled_data:
        for row in scaled_matrix:
            output_file.write("".join(map(str, row)) + "\n")
        output_file.write(" --" * 5 + "\n")

print("Fisierul imaginilor digitale, sub forma unei matrici binare de dimensiune 16x16 pixeli, a fost creat.\n\n")
