def npublica(p,q):
    n=p*q
    return (n)

def opublica(p,q):
    o=(p-1)*(q-1)
    return (o)

def gcd(e,n):
    while n>0:
        e,n=n,e%n
        pass
    return e

def eclave(o):

    e = 2
    while gcd(e,o) !=1:
        e+=1
        return e

def dclave(e, m):
    x = lasty = 0
    lastx = y = 1
    while m != 0:
        q = e // m
        e, m = m, e % m
        x, lastx = lastx - q*x, x
        y, lasty = lasty - q*y, y
    return lastx


def clave(p,q):
    n=npublica(p,q)
    o=opublica(p,q)
    e=eclave(o)

    d = dclave(e, o)
    while d < 0:
        d += o
    print('p 2579 a 2 aa76 b 949')
    return [n, e, d]

def c_relleno(list1):
    lista = []
    rango = len(list1)
    if rango >3:
        for m in range (3):
            lista.append(list1[m])
    elif rango ==3:
        return list1
    elif rango < 3:
        for m in range (rango):
            lista.append(list1[m])
        for m in range (3-rango):
            if m ==1:
                m = rango
            lista.append('1')

    else:
        print ("tamano lista error menor que cero WDF!")
    return lista
def c_unir (list1,list2):
    lista = []
    rango1=len(list1)
    rango2=len(list2)
    rango = int(rango1+rango2)
    for m in range(rango):
        if (m) < (rango):
            lista.append(list1[m])
        elif (m) >= (rango):
            lista.append(list2[m-rango])
        else:
            print("paso algo inesperado ome")
    return lista

def mrsa(p,q,e,m,t):
    a,b,c=clave(p,q)

    b=e
    rango=len(m)
    salir=0
    list2=[]
    while salir <= rango:
        list1=[]

        for i in range (3):
            #i+=1
            #a=(i+salir)
            #print('i', i, 'i+salir',a)
            if(salir+i)>= rango:
                list1=c_relleno(list1)
            elif salir <= rango:
                list1.append(m[i+salir])
            else:
                print("algo paso error rango")


        salir+=3
        c=int(''.join(list1))

        if not c:
            return

        valor=(pow(c, b, a))
        list2.append(valor)

    return list2



def drsa(p,q,e,m,t):
    a,b,c=clave(p,q)

    b=e
    rango=len(m)
    list2=[]
    for z in range (rango):
        w=m[z]
        valor=(pow(w, c, a))
        list2.append(valor)
        if not c:
            return


#Main
p=2579
q=765
key=clave(p,q)
#print(key)
