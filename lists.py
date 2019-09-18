#!/usr/bin/env python

# lists/tupels/indices

import sys, math

def a14():
    print("Arrays die dynamisch angelegt werden")

def a15():
    print("""
    erstes: x[0]
    drittes: x[2]
    letztes: x[-1]""")

def a16():
    print("3, 18, 3, 1")
    print('([11,22,33], "Nachts um zwei Uhr", None)')

def a17():
    print("print(a[0]), weil a nur eine zahl ist, kein tupel")
    print("c[1]=0, weil String nicht über indeces verändert werden kann")
    print("b[0]=3, weil tupel immutable sind")

def a18():
    print("t=(True,) und neu zuweisen mit t=(False,)")

def a19():
    print("Immutable und über indexe ansprechbar")

def a20(n):
    lebensmittel = {1000: "Kartoffeln",
                    1020: "Gurken",
                    720: "Bananen",
                    702: "Kiwis",
                    5000: "Schokolade",
                    5010: "Kartoffelchips"}
    print("Eingegeben: {}, dazu gehört {}.".format(n,lebensmittel[n] if n in lebensmittel else "Unbekannte Zahl"))

  
def a21():
    temp = int(input("Temperatur: "))
    if temp < 20:
        R=100
    elif 20<=temp<110:
        R=120-temp
    else:
        R=float("inf")
    print(R)

def a22():
    l=["hallo", "leute", "wie", "gehts", "um", 8] 
    [print(elem) for elem in l]
    print("reversed(l) für umgekehrte Reihenfolge")
    [print(elem) for elem in reversed(l)]

def a23():
    print("""
    Checkt letztes bit von zahl ob 1 oder 0, wenn 1 gib ungerade zurück
    Wenn gerade wird nichts zurück gegeben

    Erste print gibt None aus, zweite 0
    """)

def a24():
    def my_mod(a,b):
        x = a//b
        return a-x*b
    
    print("""
    def my_mod(a,b):
        x = a//b
        return = a-x*b
    """)
    print(my_mod(12,5))

def a25():
    def my_reverse(li):
        new_list = []
        for elem in li:
            new_list.insert(0,elem)
        return new_list

    print("""
    def my_reverse(li):
        new_list = []
        for elem in li:
            new_list.insert(0,elem)
        return new_list
    """)
    print(my_reverse([1,2,3,4,5,6,7,8,9]))

def a26():
    print("""
    Lokal, wenn sie innerhalb eines blocks definiert ist -> für gesamten block verfügbar
    Global, wenn sie außerhalb eines blocks definiert ist -> zb am anfang des scripts
    global wird benutzt wenn bekannt gemacht werden soll dass die eigentliche lokale variable global schon definiert wurde
    """)

def a27():
    def my_and(a,b):
        if a:
            return b
        else:
            return a

    def my_or(a,b):
        if a:
            return a
        else:
            return b
    
    print("""
    "Adam" or False and "Eva": {}
    ("Adam" or False) and "Eva" : {}
    "Adam" or (False and "Eva"): {}
    """.format(
        my_or("Adam", my_and(False, "Eva")),
        my_and(my_or("Adam", False), "Eva"),
        my_or("Adam", my_and(False, "Eva"))
    ))

def a28():
    lam_and = lambda a,b: b if a else a
    lam_or  = lambda a,b: a if a else b

    print("""
    lam_or("Adam", lam_and(False, "Eve")): {}
    ...
    """.format(
        lam_or("Adam", lam_and(False, "Eve"))
    ))

def a29():
    # aus tb_lambda.py 
    def foreach(f, *argus):
        res=[]
        for arg in argus: res.append(f(arg))
        return res 
    def my_sqrt(x): return x**0.5 
    
    res=foreach(math.sqrt, 1, 2, 3, 4)
    my_res=foreach(my_sqrt, 1, 2, 3, 4)
    lam_res = foreach(lambda x: x**0.5, 1, 2, 3, 4)

    print(res)
    print(my_res)
    print(lam_res)

def a30():
    print([math.sqrt(x) for x in [1,2,3,4]])
    print("[math.sqrt(x) for x in [1,2,3,4]]")

if __name__=="__main__":
    args = sys.argv[1:]
    if args:
        if args[0]=="14":
            a14()
        elif args[0]=="15":
            a15()
        elif args[0]=="16":
            a16()
        elif args[0]=="17":
            a17()
        elif args[0]=="18":
            a18()
        elif args[0]=="19":
            a19()
        elif args[0]=="20":
            a20(int(args[1]))
        elif args[0]=="21":
            a21()
        elif args[0]=="22":
            a22()
        elif args[0]=="23":
            a23()
        elif args[0]=="24":
            a24()
        elif args[0]=="25":
            a25()
        elif args[0]=="26":
            a26()
        elif args[0]=="27":
            a27()
        elif args[0]=="28":
            a28()
        elif args[0]=="29":
            a29()
        elif args[0]=="30":
            a30()