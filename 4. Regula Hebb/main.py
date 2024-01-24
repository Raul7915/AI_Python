# Gavrilescu Raul - Adrian
# LABORATOR 4 - Regula Hebb

import numpy as np

ex = 0

def i_exercitiu():
    global ex
    ex += 1
    print("\n" + "-" * 21 + f" EXERCITIU {ex} " + "-" * 21 + "\n")

def title(data):
    print("-" * 43)
    print(data)
    print("-" * 43)

def sgn(net):
    return 1 if net >= 0 else -1

# FUNCTIE BIPOLARA CONTINUA f(net) = (2 / 1 + exp^-(lan*net))-1, landa>0
def bipolara_continua(net, landa):
    if landa > 0:
        return (2 / (1 + np.exp(-landa * net))) - 1


# Exercitiu 1
i_exercitiu()

x = np.array([[1, -2, 1.5, 0],
              [1, -0.5, -2, -1.5],
              [0, 1, -1, 1.5]])

c = 1

w1 = np.array([1, -1, 0, 0.5])
net1 = np.dot(w1, x[0])

w2 = w1 + sgn(net1) * x[0]
net2 = np.dot(w2, x[1])

w3 = w2 + sgn(net2) * x[1]
net3 = np.dot(w3, x[2])

w4 = w3 + sgn(net3) * x[2]

w_values = [w1, w2, w3, w4]
net_values = [net1, net2, net3]


title("PONDERI")
for i, w_i in enumerate(w_values, start=1):
    print(f'w{i}: {w_i}')

print(" ")
title(" NET ")
for i, net_i in enumerate(net_values, start=1):
    print(f'net{i}: {net_i}')


print("")
title(" FUNCTIE BIPOLARA CONTINUA ")
print("net1 = ", net1)
print(f"f(net1) = ", np.round(bipolara_continua(net1, 1), 3))
w2 = np.round(np.dot(bipolara_continua(net1, 1), x[0]) + w1, 3)
print("w1_update: ", w2)
net2 = np.round(np.dot(w2, x[1]), 3)
print("\nnet2 = ", net2)
print("f(net2) = ", np.round(bipolara_continua(net2, 1), 3))
w3 = np.round(np.dot(bipolara_continua(net2, 1), x[1]) + w2, 3)
print("w2_update: ", w3)
net3 = np.round(np.dot(w3, x[2]), 3)
print("\nnet3 = ", net3)
print("f(net3) = ", np.round(bipolara_continua(net3, 1), 3))
w4 = np.round(np.dot(bipolara_continua(net3, 1), x[2]) + w3, 3)
print("w3_update: ", w4, "\n")


# Exercitiu 2
i_exercitiu()
print("")

y = np.array([[1, -2],
              [0, 1],
              [2, 3],
              [1, -1]])

w1 = np.array([1, -1])
net1 = np.dot(w1, y[0])

w2 = w1 + sgn(net1) * y[0]
net2 = np.dot(w2, y[1])

w3 = w2 + sgn(net2) * y[1]
net3 = np.dot(w3, y[2])

w4 = w3 + sgn(net3) * y[2]
net4 = np.dot(w4, y[3])

w5 = w4 + sgn(net4) * y[3]

w_values = [w1, w2, w3, w4, w5]
net_values = [net1, net2, net3, net4]

title(" PONDERI ")
for i, w_i in enumerate(w_values, start=1):
    print(f'w{i}: {w_i}')
print("")
title(" NET ")
for i, net_i in enumerate(net_values, start=1):
    print(f'net{i}: {net_i}')

print("")
title("FUNCTIE BIPOLARA CONTINUA")
print("net1 = ", net1)
print(f"f(net1) = ", np.round(bipolara_continua(net1, 1), 3))
w2 = np.round(np.dot(bipolara_continua(net1, 1), y[0]) + w1, 3)
print("w1_update: ", w2)
net2 = np.round(np.dot(w2, y[1]), 3)
print("\nnet2 = ", net2)
print("f(net2) = ", np.round(bipolara_continua(net2, 1), 3))
w3 = np.round(np.dot(bipolara_continua(net2, 1), y[1]) + w2, 3)
print("w2_update: ", w3)
net3 = np.round(np.dot(w3, y[2]), 3)
print("\nnet3 = ", net3)
print("f(net3) = ", np.round(bipolara_continua(net3, 1), 3))
w4 = np.round(np.dot(bipolara_continua(net3, 1), y[2]) + w3, 3)
print("w3_update: ", w4)
net4 = np.round(np.dot(w4, y[3]), 3)
print("\nnet4 = ", net4)
print("f(net4) = ", np.round(bipolara_continua(net4, 1), 3))
w5 = np.round(np.dot(bipolara_continua(net4, 1), y[3]) + w4, 3)
print("w4_update: ", w5)
