import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#def diffquotient(a,b,c):
#    return (a-b)/(c)
#
#t1,f1=np.genfromtxt("data1.txt", unpack=True)
#t2,f2=np.genfromtxt("data2.txt", unpack=True)
#
#T1=f1+273.15
#T2=f2+273.15
#
#print(diffquotient(T1[4],T1[0],4))
#print(diffquotient(T1[8],T1[0],8))
#print(diffquotient(T1[12],T1[0],12))
#print(diffquotient(T1[16],T1[0],12))
t=4
for t in range(4,20,4):
    A=ufloat(-6.155e-6,0.22e-6)
    B=ufloat(0.02742,0.00033)

    X=ufloat(4.122e-6,0.249e-6)
    Y=ufloat(0.02078,0.00037)

    D=2*X*t*60+Y
    print(D)
    t+4
