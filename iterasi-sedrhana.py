# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 13:30:48 2018

@author: azmijuhda
"""

import math

def f(x) :
    fx = math.exp(-x)-x
    return fx

def gx(x):
    gx = math.exp(-x)
    return gx
    
x0 = input("Tebakana Awal : ")
e = input("Toleransi Error : ")
n = input("Iterasi Maksimum : ")

print("-------------------------------------------------")
print "i","\t","x0","\t","x","\t","f(x)"
print("-------------------------------------------------")

iterasi = 1

while True :
    x = gx(x0)
    fx = f(x)
    print "%d\t%.4f\t%.4f\t%.4f" % (iterasi, x0, x, fx)
    x0 = x
    iterasi += 1
    if (iterasi >= n+1 or math.fabs(fx) <= e):
        break

print("-------------------------------------------------")
print "Akar terletak di x = %f " % (x)