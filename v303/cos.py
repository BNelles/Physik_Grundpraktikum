import matplotlib.pyplot as plt
import numpy as np

x,y=np.genfromtxt('data1.txt',unpack=True)
m,n=np.genfromtxt('data2.txt',unpack=True)
b=2.96*np.cos((np.pi*x)/180)

A=(y-b)/b
B=(n-y)/y

print(B*100)