import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

t_f,t_s=np.genfromtxt("data.txt", unpack=True)
U=249
d=5*10**(-4)
T=22+274.15
#Teilchen1
t_f1=t_f[0:7]
t_s1=t_s[0:7]
#Teilchen2
t_f2=t_f[7:12]
t_s2=t_s[7:12]
#Teilchen3
t_f3=t_f[12:17]
t_s3=t_s[12:17]
#Teilchen4
t_f4=t_f[17:22]
t_s4=t_s[17:22]
#Teilchen5
t_f5=t_f[22:27]
t_s5=t_s[22:27]
#Teilchen6
t_f6=t_f[27:32]
t_s6=t_s[27:32]
#Teilchen7
t_f7=t_f[32:37]
t_s7=t_s[32:37]
#Teilchen8
t_f8=t_f[37:42]
t_f8=t_f[37:42]
#Teilchen9
t_f9=t_f[42:47]
t_s9=t_s[42:47]
#Teilchen10
t_f0=t_f[47:52]
t_s0=t_s[47:52]

v_f1=np.average(d/t_f1)
print(v_f1)
print(np.mean(d/t_f1))
fig, ax=plt.subplots(1,1,layout="constrained")

ax.plot(t_f,t_s,".k")
fig.savefig("Daten.pdf")
