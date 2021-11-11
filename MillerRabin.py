import random

def exponenciacion(x,a,n):
    bin = []
    l = 0
    z = 1
    while a > 0:
        bin.append(a % 2)
        a = a // 2
        l = l + 1

    i = l - 1
    while i >= 0:
        z = (z*z) % n
        print("Columna 1: ",z,end="")
        if bin[i] == 1:
            z = (z*x) % n
            print("\tColumna 2: ",z)
        else:
            print()
        i = i - 1

    return z

def MillerRabin(n):
    m = n - 1
    k = 0
    while m % 2 == 0:
        m = m/2
        k = k + 1

    a = random.randint(1,n-1)
    b = exponenciacion(a,m,n)
    if b == 1:
        return True
    for i in range(k):
        if b == n-1:
            return True
        b = exponenciacion(b,2,n)
    return False

def primalidad(n):
    for x in range(10):
        if not MillerRabin(n):
            print("No es un primo")
            return
    print("Es un primo")
