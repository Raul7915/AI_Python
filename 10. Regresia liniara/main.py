# Gavrilescu Raul - Adrian
# LABORATOR 10 - TEMA 3 - Regresia Liniara


import pandas as pd
import matplotlib.pyplot as plt

# Citirea datelor din fisier
data_file = pd.read_csv('Salary_Data.csv')

def descenta_gradient(x, y, w1_initial=0, w2_initial=0, c=0.01, iteratii=10000):
    n = float(len(y))
    w1, w2 = w1_initial, w2_initial

    for i in range(iteratii):
        y_prevazut = (w1 * x) + w2
        # E = 1 / 2 * n * sum(y - y_prevazut) ** 2
        # print(E)
        dE_dw1 = (-1 / n) * sum(x * (y - y_prevazut))
        dE_dw2 = (-1 / n) * sum(y - y_prevazut)
        w1 -= (c * dE_dw1)
        w2 -= (c * dE_dw2)

        # print("W1 :", (round(w1, 3)))
        # print(round(w2, 2))

    return w1, w2


# Aplicarea metodei gradientului
w1_val, w2_val = descenta_gradient(data_file['YearsExperience'], data_file['Salary'], c=0.01, iteratii=1000)

# Graficul
plt.scatter(data_file['YearsExperience'], data_file['Salary'], color='blue', label='Date intrare')
plt.plot(data_file['YearsExperience'], (w1_val * data_file['YearsExperience'] + w2_val),
         color='red', label='Dreapta de regresie')
plt.xlabel('YearsExperience [x] ---> ')
plt.ylabel('Salary [y] ---> ')
plt.title('Regresie liniara')
plt.legend()
plt.show()

CY = '\033[93m'
END = '\033[0m'

# Afisarea in consola
print()
print(f'Dreapta de regresie:  𝑦̅ = ' + CY + f'{round(w1_val, 3)}' + END + "𝑥 + " + CY + f'{round(w2_val, 3)}' + END)
print("-" * 45)
print(CY + "w1" + END + f" = {w1_val}")
print(CY + "w2" + END + f" = {w2_val}")
print("-" * 45)
