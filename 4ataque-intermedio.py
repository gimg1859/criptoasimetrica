
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
    #aumento el e mientras  el gcd no sea 1
    e = 2
    while gcd(e,o) !=1:
        e+=1
        return e
#dclave basado de https://teampython.wordpress.com/
def dclave(e, m):
    x = lasty = 0
    lastx = y = 1
    while m != 0:
        #desde python 3 division entera //
        q = e // m
        e, m = m, e % m
        x, lastx = lastx - q*x, x
        y, lasty = lasty - q*y, y
    return lastx


def clave(p,q):
    #n: p*q 0:(p-1)*(q-1), e:coprimo de o, d:privada usando inv
    n=npublica(p,q)
    o=opublica(p,q)
    #e=eclave(o)
    e=79
    d = dclave(e, o)
    while d < 0:
        d += o
    #print("p",p,'q',q,'n=p*q',n,'o=(p-1)*(q-1)',o,'e',e,'d',d)
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
    #print ('relleno',lista)
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
    #print('a,b,c',a,b,c)
    b=e
    rango=len(m)
    salir=0
    #print('rango:',rango,'b',b)
    list2=[]
    while salir <= rango:
        list1=[]
        #list2=[]
        #print('list1:',list1,'salir:',salir,'rango:',rango)

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



        #print('list1',list1,'list2',list2,'len',(len(list2)))
        salir+=3
        c=int(''.join(list1))
        #print('str1 list1',str1)



        #c = int(input("Number to encode: "))

        if not c:
            return
        #print('c',c,'b',b,'a',a)
        valor=(pow(c, b, a))
        list2.append(valor)
        #print('list2',list2)
    return list2

def drsa(p,q,e,m,t):
    a,b,c=clave(p,q)
    #print('a,b,c',a,b,c)
    b=e
    rango=len(m)

    #print('rango:',rango,'b',b)
    list2=[]
    for z in range (rango):
        w=m[z]
        valor=(pow(w, c, a))
        list2.append(valor)



        #print('list2',list2,'len',(len(list2)))

        #c=int(''.join(list1))
        #print('str1 list1',str1)


        #c = int(input("Number to encode: "))

        if not c:
            return
        #print('c',c,'b',b,'a',a)

        #print('list2',list2)
    return list2

w=14
c=10
a=23
z1=(pow(w, c, a))
p=23
q=7
a=17
b=12
n,e,d=clave(p,q)
a1=(pow(a,z1,p))
b1=(pow(b,z1,p))
x1=(pow(z1,a,p))
y1=(pow(z1,b,p))
print('z1',z1,'n',n,'e',e,'d',d,'n',n,'e',e,'d',d,'a1',a1,'b1',b1,'x1',x1,'y1',y1)
