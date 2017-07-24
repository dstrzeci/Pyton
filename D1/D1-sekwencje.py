# -*- coding: utf-8 -*-
'''
napis = "zawazawartość"
#napis[0] = 't'
print(napis [4])
print(napis.capitalize())
print(napis.count("aw"))
print(napis.islower())
print(napis.index("a"))
print(napis.replace("zawa","otwa"))
'''
#tablice, listy - mogą zawierać wszystkie typy danych
'''
Tab = []
Tab.append (1)
Tab.append ("abc")
Tab.append ('A')

print(Tab)
print(Tab[2])

oceny = []
a = input("Podaj ocenę")
oceny.append(a)
oceny.append(input("Podaj ocenę"))
print(oceny[0], oceny[1])
oceny[0]='5'
print(oceny[0], oceny[1])
oceny2 = [3,4,5]
print(oceny2)
'''
#oceny2 = [3,4,5,6,7,8,9,10]
'''
ListList = [ [1, 2, 3], ["Nocny", "Dzienny", [0,1,2] ]]
print(ListList[1][2])

print(oceny2[3:5])

print(oceny2[1::2])
print(oceny2[4:])
print(len(oceny2))

text = 'napis'
lista = list (text)
print(lista)
lista[2] = "w"
print(lista)
#print(lista.count())
lista.pop(2)
print(lista)
print(lista[2], len(lista))

listap = list(text)
listac = list(text)
listap = ['melko', 'cukier', 'woda']
listac = [2, 3, 4]
print(listap,listac)
'''
'''
art = [["melko", "cukier", "woda"], [1.99, 3.15, 13.55]]
print (art)
print (art[0][0] +"\t\t"+str(art[1][0]))
print (art[0][1] +"\t\t"+str(art[1][1]))
print (art[0][2] +"\t\t"+str(art[1][2]))
'''
#krotka = ("a", 2, 13.5)
'''
#krotka2 = "a","b" ,"c"
#print(krotka, krotka2)
data = (("melko", "cukier", "woda"),("01-01-2017", "03-03-2018", "05-05-2019"))
print(data)
print(data[0][0]+ "\t\t"+ str(art[1][0]))
print(data[0][1]+ "\t\t"+ str(art[1][1]))
print(data[0][2]+ "\t\t"+ str(art[1][2]))
#krotkad = (2017, 07, 24)
#print("Data wzanosci  artyukułu:", krotkad[0], krotkad[1],krotkad[2] )


tabelka = [("Kowal", ""), (), []]
'''
