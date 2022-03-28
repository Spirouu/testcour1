import hashlib
from itertools import product

def crack():
    global hash_mdp

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}:;\"'<>,.?/\\"
    numb = "1234567890"
    longueur = 2
    compteur=0
    find = False

    while find == False:
        liste = [''.join(i) for i in list(product(alphabet, repeat=longueur))]
        for pwd in liste:
            print(pwd)
            compteur += 1
            if hash(pwd) == hash_mdp:
                print("\n\n\n\n\n\n The password is : ", pwd,", for this there was ", compteur, "combinations tried")
                exit()
                find = true
        longueur += 1


def hash(x):
    hash1=x
    plaintext = hash1.encode()
    d = hashlib.sha256(plaintext)
    hash = d.digest()
    return hash

global hash_mdp
mdp=input("Mot de passe : ")
hash_mdp = hash(mdp)
go=input("Run or Stop : ")
if go == 'Run':
    crack()
else:
    print("Have a nice day !")
