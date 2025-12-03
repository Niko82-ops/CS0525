import re

def conta_parole(testo):
    # Trasforma tutto in minuscolo
    testo = testo.lower()
    # Rimuove la punteggiatura
    testo = re.sub(r'[^\w\s]', '', testo)
    # Divide il testo in parole
    parole = testo.split()
    
    # Dizionario per contare le occorrenze
    conteggio = {}
    for parola in parole:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1
    return conteggio

# Input dall'utente
testo = input("Inserisci il testo: ")

# Calcola e stampa il dizionario
risultato = conta_parole(testo)
print(risultato)
