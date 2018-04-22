# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 21:44:11 2018

@author: azmijuhda
"""

import math

def f(x):
    fx = math.exp(-x) - x
    return fx

a = input("Batas x bawah : ")
a = float(a)
b = input("Batas x atas : ")
b = float(b)
e = input("Tolerannsi Error : ")
n = input("Iterasi Makasimum : ")

print("-------------------------------------------------")
print "i","\t","a","\t","b","\t","x","\t","f(x)","\t","f(a)"
print("-------------------------------------------------")
iterasi = 0

while True :
    iterasi+=1
    xr = (a + b)/2
    fa = f(a)
    fb = f(b)
    fxr = f(xr)
    
    print "%d\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f" % (iterasi, a, b, xr, fxr, fa)
    if( fa* fxr < 0 ):
        b = xr
        fb = fxr
    elif ( fa* fxr > 0 ):
        a = xr
        fa = fxr
    
    if (math.fabs(a - b) < e or iterasi > n):
        break
print("-------------------------------------------------")
print "Akar = %.4f" % (xr)