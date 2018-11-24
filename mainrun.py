# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:27:58 2018

@author: cabhi
"""


reqamt = int(input("What is the amount you want to store in USD: "))

#denom of USD
usd = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.1, 0.05, 0.01]
def howmuch(reqamt):
    hund = 0
    fif = 0
    twen = 0
    ten = 0
    fiv = 0
    tw = 0
    on = 0
    quart = 0
    dime = 0
    fivc = 0
    c = 0
    total = 0
    if(reqamt < usd[10]):
        while(reqamt >= usd[0]):
            reqamt = reqamt-usd[0]
            hund+=1
            total+=1
        while(reqamt >= usd[1]):
            reqamt = reqamt-usd[1]
            fif+=1
            total+=1        
        while(reqamt >= usd[2]):
            reqamt = reqamt-usd[2]
            twen+=1
            total+=1
        while(reqamt >= usd[3]):
            reqamt = reqamt-usd[3]
            ten+=1
            total+=1
        while(reqamt >= usd[4]):
            reqamt = reqamt-usd[4]
            fiv+=1
            total+=1    
        while(reqamt >= usd[5]):
            reqamt = reqamt-usd[5]
            tw+=1
            total+=1
        while(reqamt >= usd[6]):
            reqamt = reqamt-usd[6]
            on+=1
            total+=1
        while(reqamt >= usd[7]):
            reqamt = reqamt-usd[7]
            quart+=1
            total+=1
        while(reqamt >= usd[8]):
            reqamt = reqamt-usd[8]
            dime+=1
            total+=1
        while(reqamt >= usd[9]):
            reqamt = reqamt-usd[9]
            fivc+=1 
            total+=1  
        while(reqamt >= usd[10]):
            reqamt = reqamt-usd[10]
            c+=1
            total+=1
    return(total, hund, fif, twen, ten, fiv, tw, on, quart, dime, fivc, c)
    
#outputs
print(total, "is the total amount of notes, coins required.")
print("You need: ", hund, " Hundreds,", fif, " Fifties,", twen, " Twenties,", ten, " Tens,",
      fiv, " Fives,", tw, " Two's,", on, " One's,", quart, " Quarters,", dime, " Dimes,", fivc,
      " Five Cents,", c, " Cents.")









