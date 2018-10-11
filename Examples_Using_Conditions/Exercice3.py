print("Script appartenant à Alexy DA CRUZ.");
print("Script créé le 04/10/2018");
print("Plus d'info sur http://alexydacruz.geomtech.fr");
print();

Maths = float(input("Note en maths : "));
Francais = float(input("Note en français : "));
Informatique = float(input("Note en informatique : "));

Moyenne = float((Maths+Francais+Informatique)/3);
print("Moyenne :", Moyenne);
print();

if (Moyenne >= 0 and Moyenne < 5) :
    print("Appréciation : C'est nul !");
elif (Moyenne >= 5 and Moyenne < 10) :
    print("Appréciation : Pas bien");
elif (Moyenne >= 10 and Moyenne < 15) :
    print("Appréciation : Assez bien");
elif (Moyenne >= 15 and Moyenne <= 20) :
    print("Appréciation : Très bien");
else :
    print("/!\ Appréciation indisponible !");
