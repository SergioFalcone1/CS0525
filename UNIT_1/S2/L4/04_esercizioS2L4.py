import math

print("Calcoliamo il perimetro di una figura geometrica!")
print("1,Quadrato")
print("2,Cerchio")
print("3,Rettangolo")

scelta = input("Scegli la figura (1-3): ")
if scelta == "1":
    lato = float(input("Inserire lato del Quadrato: "))
    perimetro = (lato*4)
    print("Il perimentro del Quadrato è: ",perimetro)
elif scelta == "2":
    raggio = float(input("Inserisci il raggio del Cerchio: "))
    circonferenza = 2*math.pi*raggio 
    print("La circonferenza del Cerchio è: ",circonferenza)
elif scelta =="3":
    base = float(input("Inserisci base del Rettangolo: "))
    altezza = float(input("Inserisci altezza del Rettangolo: "))
    perimetro = base*2 + altezza*2
    print("Il perimetro del Rettangolo è: ", perimetro)
else:
    print('No. "Questo" non lo avevo considerato.')
    


