#!/usr/bin/env python

# This document contains the first easy excercises from the pyhton kurs

import sys

def a1():
    pass

def a2():
    pass

def a3():
    print("""
    3a              :   Nein
    Änderung        :   Ja
    ÄNDERUNG        :   Ja
    Mit,1           :   Nein
    Label$3         :   Nein
    Drei-fach-Wert  :   Nein (minus)"""
    )

def a4():
    print("""
    _ ist ein platzhalter für leere variablen, die nicht genutzt werden.
    ZB wenn eine funktion 2 werte zurück gibt, man aber nur einen benötigt:
    erster_wert, _ = funktion_xy()
    """)

def a5():
    print("""
    5/2         tipp: 2.5   float,  ergebnis: {} {}
    5//2        tipp: 2     int,    ergebnis: {} {}
    5 % 2       tipp: 1     int,    ergebnis: {} {}    
    5.5 % 2     tipp: 1.5   float,  ergebins: {} {}
    5.5 % 2.2   tipp: 1.1   float,  ergebins: {} {}
    3-3*2       tipp: 3     int,    ergebnis: {} {}
    (1+2)/3     tipp: 1     int,    ergebnis: {} {}
    3 & 2       tipp: True  bool,   ergebnis: {} {}
    3 | 2       tipp: True  bool,   ergebnis: {} {}
    not 0       tipp: True  bool,   ergebnis: {} {}
    2**2000     tipp: @@    int,    ergebnis: {} {}
    2.0**200    tipp: @@    float,  ergebnis: {} {}
    """.format(5/2,type(5/2),
                5//2,type(5//2),
                5%2, type(5%2),
                5.5%2,type(5.5%2),
                5.5%2.2,type(5.5%2.2),
                3-3*2,type(3-3*2),
                (1+2)/3, type((1+2)/3),
                3&2, type(3&2),
                3|2, type(3|2),
                not 0, type(not 0),
                2**2000,type(2**2000),
                2.0**200, type(2.0**200)
                ))

def a6():
    print("klammern > and > or > links nach rechts")
    print("'Adam' or False and 'Eva': {}".format("Adam" or False and "Eva"))
    print("('Adam' or False) and 'Eva': {}".format(("Adam" or False) and "Eva"))
    print("'Adam' or (False and 'Eva'): {}".format("Adam" or False and "Eva"))
    print("(False and 'Eva') unnötig, da and eh > or; nur für lesbarkeit sinnvoll")

def a7(a):
    print("(1<=a) and (a <=4): {}".format((1<=a) and (a <=4)))
    print("1<=a<=4: {}".format(1<=a<=4))
    print("a zwischen 1 und 4")
    print("1<=a<=4 ist gleichwertig")
    print("gilt auch für True/False")

def a8():
    print(u"\u221E"+" viele Lösungen")
    print("u'\\u221E'+' viele Lösungen'")

def a9():
    print("wert_1 wird 'Anmerkung' zugewiesen.")
    print("wert_2 wied '--- Lösung ---'")
    print("wert_3=kein_wert wirft error, weil var kein_wert nicht existiert")
    print("wert_4=7*'7'+8 wirft Error, weil string nicht mit zahlen rechnen kann")
    print("wert_4 gibt error, weil var nicht definiert wurde")

def a10(a,b):
    print("erg = 'a=%.1f, b=%.3f' % (a, b) : {}".format('a=%.1f, b=%.3f' % (a, b)))
    print("Mit fstring einfach a={:.1f}, b={:.3f}")

def a11(a,b):
    print("a/dez={}, b/dez={}, a/hex={}".format(a, b, hex(a)))

def a12():
    txt=7*"ABC"
    print("sliced with tct[2::3]: {}".format(txt[2::3]))

def a13():
    ET="Dxuitfe gsweeitrre diT leat"
    #ET=A[0]+B[0]+C[0]+A[1]+B[1]+C[1]+...+A[-1]+B[-1]+C[-1]
    print("Solution für A, B, C: A,B,C=[ET[i::3] for i in [0,1,2]]")
    print("Solution für OT: OT=''.join([ET[i::3] for i in [0,1,2]])")
    OT="".join([ET[i::3] for i in [0,1,2]])
    print("OT: %s" % OT)

if __name__=="__main__":
    args = sys.argv[1:]
    if args:
        if args[0]=="1":
            a1()
        elif args[0]=="2":
            a2()
        elif args[0]=="3":
            a3()
        elif args[0]=="4":
            a4()
        elif args[0]=="5":
            a5()
        elif args[0]=="6":
            a6()
        elif args[0]=="7":
            a7(int(args[1]))
        elif args[0]=="8":
            a8()
        elif args[0]=="9":
            a9()
        elif args[0]=="10":
            a10(int(args[1]),int(args[2]))
        elif args[0]=="11":
            a11(int(args[1]),int(args[2]))
        elif args[0]=="12":
            a12()
        elif args[0]=="13":
            a13()
