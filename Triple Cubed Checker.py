import sys

num = int(input("What number would you like to use?\n"))

incriment = 100
lastcap = 1
cap = 101

looper = True

while looper:
    for i in range(lastcap, cap+1):
        for x in range(lastcap, cap+1):
            for y in range(lastcap, cap+1):
                if i**3 + x**3 + y**3 == num:
                    print(f"Okay, the solution is {i}^3+{x}^3+{y}^3")
                    #looper = False
                if i**3 + x**3 - y**3 == num:
                    print(f"Okay, the solution is {i}^3+{x}^3-{y}^3")
                    #looper = False
                if i**3 - x**3 + y**3 == num:
                    print(f"Okay, the solution is {i}^3-{x}^3+{y}^3")
                    #looper = False
                if i**3 - x**3 - y**3 == num:
                    print(f"Okay, the solution is {i}^3-{x}^3-{y}^3")
                    #looper = False
                if i**3 - x**3 + y**3 == num:
                    print(f"Okay, the solution is {i}^3-{x}^3+{y}^3")
                    #looper = False
                if i**3 - x**3 - y**3 == num:
                    print(f"Okay, the solution is {i}^3-{x}^3-{y}^3")                
                    #looper = False
    print(cap)
    lastcap = cap
    cap += incriment