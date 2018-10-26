from prettytable import PrettyTable
import datetime

print("Script appartenant à Alexy DA CRUZ.");
print("Script créé le 25/10/2018");
print("Plus d'info sur http://alexydacruz.geomtech.fr");
print();

EleveArr = []
MatiereArr = []
NoteArr = []
CoeffArr = []
Table = PrettyTable(['Eleve', 'Matière', 'Note', 'Coefficient'])

while True:
    cmd = input("Commande : ")

    if cmd == "Add":
        NomEleve = input("Nom de l'élève : ")
        Matiere = input("Matière (Maths, Français, ou Informatique) : ")
        Note = float(input("Note de l'élève : "))
        EleveArr.append(NomEleve)
        MatiereArr.append(Matiere)
        if Matiere == "Français":
            Coefficient = 2
            CoeffArr.append(2)
        elif Matiere == "Maths":
            Coefficient = 3
            CoeffArr.append(3)
        elif Matiere == "Informatique":
            Coefficient = 4
            CoeffArr.append(4)
        NoteArr.append(Note * Coefficient)
        Table.add_row([NomEleve, Matiere, Note, Coefficient])
    elif cmd == "Notes":
        print(Table)
        ID = 0
        for value in EleveArr:
            print(EleveArr[ID], MatiereArr[ID], NoteArr[ID])

            ID=+1
    else:
        print("Commande inconnue")
