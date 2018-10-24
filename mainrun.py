# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:27:58 2018

@author: cabhi
"""
import time


thou = 0
hund = 0
fif = 0
twen = 0
ten = 0
fiv = 0
total = 0


print("This only works with USD and CHF at the moment i will work on adding other currencies when i get the time.")

reqamt = int(input("What is the amount you want to store in USD: "))

#denom of swiss francs
chfd = [5, 10, 20, 50, 100, 1000]

#denom of swiss francs in USD value
chf = [5.01, 10.03, 20.07, 50.17, 100.33, 1003.34 ]
na = True

while(na == True):
    if(reqamt >=(chf[5])):
        reqamt = reqamt - chf[5]
        thou+=1
        total += 1
    if(reqamt >=(chf[4])):
        reqamt = reqamt - chf[4]
        hund+=1
        total += 1
    if(reqamt >=(chf[3])):
        reqamt = reqamt - chf[3]
        fif+=1
        total += 1
    if(reqamt >=(chf[2])):
        reqamt = reqamt - chf[2]
        twen+=1
        total += 1
    if(reqamt >=(chf[1])):
        reqamt = reqamt - chf[1]
        ten+=1
        total += 1
    if(reqamt >=(chf[0])):
        reqamt = reqamt - chf[0]
        fiv+=1
        total += 1
    if(reqamt < (chf[0])):
        na = False

tot = (thou + hund + fif + twen + ten + fiv)
print(total)
print(thou, hund, fif, twen, ten, fiv)
print(reqamt)

