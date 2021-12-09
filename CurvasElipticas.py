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
        if bin[i] == 1:
            z = (z*x) % n
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
            return False
    return True

def invMul(r0,r1):
    if r1 < 0:
        r1 = r1%r0
    r2 = 1
    q = 0
    t0 = 0
    t1 = 1
    t2 = 0
    mod = r0

    p = 0

    while r2 != 0:
        q = r0 // r1
        r2 = r0-(q*r1)

        r0 = r1
        r1 = r2

        if r2 != 0:
            t2 = (t0-q*t1)%mod
            t0 = t1
            t1 = t2
    if r0 == 1:
        return t2
    return -1

"""Creación de un punto de la curva eliptica dado un punto"""
def unPunto(X,Y,a,p):
    delta = ((3*(X**2)+a)*invMul(p,2*Y))%p
    X1 = (delta**2-2*X)%p
    Y1 = (delta*(X-X1)-Y)%p
    return X1, Y1

"""Creación de un punto de la curva eliptica dado dos puntos"""
def dosPuntos(X1,Y1,X2,Y2,p):
    delta = ((Y2-Y1)*invMul(p,X2-X1))%p
    X3 = (delta**2-(X1+X2))%p
    Y3 = (delta*(X1-X3)-Y1)%p
    return X3,Y3

def CurvasElipticas():
    """
    a = 651
    b = 170
    p = 452701
    q = 113501
    aX0 = 55211
    aY0 = 443096
    K = 428301
    """

    """Pedir los valores a y b"""
    print("Ingrese un valor a")
    a = int(input())
    if a == 0:
        random.randint(4,1001)
        print("a: ",a)
    print("Ingrese un valor b")
    b = int(input())
    if b == 0:
        random.randint(2,1001)
        print("b: ",b)

    """Calculo de p"""
    p = (a**2) + (b**2)
    while not (primalidad(p) and p%4==1 and (a+b)%4==1):
        b = b+2
    print("p: ",p)

    """Calculo de q"""
    q = (p+1+2*a)//4
    while not (primalidad(q)):
        random.randint(4,1001)
        print("a: ",a)
        random.randint(2,1001)
        print("b: ",b)
        p = (a**2) + (b**2)
        while not (primalidad(p) and p%4==1 and (a+b)%4==1):
            b = b+2
        print("p: ",p)
        q = (p+1+2*a)/4
    print("q: ",q)

    """Pedir los valores X0 y Y0"""
    print("Ingrese un valor X0")
    aX0 = int(input())
    if aX0 == 0:
        random.randint(1,p)
        print("X0: ",aX0)
    print("Ingrese un valor Y0")
    aY0 = int(input())
    if aY0 == 0:
        random.randint(1,p)
        print("Y0: ",aY0)

    """Calculo de K"""
    K = ((aX0**3-aY0**2)*invMul(p,aX0))%p
    while not((K**((p-1)//4))%p != 1 and (K**((p-1)//2))%p == 1):
        random.randint(1,p)
        print("X0: ",aX0)
        random.randint(1,p)
        print("Y0: ",aY0)
        K = ((aX0**3-aY0**2)*invMul(p,aX0))%p
    print("K: ",K)

    """
    Convertir a binario q-1 e ir multiplicando los valores de
    X0 y Y0
    """
    X = aX0
    Y = aY0
    aX = []
    aY = []
    lc = []
    binario = bin(q-1)
    limite = len(binario)-1
    if binario[limite] == '1':
        aX.append(aX0)
        aY.append(aY0)
        lc.append(1)
    limite = limite - 1
    contador = 2
    while limite > 1:
        X,Y = unPunto(X,Y,-K,p)
        print(contador,"X0=(",X,",",Y,")")
        if binario[limite] == '1':
            aX.append(X)
            aY.append(Y)
            lc.append(contador)
        contador = contador*2
        limite = limite -1

    """
    Sumar todas las multiplicaciones correspondientes a los 1s
    del q-1 binario
    """
    while len(aX) > 1:
        X1 = aX.pop()
        X2 = aX.pop()
        n1 = lc.pop()
        Y1 = aY.pop()
        Y2 = aY.pop()
        n2 = lc.pop()
        X,Y = dosPuntos(X2,Y2,X1,Y1,p)
        su = n1 + n2
        print(su,"X0=(",X,",",Y,")")
        aX.append(X)
        aY.append(Y)
        lc.append(su)

    """Analizar el resultado"""
    X = aX.pop()
    Y = aY.pop()
    print("(",X,",",Y,")")
    if X == aX0 and Y == (-aY0%p):
        print("(X0,Y0) es un elemento generador")
    else:
        print("(X0,Y0) no es un elemento generador")

def multiplicarPunto(aX0,aY0,q,K,p):
    """
    Convertir a binario q-1 e ir multiplicando los valores de
    X0 y Y0
    """
    X = aX0
    Y = aY0
    aX = []
    aY = []
    lc = []
    binario = bin(q)
    limite = len(binario)-1
    if binario[limite] == '1':
        aX.append(aX0)
        aY.append(aY0)
        lc.append(1)
    limite = limite - 1
    contador = 2
    while limite > 1:
        X,Y = unPunto(X,Y,-K,p)
        print(contador,"X0=(",X,",",Y,")")
        if binario[limite] == '1':
            aX.append(X)
            aY.append(Y)
            lc.append(contador)
        contador = contador*2
        limite = limite -1

    """
    Sumar todas las multiplicaciones correspondientes a los 1s
    del q-1 binario
    """
    while len(aX) > 1:
        X1 = aX.pop()
        X2 = aX.pop()
        n1 = lc.pop()
        Y1 = aY.pop()
        Y2 = aY.pop()
        n2 = lc.pop()
        X,Y = dosPuntos(X2,Y2,X1,Y1,p)
        su = n1 + n2
        print(su,"X0=(",X,",",Y,")")
        aX.append(X)
        aY.append(Y)
        lc.append(su)

    """Analizar el resultado"""
    X = aX.pop()
    Y = aY.pop()
    print("(",X,",",Y,")")
