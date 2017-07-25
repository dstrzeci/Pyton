# -*- coding: utf-8 -*-
import random

# Słowniki zadania 1
'''
literki = {'a' : 'A', 'b' : ' B', 'c ': 'C'}
print (literki)

print (len(literki))
#print (literki['a'], literki['b'], literki['c'])
literki['c'] = 'napis'
print (literki['c'])
print (literki.keys(), literki.values())
literki['d'] = 'D'
del literki ['c']
print(literki)
literki[2] = 'abc'
print(literki)
to_str = str(literki)
print(to_str[0], to_str[1], to_str[2])

'''
'''
# liczby 1 -5
key1 = input('Podaj wartość od 1 do 5 zapisana słownie - ')
to_dec = {'jeden': 1 , 'dwa': 2, 'trzy' : 3, 'cztery' : 4, 'pięć' : 5, 'piec' : 5   }
print (key1.capitalize() +' w postaci dzieisętnej to:'+str(to_dec[key1]))

'''
# rzymskie i dec 
'''
key1 = input('Podaj wartość od 1 do 5 zapisana słownie - ')
to_dec = {'jeden': 1 , 'dwa': 2, 'trzy' : 3, 'cztery' : 4, 'pięć' : 5, 'piec' : 5   }
to_roman = { 1: 'I' , 2: 'II', 3 : 'III', 4 : 'IV', 5 : 'V' }
print (key1.capitalize() +' w postaci dzieisętnej to:'+str(to_dec[key1]))
print (key1.capitalize() +' w postaci rzymskiej to:'  +str(to_roman[to_dec[key1]]) )
 '''
#SŁoWNIKI {}
'''
# słownik nazwa, ilośc, cena
#pobieramy produkt
nazwa = input("Jaki produkt wybierasz? (chleb, mleko, cukier) :")
#kod produktu
s1_nazwa = {'chleb' : '0x1', 'mleko': '0x2', 'cukier' : '0x3'}
#ceny produktów
s2_cena = { '0x1' : 1.99, '0x2' : 3.99, '0x3' : 5.99 }
#ilość produktów
s3_ilośc = int(input('Podaj ilość produktu :'))
print("Razen do zapłaty :"+ str(round(s2_cena[s1_nazwa[nazwa]]*s3_ilośc, 2)) + "zł ("+  str(round(s2_cena[s1_nazwa[nazwa]]*s3_ilośc*1.23, 2))+ "zł brutto)" )
'''
#zbiory - tworzenie
'''
kształty = set(['kolo', 'kwadrat','trojkąt'])
kształty.add('okrąg') 
kształty.discard('kolo')
print(kształty)
okragle = set(['okrag'])
print(len(kształty), len(okragle))
#podzbiory
print(kształty.issubset(okragle))
#nadzbiorem 
print(kształty.issuperset(okragle))
print(kształty>=set(['trojkąt'or'kwadrat']))
'''
#zbiory - metody teoriomnogościowe
'''
print(kształty)
print(okragle)
#połaczenie
print(kształty | okragle)
#czesc wspolna
print(kształty & okragle)
#Roznaica
print(kształty - okragle)
#Roznica
print(kształty ^ okragle)
'''
#Zadanie liczby 1-49
#random.randint - biblioteka losowanie liczb int
'''
los1 = random.randint(1,49)
los2 = random.randint(1,49)
los3 = random.randint(1,49)
los4 = random.randint(1,49)
los5 = random.randint(1,49)
los6 = random.randint(1,49)

losowanie = set([los1, los2, los3, los4, los5, los6])
print(losowanie)
print(losowanie)
'''
#Zb losowy 6 liczb z 1-49
# Zb pusty S 
'''
S =set()
#dodajemy kolejne elementy
S.add(random.randint(1,49))
S.add(random.randint(1,49))   
S.add(random.randint(1,49))   
S.add(random.randint(1,49))   
S.add(random.randint(1,49))   
S.add(random.randint(1,49))   
S.add(random.randint(1,49))  
S.add(random.randint(1,49))
S.add(random.randint(1,49))   
S.add(random.randint(1,49))  
#krotka L z zawartością zbioru S
L = list(S)
#wyswietalanie listy L
print(L[:6])
'''
# Instrukacja IF
'''
a = int(input("Podaj liczbe 2:")) 
if(a %2 == 0):
    print("Liczba " +str(a)+ " jest parzysta")
    #print("jestem w if'e")
    if(a >= 10):
        print("Liczba "+str(a)+" jest parzysta i większa równa od 10")
    else:
        print("Liczba "+str(a)+" jest parzysta i mniejsza od 10")
else:
    print("Liczba "+str(a)+" jest nieparzysta")
    print("jestem w elsie")
'''
# prog if
'''
a = int(input("Podaj liczbe 2:")) 
if(a%2 == 0 and a>= 10):
    print("Liczba " +str(a)+ " jest parzysta i większa równa od 10" )
elif(a%2 == 0 and a < 10):
    print("Liczba " +str(a)+ " jest parzysta i mniejsza od 10" )
else:
    print("Liczba "+str(a)+" jest nieparzysta")
'''
# prog if
'''
a = int(input("Podaj liczbe :"))
if(a == 0):
    print("Liczba " +str(a)+ " jest równa 0" )
elif(a == 1):
    print("Liczba " +str(a)+ " jest równa 1" )
'''
# prog  if bool
'''
if(bool(0)):
    print(bool(0))
if(bool(1)):
    print(bool(1))
if(bool(2)):
    print(bool(2))
if(bool(3)):
    print(bool(3))  
   
 '''
# prog  if bool
'''
a = int(input("Podaj liczbe 2:")) 
if(a>= 0 and a<= 9):
    print("Liczba " +str(a)+ " jest w przedziale 0 do 9" )
else:
    print("Out of range ")
'''
#ZAdanie
'''
list = [1,2,3,4,5,6,7,8,9]
index = int(input('Podaj elemen do wyświetlenia :'))
if(index >= 0 and index <=(len(list)-1)):
    print("Index is ok" )
    print(list[index]-1)
else:
    print("Out of range ")
'''

#ZAdanie lista 0,1 sprawdzenie 2 pozycji z listy
'''
list = [1,2,3,4,5,6,7,8,9]
index = int(input('Podaj elemen do wyświetlenia :'))
if(index >= 0 and index <=(len(list)-8)):
    print("Index is ok" )
    print(list[index]-1)
else:
    print("Out of range ")
if (list[0] > 0 and list[1] > 0):
    print("Elementy większe od ")
elif(list[0] > 0 and list[1] < 0):
        print("Pierwszy element większe od 0, a drugi mniejszy od 0")
elif(list[0] < 0 and list[1] > 0):
    print("Pierwszy element mniejszy od 0, a drugi większy od 0")     
else:
    print("elementy sa mniejsze do zera")
    
'''
# Zbioiry i listy
'''
A = set([1,2,3,4,5,12])
B = set([1,2,3,4,5,7])

if(A == B):
    print("Zbiory sa rowne")
elif(A.issuperset(B)):
    print (" A jest nadzbiorem B")
elif(B.issuperset(A)):
    print (" B jest nadzbiorem A")
else:
    print("Zbiory rózne ")
'''
#Pętle
'''
lista = [1,2,3,4,5,6,7,8,9]
i = 0
while(i <= (len(lista) -1)):
    print("Index :" +str(i)+"\t Wartość:" +str(lista[i]) )
    i+=1
print("Poza pętlą ")
'''
#ZAdanie Pętle odwrotna
#Po while dodajemy elsa dla przypadku wyjscia z petli
'''
lista = [1,2,3,4,5,6,7,8,9]
i = len(lista)-1
while(i >= 0 ):
    if(lista[i]%2 == 0):
        print("Index :" +str(i)+"\t Wartość:" +str(lista[i]) )
    i-=1
else:
      print("Jestem w else")

print("Jestem poza elsem")  
'''
#ZAdanie warunek 3 arg

a= 15
b= 15
print('A jest większe od B o: '+str(a-b)) if(a >= b) else print("a jest miejsze od b o: " +str(b-a))