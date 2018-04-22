# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 11:42:16 2018

@author: azmijuhda
"""
import math
import os
def tabel():
    print "\n==== METODE TABEL ===="
    print "f(x) = x*exp(-x)+(cos(2*x))\n"
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
        
    yatdk = raw_input("\nKembali ke menu [y/t] ? > ")
    if (yatdk == "y" or yatdk == "Y") :
        os.system('clear')
        menu()
    else :
        exit(0)


def biseksi():
    def f(x):
        fx = x*math.exp(-x)+(math.cos(2*x))
        return fx
    
    print "\n==== METODE BISEKSI ===="
    print "f(x) = x*exp(-x)+(cos(2*x))\n"
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
        fxr = f(xr)
        
        print "%d\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f" % (iterasi, a, b, xr, fxr, fa)
        if( fa* fxr < 0 ):
            b = xr
        elif ( fa* fxr > 0 ):
            a = xr
            fa = fxr
        
        if (math.fabs(a - b) < e or iterasi > n):
            break
    print("-------------------------------------------------")
    print "Akar = %.4f" % (xr)
    yatdk = raw_input("\nKembali ke menu [y/t] ? > ")
    if (yatdk == "y" or yatdk == "Y") :
        os.system('clear')
        menu()
    else :
        exit(0)


def regula():
    def f(x):
        fx = x*math.exp(-x)+(math.cos(2*x))
        return fx
    
    print "\n==== METODE REGULA FALSI ===="
    print "f(x) = x*exp(-x)+(cos(2*x))\n"    
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
    yatdk = raw_input("\nKembali ke menu [y/t] ? > ")
    if (yatdk == "y" or yatdk == "Y") :
        os.system('clear')
        menu()
    else :
        exit(0)


def iterasisederhana():
    def f(x) :
        fx = math.exp(-x)-x
        return fx
    
    def gx(x):
        gx = math.exp(-x)
        return gx
        
    print "\n==== METODE ITERASI SEDERHANA ===="
    print "f(x) = exp(-x)-x"
    print "g(x) = exp(-x)\n"
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
    yatdk = raw_input("\nKembali ke menu [y/t] ? > ")
    if (yatdk == "y" or yatdk == "Y") :
        os.system('clear')
        menu()
    else :
        exit(0)


def nr():
    def f(x) :
        fx = x*math.exp(-x)+(math.cos(2*x))
        return fx

    def ft(x) :
        ft = (1-x)*math.exp(-x)-(2*math.sin(2*x))
        return ft
    
    print "\n==== METODE NEWTON RAPHSON ===="
    print "f(x) = x*exp(-x)+(cos(2*x))"
    print "f(x) = (1-x)*exp(-x)-(2*sin(2*x))\n"
    
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
    yatdk = raw_input("\nKembali ke menu [y/t] ? > ")
    if (yatdk == "y" or yatdk == "Y") :
        os.system('clear')
        menu()
    else :
        exit(0)
    

def secant():
    def f(x) :
        fx = x*math.exp(-x)+math.cos(2*x)
        return fx

    print "\n==== METODE SECANT ===="
    print "f(x) = x*exp(-x)+(cos(2*x))\n"
    
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
    yatdk = raw_input("\nKembali ke menu [y/t] ? > ")
    if (yatdk == "y" or yatdk == "Y") :
        os.system('clear')
        menu()
    else :
        exit(0)
    

def menu():
    print ""    
    print "     ╔╦╗╔═╗╔╦╗╔═╗╔╦╗╔═╗  ╔╗╔╦ ╦╔╦╗╔═╗╦═╗╦╦╔═"
    print "  ══ ║║║║╣  ║ ║ ║ ║║║╣   ║║║║ ║║║║║╣ ╠╦╝║╠╩╗  ══"
    print "     ╩ ╩╚═╝ ╩ ╚═╝═╩╝╚═╝  ╝╚╝╚═╝╩ ╩╚═╝╩╚═╩╩ ╩"
    print ""
    print "Menu : "
    print "1. Tabel"
    print "2. Biseksi"
    print "3. Regula Falsi"
    print "4. Iterasi Sederhana"
    print "5. Newton Raphson"
    print "6. Secant"
    print "7. Keluar Program"
    
    menu = raw_input("Pilih menu (1-7) : ")
    if (menu == "1"):
        os.system('clear')
        tabel()
    elif (menu == "2"):
        os.system('clear')
        biseksi()
    elif (menu == "3"):
        os.system('clear')
        regula()
    elif (menu == "4"):
        os.system('clear')
        iterasisederhana()
    elif (menu == "5"):
        os.system('clear')
        nr()
    elif (menu == "6"):
        os.system('clear')
        secant()
    elif (menu == "7"):
        print "\n- TERIMA KASIH -"
        os.system('sleep 2')
        os.system('clear')
        exit(0)
    else:
        print "Tidak ada menu !"


if __name__ == "__main__" :
    while(True):
        menu()
    
