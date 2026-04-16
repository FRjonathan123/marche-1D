import random
import matplotlib.pyplot as plt


nb_pas = 1000
position = 0

list_nb_pas = []
list_position = []


for i in range(nb_pas):
    position += random.choice([1, -1])
    # si pile = avancer de 1 | si face = reculer de 1
    list_nb_pas.append(i)
    list_position.append(position)



plt.plot(list_nb_pas, list_position)
plt.title("La marche aléatoire")
plt.xlabel("nombre de pas")
plt.ylabel("position")

plt.show()
