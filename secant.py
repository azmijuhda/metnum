# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 08:17:34 2018

@author: azmijuhda
"""

import math

def f(x) :
    fx = x*math.exp(-x)+math.cos(2*x)
    return fx

print "METODE SECANT"

x0 = input("Pendekatan Awal (x0) : ")
x0 = float(x0)
x1 = input("Pendekatan Awal (x1) : ")
x1 = float(x1)
e = input("Toleransi Error : ")
e = float(e)
n = input("Iterasi Maksimum : ")
iterasi = 1

print("-------------------------------------------------")
print "i","\t","x0","\t","x1","\t","x2","\t","f(x0)","\t","f(x1)"
print("-------------------------------------------------")

y0=f(x0)
y1=f(x1)

while True :
    xr = x1-x0    
    x2 = x1 - ((y1*xr)/(y1-y0))
    y2=f(x2)
    
    print "%d\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f" % (iterasi, x0, x1, x2, y0, y1)
    x0=x1
    x1=x2    
    y0=f(x0)
    y1=f(x1)
    iterasi+=1
    if (math.fabs(y2) <= e or iterasi >=n):
        break

print("-------------------------------------------------")
print "Akar terletak di x = %f " % (x2)
    