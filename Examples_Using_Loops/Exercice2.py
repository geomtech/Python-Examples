from prettytable import PrettyTable
import datetime

print("Script appartenant à Alexy DA CRUZ.");
print("Script créé le 25/10/2018");
print("Plus d'info sur http://alexydacruz.geomtech.fr");
print();

Table = PrettyTable(['Date', 'Heure', 'Température (°C)', 'Ecart avec 37°C'])
now = datetime.datetime.now()
Temperatures = []

while True:
    cmd = input("Commande : ")

    if cmd == "Add":
        TemperatureActuel = float(input("Veuillez rentrer la température actuelle du patient : "))
        Table.add_row([str(now.day) + "/" + str(now.month) + "/" + str(now.year), str(now.hour) + ":" + str(now.minute), TemperatureActuel, (float(TemperatureActuel) - float(37))])
        Temperatures.append(TemperatureActuel)
    elif cmd == "Report":
        print(Table)
        Moyenne = 0
        for i in Temperatures:
            Moyenne = Moyenne + i
        Moyenne = Moyenne / len(Temperatures)
        print("Moyenne du patient :", Moyenne, "°C")
        print("Ecart avec la température normale :", (float(Moyenne) - float(37)), "\n")

    else:
        print("Commande inconnue")
