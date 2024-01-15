import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#def diffquotient(a,b,c):
#    return (a-b)/(c)
#
#t1,f1=np.genfromtxt("data1.txt", unpack=True)
t2,f2=np.genfromtxt("data2.txt", unpack=True)
#
#T1=f1+273.15
T2=f2+273.15
#
#print(diffquotient(T1[4],T1[0],4))
#print(diffquotient(T1[8],T1[0],8))
#print(diffquotient(T1[12],T1[0],12))
#print(diffquotient(T1[16],T1[0],12))
t=4
N=115
for t in range(4,20,4):
    A=ufloat(-6.155e-6,0.22e-6)
    B=ufloat(0.02742,0.00033)

    X=ufloat(4.122e-6,0.249e-6)
    Y=ufloat(0.02078,0.00037)

    D=2*X*t*60+Y
    v=(1/N)*(3*4200+750)*D
 #   print(v)
    t+4

r=ufloat(2.72   ,   0.04)
t1=ufloat(25.9,0.1)
t2=ufloat(16.4,0.1)
i=(t1+273.15)/(t1-t2)
print(i) 
a=(i-r)/i
print(a*100)

#Massendurchsatz
L=ufloat(243,14)*0.01801528
m=r*125/L
print(m)
print(L)

#Kompressorleistung

def leistung(m,p1,p2,T):
    return 1/(1.14-1)*(p2*(p1/p2)**(1/1.14)-p1)*1/(5.51)*T/(273.15*p1)*m

m1=ufloat(78,5)
m2=ufloat(68,4)
m3=ufloat(57,4)
m4=ufloat(51.7,3.4)
print(leistung(m1,3.5,6,T2[4]))
print(leistung(m2,3,7,T2[8]))
print(leistung(m3,2.4,8,T2[12]))
print(leistung(m4,2.2,9,T2[16]))
