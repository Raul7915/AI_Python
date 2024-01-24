# Gavrilescu Raul - Adrian
# LABORATOR 3 - Metoda Gradientului

ex = 0
def i_exercitiu():
    global ex
    ex += 1
    print("\n\n\n" + "-" * 21 + f" EXERCITIU {ex} " + "-" * 21 + "\n")


error = 0.00001

# Diverse valori pentru c
c_values = [0.1, 0.01, 0.001]


# Exercitiu 1
i_exercitiu()

def f(x):
    return x ** 2 + 3 * x + 2

def det_f(x):
    return 2 * x + 3


def gradient1(x_initial, constanta, nr_iteratii):
    x = x_initial
    last_itr = 0
    for i in range(1, nr_iteratii + 1):
        last_itr = i - 1
        gradient_x = det_f(x)
        if x - (x - constanta * gradient_x) < error:
            break
        x -= constanta * gradient_x
        if i <= 5 or i == nr_iteratii:
            print(f"x{i} = {round(x, 2)}", f",   f(x) = {round(f(x), 2)}")
        elif i == 6:
            print(". \n. \n.")

    print(f"x{last_itr} = {round(x, 2)}", f", f(x) = {round(f(x), 2)}")
    print("-" * 72)
    print(f"Punctul de minim este: {x}", f", f(x) = {f(x)}")


for c in c_values:
    print(f"\nConstanta c este:  {c}")
    print("-" * 35)
    gradient1(x_initial=3, constanta=c, nr_iteratii=5000)
    print("-" * 72)


# Exercitiu 2
i_exercitiu()

def g(x, y):
    return x ** 2 + 2 * (y ** 2)

def det_g(x, y):
    det_x = 2 * x
    det_y = 4 * y
    return det_x, det_y

def gradient2(x_initial, y_initial, constanta, nr_iteratii):
    x = x_initial
    y = y_initial
    last_itr = 0
    for i in range(1, nr_iteratii + 1):
        last_itr = i - 1
        gradient_x, gradient_y = det_g(x, y)
        if x - (x - constanta * gradient_x) < error and y - (y - constanta * gradient_y) < error:
            break
        x -= constanta * gradient_x
        y -= constanta * gradient_y
        if i <= 5 or i == nr_iteratii:
            print(f"x{i} = {round(x, 2)},  y{i} = {round(y, 2)}, --->  g(x,y) = {round(g(x, y), 2)}")
        elif i == 6:
            print(". \n. \n.")

    print(f"x{last_itr} = {round(x, 2)},  y{last_itr} = {round(y, 2)}, --->  g(x,y) = {round(g(x, y), 2)}")
    print("-" * 70)
    print(f"Punctul de minim este: (x,y) - {x, y}\n      g(x,y) = {g(x, y)}")


c_values_2 = [0.01, 0.001, 0.0001]

for c in c_values_2:
    print(f"\nConstanta c este:  {c}")
    print("-" * 45)
    gradient2(x_initial=3, y_initial=2, constanta=c, nr_iteratii=30000)
    print("-" * 70)


# Exercitiu 3
i_exercitiu()

def h(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

def det_h(x, y):
    det_x = -2 * (1 - x) - 400 * x * (y - x ** 2)
    det_y = 200 * (y - x ** 2)
    return det_x, det_y


def gradient3(x_initial, y_initial, constanta, nr_iteratii):
    x = x_initial
    y = y_initial
    last_itr = 0
    for i in range(1, nr_iteratii + 1):
        last_itr = i
        gradient_x, gradient_y = det_h(x, y)
        if x - (x - constanta * gradient_x) < error and y - (y - constanta * gradient_y) < error:
            break
        x -= constanta * gradient_x
        y -= constanta * gradient_y
        if i <= 5 or i == nr_iteratii:
            print(f"x{i} = {x:.2f},  y{i} = {y:.2f}  --->  h(x,y) = {h(x, y):.2f}")
        elif i == 6:
            print(". \n. \n.")

    print(f"x{last_itr - 1} = {x:.2f},  y{last_itr - 1} = {y:.2f}, --->  h(x,y) = {h(x, y):.2f}")
    print("-" * 73)
    print(f"Punctul de minim este: (x,y) - {x, y}\n      h(x,y) = {h(x, y)}")


# Constante pentru Rosenbrock
c_values_rosenbrock = [0.001, 0.0001, 0.00001]

for c in c_values_rosenbrock:
    print(f"\nConstanta c este:  {c}")
    print("-" * 47)
    gradient3(x_initial=2, y_initial=2, constanta=c, nr_iteratii=50000)
    print("-" * 73)
