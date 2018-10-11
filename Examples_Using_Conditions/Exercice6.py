print("Script appartenant à Alexy DA CRUZ.");
print("Script créé le 04/10/2018");
print("Plus d'info sur http://alexydacruz.geomtech.fr");
print();

Choix = input("Euro ou Franc ? : ")

if Choix == "Euro":
    Euro = float(input("Euro : "))
    Resultat = Euro*6.55957
    print("Conversion de l'Euro vers le Franc :", Resultat)
elif Choix == "Franc":
    Franc = float(input("Franc : "))
    Resultat = Franc/6.55957
    print("Conversion du Franc vers l'Euro :", Resultat)
