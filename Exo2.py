import numpy as np


def is_stochastic(vector):
    summation = 0
    for value in vector:
        if value > 1 or value < 0:
            return False
        summation += value
    return summation == 1


def is_stochastic_matrix(mat):
    return all(is_stochastic(vect) for vect in mat)


def mat_mul(a, b):
    c = []
    for i in range(len(a)):
        c.append([0] * len(b[0]))
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += (a[i][k] * b[k][j])
    return c


def mat_pow(a, n):
    if n <= 0:
        return None
    if n == 1:
        return a
    if n == 2:
        return mat_mul(a, a)
    t1 = mat_pow(a, n // 2)
    if n % 2 == 0:
        return mat_mul(t1, t1)
    return mat_mul(t1, mat_mul(a, t1))


def enter_vect(V: []):
    j=0
    n = int(input("Enter la dimension de la languer de vecteur:"))
    while j < n:
        valeurInput = input("Enter la valeur")
        if valeurInput != "":
            V.append(float(valeurInput))
            j = j + 1

        else:
            V.clear()
            valeurInput = input("Rentrer tous les valeurs:")
            V.append(float(valeurInput))
    res_val = np.array(V)
    print(res_val)
    print("le vecteur est stochastic ?")
    print(is_stochastic(V))

def enter_mat():
    n = int(input("Enter la dimension de la matrice:"))
    i=0
    mat= []
    while i < n * n:
        valeurInput = input("Enter les values:")
        if valeurInput != "":
           mat.append(float(valeurInput))
           i= i + 1

        else:
            mat.clear()
            valeurInput = input("Rentrer  les values")    
            mat.append(float(valeurInput))

    w = np.array(mat)
    w.shape = (n,n)
    print(w)

    print("la matrice est stochastic ?")
    print(is_stochastic_matrix(w))
    if (is_stochastic_matrix(w)==True):
        c=str(input("voulez-vous calculer la puissance oui/non?"))

        if(c=="oui"):

                m= int(input("\nEnter la puissance :"))
                print("le resultat de la puissance de votre matrice et :")
                print(mat_pow(w,m))
        else:
            print("terminer")
    else:
        print("votre matrice n'est pas stochastic")







print("choisissez une option")
print("pour verifeie si le vecteur est stochastique tappez 1")
print("pour verifeie si la matrice est stochastique et calculer leur puissance tappez 2")

j=0
while(j<1):

    ch=input("votre chois svp?")
    if(str(ch)==""):

        print("merci de donner votre choix")
    elif(int(ch)==1):
        d=[]
        enter_vect(d)

    elif(int(ch)==2):
        enter_mat()




    decision=str(input("si vous voulez stopper le programme tappez oui"))
    if(decision=="oui") :
        j=j+1
        print("Programme Terminé")




