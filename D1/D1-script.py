# -*- config: utf-8 -#-
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
# print ("Twoja kwota brrutto" "+str(vat)+" VAT wynosi "+str(kwota_brutto)+"zł.")

#stanowisko = input(" Podaj stanowisko ")
#data = input(" Podaj date ")
#print (imie, nazwisko, stanowisko, data)
#zwraca typ wartości zmiennej
'''
#P6
nazwa_p1 = "chleb"
nazwa_p2 = "mleko"
nazwa_p3 = "cukier"
cena_p1  = 1.99
cena_p2  = 4.15
cena_p3  = 15.99
zamowienie_p1 = int(input("Liczba chlebów: "))
zamowienie_p2 = float(input("Litry mleka: "))
zamowienie_p3 = float(input("Waga cukierkrów: "))
suma = (cena_p1*zamowienie_p1) + (cena_p2*zamowienie_p2) + (cena_p3*zamowienie_p3)

print ("Twoje zamówienie")
print ("================")
print ("Ilość chleba", zamowienie_p1, "szt." )
print ("Ilość mleka", zamowienie_p2, "l." )
print ("Ilość cukierków", zamowienie_p3, "gr." )
print ("Cena do zapłaty to:", suma )



