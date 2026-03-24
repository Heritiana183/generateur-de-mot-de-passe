# Générateur de mdp aléatoire

import random

def welcome():
    print("Welcome to my password auto-generate")
    print("The minimum length is 4")


def one_number():
    return random.randint(0, 9)


def special_character():
    return random.choice(["&", "#", "@", "$"])


def alphabet():
    return random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])    


def main():
    welcome()
    while True:
        length_request = int(input("What will the desired length be? : "))
        print("Length = {}".format(length_request))
        password = []
        if length_request < 4:
            print("Number not valide, must be 4 or more")
            continue
        elif length_request > 100:
            print("Too long")
            continue
        #A propos du nombre
        number_request = input("Do you need number inside?(Y/n)").lower()
        if number_request == "y":
            if length_request < 6:
                print("You can enter only 1 number")
            elif length_request >= 6 and length_request < 10:
                print("You can enter 3 numbers")
            elif length_request >= 10 and length_request < 20:
                print("You can enter 5 numbers")
            elif length_request >= 20:
                print("You can enter 10 numbers")
            while True:
                req_number = int(input("How many is the number? : "))
                if length_request < 6:
                    if req_number != 1:
                        print("You have to enter 1")
                        continue
                    else:
                        break
                elif length_request >= 6 and length_request < 10:
                    if req_number > 3 or req_number < 1:
                        print("Maximum is 3 and minimum is 1")
                        continue
                    else:
                        break
                elif length_request >= 10 and length_request < 20:
                    if req_number > 5 or req_number < 1:
                        print("Maximum is 5 and minimum is 1")
                        continue
                    else:
                        break
                elif length_request >= 20:
                    if req_number > 10 or req_number < 1:
                        print("Maximum is 10 and minimum is 1")
                        continue
                    else:
                        break
            for i in range(0, req_number, +1):
                password += [str(one_number())]
        elif number_request != "y":
            password = password
        #A propos du special caractère
        print("Our specials characters are :", " ".join(["&", "#", "@", "$"]))
        special_request = input("Include special characters?(Y/n)").lower()
        if special_request == "y":
            if length_request < 6:
                print("You can enter only 1 special character")
            elif length_request >= 6 and length_request < 10:
                print("You can enter 2 specials characters")
            elif length_request >= 10 and length_request < 20:
                print("You can enter 3 specials characters")
            elif length_request >= 20:
                print("You can enter 5 specials characters")
            while True:
                req_special = int(input("How many special character? : "))
                print("You want {}".format(req_special), "special character")
                if length_request < 6:
                    if req_special != 1:
                        print("You have to enter 1")
                        continue
                    else:
                        break
                elif length_request >= 6 and length_request < 10:
                    if req_special > 3 or req_special < 1:
                        print("Maximum is 2 and minimum is 1")
                        continue
                    else:
                        break
                elif length_request >= 10 and length_request < 20:
                    if req_special > 5 or req_special < 1:
                        print("Maximum is 3 and minimum is 1")
                        continue
                    else:
                        break
                elif length_request >= 20:
                    if req_special > 5 or req_special < 1:
                        print("Maximum is 5 and minimum is 1")
                        continue
                    else:
                        break
            for i in range(0, req_special, +1):
                password.append(special_character())
        elif special_request != "y":
            password = password
        #A propos du Majuscule et des lettres
        upper_request = input("Include upper letter?(Y/n)").lower() 
        rest_length = length_request - len(password)#Reste de la longueur dispo
        array_letters = []
        for i in range(0, rest_length, +1):
            array_letters += [alphabet()]
        if upper_request == "y":
            if length_request < 10:
                print("You can make only 1 upper case")
            elif length_request >= 10:
                print("You can make 3 upper cases")
            if length_request < 10:
                letter_to_upper = random.choice(array_letters)
                for i in range(0, len(array_letters), +1):
                    if letter_to_upper == array_letters[i]:
                        array_letters[i] = letter_to_upper.upper()
                        break
                password += array_letters
            elif length_request >= 10:
                while True:
                    req_upper = int(input("How many upper?(Max 3, min 1) : "))
                    if req_upper > 3 or req_upper < 1:
                        print("Invalide number, try again")
                        continue
                    else:
                        break
                array_upper_letters = []
                for i in range(0, req_upper, +1):
                    letter_to_upper = random.choice(array_letters)
                    array_upper_letters += [letter_to_upper.upper()]
                rest_length2 = len(array_upper_letters)
                array_letters += array_upper_letters
                del array_letters[0:rest_length2]
                password += array_letters
        elif upper_request != "y":
            password += array_letters
        random.shuffle(password)
        password = "".join(password)
        print("Your password is : {}".format(password))
        print()
        after_result = input("Do you want this or make a new one?(Y/n)").lower()
        if after_result == "y":
            continue
        elif after_result != "y":
            print("It was a pleasure!")
            break


main()