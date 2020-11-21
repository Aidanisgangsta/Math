import math
from decimal import getcontext, Decimal

def Leibniz():
    num = 1
    positive = True
    total = 0
    for _ in range(0, 100000):
        add = 1/num
        if positive == True:
            total += add
            positive = False
        else:
            total -= add
            positive = True
        num += 2
    print(total * 4)

def Chudnovsky():
    C = 426880*math.sqrt(10005)

def Riemann():
    total = 0
    for i in range(1, 100000):
        add = 1/(i**2)
        total += add
    pi = math.sqrt(6*total)
    print(pi)

def Ramanujan1(): # fix
    total = 0
    multiply = (2*math.sqrt(2))/9801
    for i in range(10):
        sigma = multiply * (math.factorial(4*i) * (1103 + (26309*i)) / ((math.factorial(i))**4) * (396**(4*i)))
        total += sigma
    pi = 1/total
    print(pi)


def spigot1(): #GOOD
    pi = Decimal(0)
    add = Decimal
    for i in range(100):
        a = Decimal(1/Decimal(16**i))
        print(a)
        b = Decimal(4/Decimal(8*i + 1))
        c = Decimal(2/Decimal(8*i + 4))
        d = Decimal(1/Decimal(8*i + 5))
        e = Decimal(1/Decimal(8*i + 6))
        add = Decimal((a) * ((b) - (c) - (d) - (e)))
        pi += add
    
    print("{0:.100f}".format(pi))

spigot1()