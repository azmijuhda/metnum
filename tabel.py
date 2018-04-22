# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:47:09 2018

@author: azmijuhda
"""

import math
x=[]
y=[]
xatas = input("Batas Atas : ")
xatas = float(xatas)
xbawah = input("Batas Bawah : ")
xbawah = float(xbawah)
n = input("Jumlah Pembagi : ")

h = (xatas - xbawah)/n
print "---------------------------------------"
print "x\t\tf(x)"
print "---------------------------------------"
i=0
while (i <= n):
    xx = xbawah + (i*h)
    x.insert(i, xx)
    xx = x[i]*math.exp(-x[i]) + math.cos(2*x[i])
    y.insert(i, xx)
    print "%.4f\t\t%.4f" % (x[i], y[i])
    i+=1

print "---------------------------------------"    
kondisi = 0
j=0
while (j < n-1):
    yy = y[j]*y[j+1]
    if (yy < 0):
        kondisi = 1
        akar = x[j+1]
        if ( math.fabs(y[j]) < math.fabs(y[j+1]) ):
            akar = x[j]
            print "Akar dekat dengan %.4f" % (akar)
        else :
            akar = x[j+1]
            print "Akar dekat dengan %.4f" % (akar)
    j+=1

if (kondisi != 1):
    print "Tidak Ada Akar !!"

exit(0)