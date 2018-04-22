# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 08:39:06 2018

@author: azmijuhda
"""


print ("== GAUSS ==")
n = input("Masukkan Ordo Matriks : ")
n = int(n)

a=[]
i=0
j=0
nn=n+1

for i in range(n):
   print ("")
   a.append([])
   for j in range(nn):
       if (j != n):
           print ("Masukkan Nilai Matriks [%d,%d] " % (i+1,j+1))
           x = input("-> ")
           x = float(x)
           a[i].append(x)
           
       else:
           print ("Masukkan Nilai Matriks [%d,%d] " % (i+1,j+1))
           x = input("-> ")
           x= float(x)
           a[i].append(x)
           
i=0
j=0
print ("\nMatriks Awal")
for i in range(n):
   for j in range(nn):
       if (j != n):
           print ("%.2f "% (a[i][j]), end="")
           
       else:
           print ("| %.2f"% (a[i][j]))

i=0
j=0
for i in range(n):
    print ("")
    if (a[i][i]!=n):
        konst = a[i][i]
        for j in range(nn):
            a[i][j] /= konst       
    j=i+1
    k=0
    for j in range(n):
            konst = a[j][i]
            for k in range(nn):
                a[j][k] -= (konst * a[i][k])
                

i=0
j=0
for i in range(n):
        for j in range(nn):
            if (a[i][j] == -0): 
                a[i][j]=0
                

i=0
j=0
print ("\nMatriks Baru")
for i in range(n):
   for j in range(nn):
       if (j != n):
           print ("%.2f "% (a[i][j]), end="")
           
       else:
           print ("| %.2f"% (a[i][j]))
