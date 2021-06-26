from random import *



nbr = 0
print("pour lance un dé une seule foie tappez 1\n")
print("pour lance un dé une n fois tappez 2\n")
print("pour lance un dé n fois et calcule les fois ou le resultat égale a 6 tappez 3\n")
print("pour lance un dé n fois et afficher le nombre de lancers avant obtenir le numéro 6 tappez 4\n")
print("pour tiré une piece de monnaie n fois tappez 5\n")

c = 0
j=0
def q1():
    d = randint(1, 6)
    print(d)

def q2():
    n = int(input("nombre de lancer ? "))
    for i in range(n):
        d = randint(1, 6)
        print(d)
def q3():
    global c
    list = []
    n = int(input("nombre de lancer ? "))
    for i in range(n):
        d = randint(1, 6)
        c = c + 1
        if (d == 6):
            list.append(c)

    print("le nombre de fois ou le numéro 6 apparait:")
    print(len(list))

def q4():
    global c
    n = int(input("nombre de lancer ? "))
    d = randint(1, 6)
    while (d != 6 and c <= n):
        d = randint(1, 6)
        c = c + 1

    if (d == 6):
        print("le numero 6 s'affiche apres le(s) lancer(s) :")
        print(c)
    elif (c > n):
        print("le numero 6 ne s'affcihe pas")
def q5():
    d = randint(1, 2)
    print(d)

while(j<1):
    ch = int(input("votre chois ?"))
    if (ch == 1):
        q1()
    elif (ch == 2):
        q2()
    elif (ch == 3):
        q3()
    elif (ch == 4):
        q4()
    elif (ch == 5):
        q5()

    l=str(input("si vouz voulez terminer tappez oui ?"))
    if(l=="oui"):
        j=j+1
        print("Programme Terminer")







