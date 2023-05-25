def create_vector():
    vector = [int(input("Quelle valeur pour le vecteur ? \n"))]
    vector *= int(input("Combien de ligne ? \n"))
    return vector


def print_vector(vector):
    print(vector)


def create_multiple_vector():
    n = input("Combien de vecteurs voulez vous ? \n")
    data = []
    for i in n:
        data.append(create_vector())

    data.append(n)
    return data


def

data = create_multiple_vector()

i = 0

for i in 1 :
    print_vector(data[i])



