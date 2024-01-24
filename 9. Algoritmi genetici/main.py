# Gavrilescu Raul - Adrian
# Laborator 9 - Algoritmi genetici

import random

def generare_cromozom():
    return [random.choice([0, 1]) for _ in range(10)]   # 0 - carte din primul pachet / 1 - carte din al doilea pachet

def raspuns_cromozom(cromozom):
    suma = 0
    produs = 1
    for i, bit in enumerate(cromozom):
        if bit == 1:
            produs *= i + 1
        elif bit == 0:
            suma += i + 1
    return suma, produs

def potrivire(suma_prim_pachet, produs_al_doilea_pachet):
    return abs(suma_prim_pachet - 36) + abs(produs_al_doilea_pachet - 360)

def evaluare_cromozomi(cromozomii):
    evaluari = []
    for cromozom in cromozomii:
        suma, produs = raspuns_cromozom(cromozom)
        evaluare = potrivire(suma, produs)
        evaluari.append((cromozom, evaluare))
    return evaluari

def selectie(evaluari, nr_cromozomi):
    total = sum(e_val[1] for _, e_val in evaluari)
    probabilitati_selectie = [e_val[1] / total for _, e_val in evaluari]
    selectie_indice = random.choices(range(nr_cromozomi), weights=probabilitati_selectie, k=nr_cromozomi)
    cromozomii_selectati = [evaluari[i][0] for i in selectie_indice]
    return cromozomii_selectati

def incrucisare(cromozom1, cromozom2):
    punct_incrucisare = random.randint(0, 9)
    nou_cromozom1 = cromozom1[:punct_incrucisare] + cromozom2[punct_incrucisare:]
    nou_cromozom2 = cromozom2[:punct_incrucisare] + cromozom1[punct_incrucisare:]
    return nou_cromozom1, nou_cromozom2

def mutatie(cromozom):
    pozitie_mutatie = random.randint(0, 9)
    cromozom[pozitie_mutatie] = 1 - cromozom[pozitie_mutatie]
    return cromozom

def operatii_genetice(cromozomii_selectati):
    cromozomi_noi = []

    for i in range(0, len(cromozomii_selectati), 2):
        cromozom1 = cromozomii_selectati[i]
        cromozom2 = cromozomii_selectati[i + 1]

        # Imperechere
        copil1, copil2 = incrucisare(cromozom1, cromozom2)

        # Mutatie
        copil1 = mutatie(copil1)
        copil2 = mutatie(copil2)

        cromozomi_noi.extend([copil1, copil2])

    return cromozomi_noi

def afisare_cel_mai_bun_cromozom(evaluari):
    cel_mai_bun_cromozom, evaluare = min(evaluari, key=lambda x: x[1])
    cel_mai_rau_cromozom, cea_mai_mare_evaluare = max(evaluari, key=lambda x: x[1])
    print("_" * 60)
    print("Cel mai bun cromozom:", cel_mai_bun_cromozom)
    print("Evaluare corespunzatoare:", evaluare)
    print("_"*60)
    print("\nCel mai rau cromozom:", cel_mai_rau_cromozom)
    print("Cea mai mare evaluare corespunzatoare:", cea_mai_mare_evaluare)
    print("_" * 60)


numar_cromozomi = 50
numar_generatii = 100

cromozomi = [generare_cromozom() for _ in range(numar_cromozomi)]

# Continua ciclul pana cand se indeplineste criteriul global de eroare( numarul de generatii.. )
for generatie in range(numar_generatii):
    evaluarile = evaluare_cromozomi(cromozomi)

# Afiseaza cel mai bun cromozom la sfarsit
afisare_cel_mai_bun_cromozom(evaluare_cromozomi(cromozomi))
