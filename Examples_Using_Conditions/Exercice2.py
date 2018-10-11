from math import sqrt

print("Script appartenant à Alexy DA CRUZ.");
print("Script créé le 04/10/2018");
print("Plus d'info sur http://alexydacruz.geomtech.fr");
print();

A = float(input("A="))
B = float(input("B="))
C = float(input("C="))

D = B*B-4*A*C
print("Résultat de B*B-4*A*C :", D)
#R = sqrt(D)

if D > 0:
    if A == 0 or B == 0 or C == 0:
        print("Division par 0 impossible")
    else :
        Ra = (-B+sqrt(D))/(2*A)
        Rb = (-B-sqrt(D))/(2*A)
        print("Première racine", Ra)
        print("Deuxième racine", Rb)
if D == 0:
    if A == 0 or B == 0 or C == 0:
        print("Division par 0 impossible")
    else :
        Rd = -B/(2*A)
        print("Racine double", Rd)
if D < 0:
    print("L'équation n'admet pas de racine réel")
