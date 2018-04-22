# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 17:56:11 2018

@author: azmijuhda
"""
import math

def f(x) :
    fx = x*math.exp(-x)+(math.cos(2*x))
    return fx

def ft(x) :
    ft = (1-x)*math.exp(-x)-(2*math.sin(2*x))
    return ft

print "METODE NEWTON REPSHON"

x = input("Pendekatan Awal : ")
e = input("Toleransi Error : ")
n = input("Iterasi Maksimum : ")
iterasi = 1
print("--------------------------------------------")
print "i","\t","x","\t","x1","\t","fx","\t","f'x"
print("--------------------------------------------")

y0=f(x)
y1=ft(x)

while (math.fabs(y0) > e and iterasi <= n) :
    x1 = x - (y0/y1)
    print "%d\t%f\t%f\t%f\t%f" % (iterasi, x, x1, y0, y1)
    y0=f(x1)
    y1=ft(x1)
    
    x=x1
    iterasi+=1

print("--------------------------------------------")
print "Akar terletak di x = %f " % (x1)
    
