import math

def leggi_numero(messaggio):
    while True:
        valore = input(messaggio)
        try:
            numero = float(valore)
            if numero < 0:
                print("Inserisci un numero positivo!")
            else:
                return numero
        except ValueError:
            print("Per favore, inserisci un numero valido!")

def perimetro_quadrato():
    lato = leggi_numero("Inserisci la lunghezza del lato del quadrato: ")
    return lato * 4

def circonferenza_cerchio():
    r = leggi_numero("Inserisci il raggio del cerchio: ")
    return 2 * math.pi * r

def perimetro_rettangolo():
    base = leggi_numero("Inserisci la base del rettangolo: ")
    altezza = leggi_numero("Inserisci l'altezza del rettangolo: ")
    return 2 * base + 2 * altezza

def menu():
    print("\nCalcolo del perimetro di figure geometriche")
    print("1 - Quadrato")
    print("2 - Cerchio")
    print("3 - Rettangolo")
    print("0 - Esci")

def main():
    while True:
        menu()
        scelta = input("Scegli una figura (0-3): ")
        if scelta == "1":
            print(f"Il perimetro del quadrato è: {perimetro_quadrato()}")
        elif scelta == "2":
            print(f"La circonferenza del cerchio è: {circonferenza_cerchio():.2f}")
        elif scelta == "3":
            print(f"Il perimetro del rettangolo è: {perimetro_rettangolo()}")
        elif scelta == "0":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida! Inserisci 0, 1, 2 o 3.")


main()
