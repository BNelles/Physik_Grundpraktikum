import matplotlib.pyplot as plt
import numpy as np

def brenn(x,y):
    return((y**2-x**2)/(4*y))

G=25

l1,l2,S=np.genfromtxt("data/data2.txt",unpack=True) #Daten ohne Filter

D=S-G
d=l2-l1
f=brenn(d,D)

#print(np.mean(f),np.std(f))

m1,m2,Sb=np.genfromtxt("data/data2_b.txt",unpack=True) #blauer Filter

E=Sb-G
e=m2-m1
fb=brenn(e,E)
#print(np.mean(fb),np.std(fb))

n1,n2,Sr=np.genfromtxt("data/data2_r.txt",unpack=True)  #roter Filter

H=Sr-G
h=n2-n1
fr=brenn(h,H)
print(np.mean(fr),np.std(fr))