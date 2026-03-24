import random

'''
Jeu : Devine le mot (version améliorée)

Mot prédéfini
L utilisateur devine lettre par lettre
Affiche la progression _ _ a _ _
6 erreurs maximum
Affiche les lettres déjà proposées
Interdit de répéter une lettre déjà testée
'''

def welcome():
    print("Bienvenue dans mon petit jeu")


def menu():
    print("Chosissez : ")
    print("1 - Jouer")
    print("2 - Quitter")
    req = int(input("Entrer : "))
    #len(req) == 1
    return req


def words():
    list = ["bourgeois", "ecureuil", "creneaux", "cuillere", "chirurgien", "grenouille", "grele", "heureux",
    "inaugure", "oiseaux", "poireaux", "quincaillerie", "ratatouille", "serrurier", "trottinette", "vinaigrette", "ecailles",
    "surgeles", "tonneau", "assassin"]
    return random.choice(list)


def to_underscore(x):
    new = ""
    for i in range(0, len(x), +1):
        new += "_"
    return new


def win():
    print("Felicitation vous avez gagne")


def defeat():
    print("Malheuresement, vous n'avez pas trouve")


def bye():
    print("Merci et a la prochaine")


def main():
    print("")
    welcome()
    print("")
    while True:
        z = menu()
        print("")
        z = str(z)
        if len(z) != 1:
            print("Entrer 1 seul chiffre")
            print("")
            continue
        z = int(z)
        if z == 2:
            bye()
            break
        elif z != 1:
            print("Veuillez choisir entre 1 ou 2")
            print("")
            continue
        elif z == 1:
            while True: #Le jeu commence
                x = words() #Le mot
                y = to_underscore(x) 
                error_count = 0
                show = ""
                print("Entrer seulement 1 seule lettre")
                print(y)
                print("")
                new_y = list(y) #Array  
                while True:
                    answer = input("Entrer : ").lower()
                    if answer in show:
                        print("Vous avez déja entré cette lettre, réessayez")
                        continue
                    show += answer + " "
                    if len(answer) != 1:
                        print("Dois seulement être 1 seule charactère")
                        continue
                    count = 0
                    for i in range(0, len(x), +1): #Verification du lettre
                        if answer == x[i]:
                            count += 1
                            new_y[i] = answer    
                    print("".join(new_y))
                    print("")
                    if count == 0:
                        error_count += 1
                        if error_count == 6:
                            print("")
                            defeat()
                            print("La reponse etait : {}".format(x))
                            break
                    print("Erreur = {}".format(error_count))        
                    print("Lettre deja entrer : {}".format(show))
                    print("")
                    if "".join(new_y) == x:
                        print("")
                        win()
                        break
                print("") 
                ask = input("Rejouer?(O/n) ").lower()
                print("")
                if ask == "o":
                    continue
                elif ask != "o":
                    bye()
                    break


main()  
