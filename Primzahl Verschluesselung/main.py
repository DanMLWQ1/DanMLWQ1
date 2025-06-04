import json
from generator import finde_generator
from verschluesselung import erstelle_dictionaries, verschluesseln, entschluesseln

# Alphabet laden
with open("C:\\Users\\letov\\OneDrive\Dokumente\\Python Projects\\Primzahl Verschluesselung\\alphabet.json", "r") as f:
    alphabet = json.load(f)["alphabet"]

# Parameter
p = 29
generator = finde_generator(p)  # Erster Gültiger Generator wird gespeichert
versch_dict, entsch_dict = erstelle_dictionaries(alphabet, p, generator)

# g&p Ausgabe
print(f"\nPrimzahl = {p}")
print(f"Generator = {generator}\n")


# Nutzereingabe
wort = input("Gib ein Wort ein (nur Buchstaben A-Z): ")

# Verschlüsseln & Entschlüsseln
verschluesselt = verschluesseln(wort, versch_dict)
entschluesselt = entschluesseln(verschluesselt, entsch_dict)

# Ergebnis
print("\nVerschlüsselt:", verschluesselt)
print("Entschlüsselt:", entschluesselt)