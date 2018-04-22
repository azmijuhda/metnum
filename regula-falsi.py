# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:50:58 2018

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

print("----------------------------------------------------------")
print "i","\t","a","\t","b","\t","x","\t","f(x)","\t","f(a)","\t","f(b)"
print("----------------------------------------------------------")
iterasi = 0

while True :
    iterasi+=1
    
    fa = f(a)
    fb = f(b)
    xr = ((fb*a)-(fa*b))/(fb-fa)
    fxr = f(xr)
    
    print "%d\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f" % (iterasi, a, b, xr, fxr, fa, fb)
    if( fa* fxr < 0 ):
        b = xr
        fb = fxr
    elif ( fa* fxr > 0 ):
        a = xr
        fa = fxr
    
    if (math.fabs(fxr) < e or iterasi > n):
        break
print("----------------------------------------------------------")
print "Akar = %.4f" % (xr)