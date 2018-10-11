print("Script appartenant à Alexy DA CRUZ.");
print("Script créé le 04/10/2018");
print("Plus d'info sur http://alexydacruz.geomtech.fr");
print();

Solde = float(input("Solde : "))
Retrait = float(input("Retrait : "))
AutorisationDecouvert = -50

NouveauSolde = Solde-Retrait
if NouveauSolde < AutorisationDecouvert:
    print("Désolé, vous êtes en dehors des limites fixés à votre découvert")
else :
    print("Nouveau Solde :", NouveauSolde)
