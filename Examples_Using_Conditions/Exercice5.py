print("Script appartenant à Alexy DA CRUZ.");
print("Script créé le 04/10/2018");
print("Plus d'info sur http://alexydacruz.geomtech.fr");
print();

Zone = int(input("Votre zone : "))
Benefice = float(input("Bénéfice effectué : "))
Indemnite = 0
Salaire = 0

if Zone == 1:
    Indemnite = Benefice + ((Benefice*0.5)/100)
elif Zone == 2:
    Indemnite = Benefice + ((Benefice*1)/100)
elif Zone == 3:
    Indemnite = Benefice + ((Benefice*3)/100)

Salaire = float(1498.47) + Indemnite

print("Indemnité :", Indemnite)
print("Salaire :", Salaire)
