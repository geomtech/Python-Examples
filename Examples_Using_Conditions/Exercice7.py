from prettytable import PrettyTable

print("Script appartenant à Alexy DA CRUZ.");
print("Script créé le 11/10/2018");
print("Plus d'info sur http://alexydacruz.geomtech.fr");
print()

print("Pour gérer votre compte, vous devez entrer votre Solde actuel.")
print()
Operations = PrettyTable(['Nom', 'Debit', 'Credit'])
Solde = input("Votre solde actuel : ");

print()
print("Pour connaître les commandes disponibles, taper \"help\"")
print()

while True:
    cmd = input("Commande : ")

    if cmd == "Solde":
        print(str(Solde) + "€ sur le compte")
        print()
    elif cmd == "Debit":
        Nom = input("Nom de l'opération : ")
        Debit = input("Somme à débiter : ")

        Operations.add_row([Nom, Debit, 0])
        Solde = float(Solde) - float(Debit)
        print()
    elif cmd == "Credit":
        Nom = input("Nom de l'opération : ")
        Credit = input("Somme à créditer : ")

        Operations.add_row([Nom, 0, Credit])
        Solde = float(Solde) + float(Credit)
        print()
    elif cmd == "Operations":
        print(Operations)
        print()
    elif cmd == "help":
        print()
        print("Commandes disponibles")
        print()
        print("Solde      : Affiche le solde du compte")
        print("Operations : Affiche un tableau contenant les opérations du compte")
        print("Debit      : Ajoute une opération de débit")
        print("Credit     : Ajoute une opération de crédit")
        print()
    else:
        print("Commande non disponible, taper \"help\" pour connaître les commandes disponibles")
        print()
