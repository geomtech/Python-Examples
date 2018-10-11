print("Script appartenant à Alexy DA CRUZ.");
print("Script créé le 04/10/2018");
print("Plus d'info sur http://alexydacruz.geomtech.fr");
print();

a = input("valeur de a ?")
b = input("valeur de b ?")

if float(a) != 0:
    S = -float(b)/float(a)
else:
    if float(b) != 0:
        S = "Pas de solution"
    else:
        S = "Infini de solutions"
print(S)
