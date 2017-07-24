# -*- coding: utf-8 -*-

N = int(input("Podaj lata: "))
SPK = int(input("Podaj stan SPK: "))
P = float(input("Podaj oprocentowanie: "))
res = round(SPK*(1+P/100)**N, 2) 
print ("Kwota po"+ str(N) + "latach wynosi: " + str(res)+ " zł.")