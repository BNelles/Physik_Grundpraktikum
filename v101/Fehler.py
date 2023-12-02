import numpy as np
x1,x2=np.genfromtxt("data_fig1.txt", unpack=True)
y1=np.mean(x1)
z1=np.std(x1, ddof=1) / np.sqrt(len(x1))
print(y1)
print(z1)
#I=((y/5)*(y/5)*0.02)/(4*np.pi*np.pi)
#print(I)
y2=np.mean(x2)
z2=np.std(x2, ddof=1) / np.sqrt(len(x2))

print(y2,z2)

d1,d2,d3,d4=np.genfromtxt("data_P.txt",unpack=True)/2
d_K=np.mean(d1)
d_O=np.mean(d2)
d_A=np.mean(d3)
d_B=np.mean(d4)

z_K=np.std(d1, ddof=1) / np.sqrt(len(d1/2))
z_O=np.std(d2, ddof=1) / np.sqrt(len(d2))
z_A=np.std(d3, ddof=1) / np.sqrt(len(d3))
z_B=np.std(d4, ddof=1) / np.sqrt(len(d4))
#print(d_K,d_O/2,d_A/2,d_B/2)
print(z_K,z_O,z_A,z_B)