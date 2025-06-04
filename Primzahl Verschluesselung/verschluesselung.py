def erstelle_dictionaries(alphabet, p, generator):
    verschluesselung_dict = {char: pow(generator, i, p) for i, char in enumerate(alphabet)} # Ordnet jedem buchstaben eine Zahl zu basierend auf g^i mod p
    entschluesselung_dict = {value: key for key, value in verschluesselung_dict.items()} # umgekehrt wird jeder zahl einem buchstaben hinzugefügt
    return verschluesselung_dict, entschluesselung_dict

def verschluesseln(wort, versch_dict):
    wort = wort.upper()
    return [versch_dict[char] for char in wort if char in versch_dict]

def entschluesseln(code_liste, entsch_dict):
    return ''.join(entsch_dict[code] for code in code_liste)