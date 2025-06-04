# Prüft ob g ein generator für p ist
def ist_generator(g, p): 
    erzeugte = set()
    for i in range(1, p):
        erzeugte.add(pow(g, i, p)) # g^i mod p
    return len(erzeugte) == p - 1  # alle werte von 1 bis p-1

# Findet ersten generator für p
def finde_generator(p):
    for g in range(2, p):
        if ist_generator(g, p):
            return g
