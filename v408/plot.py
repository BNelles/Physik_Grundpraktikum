import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy
#from shapely.geometry import LineString

P_L,P_B,B= np.genfromtxt("data/data1.txt",unpack=True)
#P_L=unumpy.uarray(P_L,0.1)
#P_B=unumpy.uarray(P_B,0.1)
# B=unumpy.uarray(B,0.1)



P_G=25
G=3
V1=B/G

g=P_L-P_G
b=P_B-P_L

V2=b/g
V=(V2-V1)/(V1)*100

f=g*b/(g+b)

F=np.mean(f)
fo=np.std(f)

ff=ufloat(9.75,0.06)
Af=((ff-10)/10)*100
#for i in range (0,9):
n=np.zeros(10)

n1=np.zeros(2)
n2=np.zeros(2)
n3=np.zeros(2)
n4=np.zeros(2)
n5=np.zeros(2)
n6=np.zeros(2)
n7=np.zeros(2)
n8=np.zeros(2)
n9=np.zeros(2)
n10=np.zeros(2)
#print(F)

n1[0]=g[0]
n2[0]=g[1]
n3[0]=g[2]
n4[0]=g[3]
n5[0]=g[4]
n6[0]=g[5]
n7[0]=g[6]
n8[0]=g[7]
n9[0]=g[8]
n10[0]=g[9]

r1=np.zeros(2)
r2=np.zeros(2)
r3=np.zeros(2)
r4=np.zeros(2)
r5=np.zeros(2)
r6=np.zeros(2)
r7=np.zeros(2)
r8=np.zeros(2)
r9=np.zeros(2)
r10=np.zeros(2)

r1[1]=b[0]
r2[1]=b[1]
r3[1]=b[2]
r4[1]=b[3]
r5[1]=b[4]
r6[1]=b[5]
r7[1]=b[6]
r8[1]=b[7]
r9[1]=b[8]
r10[1]=b[9]

fig, (P_L) = plt.subplots(1, 1, layout="constrained")
P_L.plot(g, n,"x",  label="Gegenstandsweiten")
P_L.plot(n, b,"x", label="Bildweiten")
P_L.plot(n1, r1,"k-")
P_L.plot(n2, r2,"k-")
P_L.plot(n3, r3,"k-")
P_L.plot(n4, r4,"k-")
P_L.plot(n5, r5,"k-")
P_L.plot(n6, r6,"k-")
P_L.plot(n7, r7,"k-")
P_L.plot(n8, r8,"k-")
P_L.plot(n9, r9,"k-")
P_L.plot(n10, r10,"k-")
P_L.set_xlabel(r"$g \mathbin{/} \unit{\centi\meter}$")
P_L.set_ylabel(r"$b \mathbin{/} \unit{\centi\meter}$")
P_L.legend(loc="best")
plt.axis((0, 60, 0, 30))
P_L.set_xticks(np.arange(0, 60, 2))
P_L.set_yticks(np.arange(0, 30, 2))
#P_L.grid()
#line_1=LineString(np.column_stack(()))


fig.savefig("build/plot.pdf")
print(Af)