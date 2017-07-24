# -*- coding: utf-8 -*-

#komentarz jednowierszowy
'''
zmienna1 = 5
zmienna2 = 5.3
'''
''' komentarz wielowierszowy 
text = "To jest moj tekst"
text2 = "To jest inny tekst"
literki = "A" literki = "a"
''' 
witaj = "I'm Dariusz"
exclamation = "!"
'''
zmienna3 = 2 + 5
Zmienna3 = 'liczba'
nowa_zmienna = zmienna3 + 5
print(zmienna1)
print(zmienna1, zmienna2) 
print(witaj)
print(zmienna3, Zmienna3)
print(nowa_zmienna)
print(" Hi, " + witaj)
print(" Hello world, Hi ," + exclamation)

print ("Przed zmiana", zmienna3)
zmienna3 = 3.14
print("Po zmianie", zmienna3)
del zmienna1
# print(zmienna1)
'''
#P1
'''
a = 1
b = 2.4
c = 'w1'
print(a, b, c)
'''
#P2
'''
a = 1
b = 2.4
c = "slowo w1"
print(a, b, c)
'''

#P3
'''
imie = "Jedrzej"
nazwisko = "Kowalski"
stanowisko = "dev"
data = "2000-01-01"
print(imie, nazwisko, stanowisko, data)
'''
    
#P4
'''
pi = 3.14
promien = int(input("Podaj liczbe ")) 
pole_kola = pi * promien*promien
print(pole_kola, pi*(promien**2))
'''
#P5
#imie = input(" Podaj imie ")
#nazwisko = input(" Podaj nazwisko ")
#stanowisko = input(" Podaj stanowisko ")
#data = input(" Podaj date ")
#print (imie, nazwisko, stanowisko, data)
#zwraca typ wartości zmiennej
'''
dluga = 31231414322
print (type (dluga))
print (3.0 / 2.0)
print (3 // 2)

print(round(3.14159), round(1.3), round(1.6))
print(round(-1.2), round(-1.5), round(-1.6))

print(int(3.14159), int(1.3), int(1.9))

print(int(-3.14159), int(-1.3), int(-1.9))
'''
#P5
'''
kwota_netto = int(input(" Podaj kwote netto "))
vat = int(input(" Podaj kwote podatku VAT 3%, 7% lub 23% ")) 
kwota_brutto = kwota_netto + (kwota_netto*(vat/100) )
print ("Twoja kwota brrutto", kwota_brutto)
print ("Twoja kwota brrutto" + str(vat) + " VAT wynosi " + str(kwota_brutto) + "zł.")

#stanowisko = input(" Podaj stanowisko ")
#data = input(" Podaj date ")
#print (imie, nazwisko, stanowisko, data)
#zwraca typ wartości zmiennej

'''
#P6
'''
nazwa_p1 = "chleb"
nazwa_p2 = "mleko"
nazwa_p3 = "cukier"
cena_p1  = 1.99
cena_p2  = 4.15
cena_p3  = 15.99
zamowienie_p1 = int(input("Liczba chlebów: "))
zamowienie_p2 = float(input("Litry mleka: "))
zamowienie_p3 = float(input("Waga cukierkrów: "))
suma = (cena_p1*zamowienie_p1) + (cena_p2*zamowienie_p2) + ((cena_p3/1000)*zamowienie_p3)
3
print ("Twoje zamówienie")
print ("==================")
print ("Ilość chleba", zamowienie_p1, "szt." )
print ("Ilość mleka", zamowienie_p2, "l." )
print ("Ilość cukierków", zamowienie_p3, "gr." )
print ("==================")
print ("Cena do zapłaty to:", round(suma,2), "zł." )

'''
#Liczby zespolenoe
'''
print((1+1j)+ (12+20j))
a = 12
b = 1 + (-1j)
print(a*b)

log1 = True
print(type(log1))
print(bool(''), bool(0), bool("TEkst"))
'''
a = """
Autor
Data
Versja
"""
#\n znak przejscia do nwej linii
#P20
'''
print(a)
b = "Autor:\nData\nVersja"
print(b)
txt = "napis "
print (txt*3)
'''
#P21
'''
imie = input("Podaj imie: ")
imie_1 = imie + ", "
imie_2 = imie + "."
n = int(input("Ile razy wydruk"))
print (imie_1 * (n-1) + imie_2)
'''

#P22
'''
imie = input(" Podaj imie ")
nazwisko = input(" Podaj nazwisko ")
stanowisko = input(" Podaj stanowisko ")
wiek = int(input(" Podaj wiek "))
pensja = int(input(" Podaj pensje "))
print (("Pan "+ imie + "(" + str(wiek) + " lat) pracuje na stanowisku " + stanowisko + " pensja:" + str(pensja)+ " brutto \n")*10)
'''
#data = input(" Podaj date ")
#print (imie, nazwisko, stanowisko, data)
#zwraca typ wartości zmiennej
'''
a = 1
print(type(a))
napis = str(a)
print (type(napis))

x = 1
a = 5.5
b = 6.5
print(type(a+b+x))
'''
'''
5500 - 168
x - 1 
'''
#P25
'''
wynagrodzenie = 5500
godziny = 168
kwota_netto = ( wynagrodzenie/godziny)
print ("stawka za godz netto:= ", round(kwota_netto, 2), "zł")
print ("stawka za godz brutto: = ", round(kwota_netto *1.22, 2), "zł")
'''
#P26
'''
p = True
q = True
dM1 = not (p and q)
dM2 = (not p) or (not q)
print (dM1, dM2)
print (dM1 == dM2)
'''
#P27 Bramki logiczne
'''
a = False
b = False
c = True
p1 = (not a and not b and not c)
p2 = (not a and not b and c)
p3 = (not a and b and c)
p4 = (a and not b and not c)
f0 = (not a and not b and not c) or (not a and not b and c) or (not a and b and c) or (a and not b and not c)
f1 = p1 or p2 or p3 or p4

'''
#P28 Operatory logiczne

'''
print('ala' < 'alan')
'''
#P28 Potęgowanie urojona
'''
liczba = round( 17**(1/2), 2)
uroj = 1j
res = str (liczba * uroj)
print (" Liczba zaspolona: 0 +" +res)

'''
#P29
'''
dziel = 17 % 7
z = dziel
print (z**2 + 3*z)
'''
'''
w1 = 1.2e+3+34.5
print ((str(w1)+ "\n")*20)
'''
'''
napis1 = input("podaj napis1: ")
napis2 = input("podaj napis2: ")
print ("napis 1 jest wiekszy leksykograficznie ", napis1 > napis2)
print ("napis 2 jest wiekszy leksykograficznie ", napis1 < napis2)
print ("napis 1 i napis 2 są takie same ", napis1 == napis2)
'''

#print (" imie\t" + "nazwisko\t"+"stanowisko")

 N = int(input("Podaj lata"))
 SPK = int(input("Podaj stan SPK"))
 P = float(input("Podaj oprocentowanie"))
 res = round(SPK*(1+P/1000)**N, 2) 
 print ("Kwota po"+ str(N) + "latach wynosi:" + str(res)+ " zł.")