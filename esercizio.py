def perimetro_quadrato(): 
    print("Definisci un lato del quadrato")
    lato=input() 
    print("Il perimetro è " + str(int(lato) *4 )) 
def circonferenza_cerchio():
    print("Definisci il raggio del cerchio")
    raggio=input()
    print("La Circonferenza è " + str(int(raggio)* 2 * 3.14))
def perimetro_rettangolo():
    print("Definisci base e altezza")
    base=input()
    altezza=input()
    print("Il perimetro è " + str(int(base) *2 + int(altezza)))
print("Benvenuto nel calcolatore di perimetri")
print("Premi 1 per calcolare il perimetro del quadrato, Premi 2 per calcolare il raggio del cerchio, Premi 3 per calcolare il perimetro del rettangolo. ")
scelta=input()
if int(scelta) ==1:
    perimetro_quadrato()
elif int(scelta) ==2:
    circonferenza_cerchio()
elif int(scelta) ==3:
    perimetro_rettangolo()
    

    
