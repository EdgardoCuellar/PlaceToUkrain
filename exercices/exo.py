import time

def main():
    exo1()

# calcul IMC
def exo1():
    taille = float(input("Taille en cm ?"))
    poids = float(input("Masse en kg ?"))
    imc = poids / (taille * taille)
    print("Votre IMC est de : ", imc)

# trois premiers char
def exo2():
    string = input("String ?")
    print(string[:3])

# trois derniers char
def exo3():
    string = input("String ?")
    print(string[-3:])

# invert varibles
def exo4():
    a = input("a: ")
    b = input("b: ")
    a, b = b, a
    print("a = ", a, "b = ", b)

# cuillere à soupe en grammes
def exo5():
    gm = int(input("Nombre de grammes de sucre ?"))
    cs = gm / 25
    print("Pour " + str(gm) + " grammes de sucre, il faut " + str(cs) + " cuillères à soupe.")


def exo6():
    notes = []
    for i in range(3):
        notes.append(float(input("Note " + str(i) + "?")))
    print(notes)


def exo7():
    notes = []
    for i in range(3):
        notes.append(float(input("Note " + str(i) + "?")))
    notes.append(float(input("Note à ajouter ?")))
    print(notes)


def exo8():
    notes = []
    for i in range(3):
        notes.append(float(input("Note " + str(i) + "?")))
    notes.append(float(input("Note à ajouter ?")))
    notes[1] += 1
    print(notes)


def exo9():
    notes = []
    for i in range(3):
        notes.append(float(input("Note " + str(i) + "?")))
    notes.append(float(input("Note à ajouter ?")))
    notes[1] += 1
    print(notes)
    print("Moyenne : ", sum(notes) / len(notes))


def exo10():
    n = int(input("Number ?"))
    for i in range(n):
        print(i)


def exo11():
    numbers = [5,62,7,652,56,156,12]
    print(min(numbers))


def exo12():
    numbers1 = [5,62,7,652,56,156,12]
    numbers2 = [5,62,7,652,56,156,12, 1, 2, 3]
    common = []
    for i in numbers1:
        if i in numbers2:
            common.append(i)
    print(common)

def exo13():
    birth_year = int(input("Année de naissance ?"))
    print("Age : ", time.localtime().tm_year - birth_year)


def exo14():
    birth_year = int(input("Année de naissance ?"))
    birth_month = int(input("Mois de naissance ?"))
    birth_day = int(input("Jour de naissance?"))
    age = time.localtime().tm_year - birth_year
    if time.localtime().tm_mon < birth_month:
        age -= 1
    elif time.localtime().tm_mon == birth_month:
        if time.localtime().tm_mday < birth_day:
            age -= 1
            
    print("Age : ", age, "ans, ", time.localtime().tm_mon - birth_month, "mois, ", time.localtime().tm_mday - birth_day, "jours")


if __name__ == "__main__":
    main()