import matplotlib.pyplot as plt
import numpy as np

def diffquotient(a,b,c):
    return (a-b)/(c)

t1,f1=np.genfromtxt("data1.txt", unpack=True)
t2,f2=np.genfromtxt("data2.txt", unpack=True)

T1=f1+273.15
T2=f2+273.15

print(diffquotient(T1[4],T1[0],4))
print(diffquotient(T1[8],T1[0],8))
print(diffquotient(T1[12],T1[0],12))
print(diffquotient(T1[16],T1[0],12))
