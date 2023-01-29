"""import random
num = random.random()
print(num)"""

import random

tour = 0
score = 0
tour_max = 4

def calcul(a, b):
    resultat = a * b
    return resultat


def comparaison(score):
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    reponse = int(input(f"Quel est le résultat de l'opération suivante : {num1} x {num2} ?"))
    resultat_theorique = calcul(num1, num2)
    if resultat_theorique == reponse:
        score += 1
        print(f"Bonne réponse. Votre score est de {score}/{tour}.")
    else:
        print(f"Mauvaise réponse. Votre score est de {score}/{tour}.")
    return score


while tour < tour_max:
    tour += 1
    score = comparaison(score)

"""def calcul(num1, num2):
    essaie = int(input(f"Quel est le résultat de l'opération suivante : {num1} x {num2} ?"))
    resultat = num1 * num2
    tour += 1
    if essaie == resultat:
        win = True
        print("Bonne réponse.")
    else:
        win = False
        print("Mauvaise réponse.")




while tour <= 4:
    calcul(num1, num2)
    tour += 1"""
