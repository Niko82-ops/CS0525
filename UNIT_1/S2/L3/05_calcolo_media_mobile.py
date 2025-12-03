numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

medie = []
# Ciclo for per calcolare la media mobile
for index in range(len(numeri)):
    # slicing per ottenere gli ultimi n elementi
    if index - n + 1 < 0: 
        finestra = numeri[0:index+1]
    else:
         finestra = numeri[index-n+1:index+1]
    
    # Somma e divisioni per calcolare la media
    somma = 0
    
    for numero in finestra:
        somma = somma + numero 

    media = somma / len(finestra)

    # Rimuove lo zero finale se la media è intera
    if media == int(media):
        media = int(media)
    
    medie.append(media)

    # Stampa del risultato su una riga senza virgole

for index in range(len(medie)):
    if index == len(medie) - 1:
        print(medie[index])
    else:
        print(medie[index], end=", ")

    

