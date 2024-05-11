import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import umath 
import uncertainties.unumpy as unp

t_f,t_s=np.genfromtxt("data.txt", unpack=True)
U=249
d=5*10**(-4)
p=1017*10**2
B=6.17*10**(-3)*(101325/760)*10**(-2)
#print(B)

rho=886
g=9.81
l=ufloat(7.6250,0.0051)*10**(-3)
E=U/l
n=1.834*10**(-5)

#Funktionen

def rad(vs,vf):
    return umath.sqrt(9/4*n/g*(vf-vs)/rho)
def ladung(vf,vs,r):
    return 3*np.pi*n*r*(vf+vs)/E
def korrektur(q,r):
    return q*umath.pow(1+B/(p*r),(-3/2))
#Teilchen1
t_f1=t_f[0:7]
t_s1=t_s[0:7]
v_f1=ufloat(np.mean(d/t_f1),np.std(d/t_f1))
v_s1=ufloat(np.mean(d/t_s1),np.std(d/t_s1))
#Teilchen2
#t_f2=t_f[7:12]
#t_s2=t_s[7:12]
#v_f2=ufloat(np.mean(d/t_f2),np.std(d/t_f2))
#v_s2=ufloat(np.mean(d/t_s2),np.std(d/t_s2))
#Teilchen3
t_f3=t_f[12:17]
t_s3=t_s[12:17]
v_f3=ufloat(np.mean(d/t_f3),np.std(d/t_f3))
v_s3=ufloat(np.mean(d/t_s3),np.std(d/t_s3))
#Teilchen4
t_f4=t_f[17:22]
t_s4=t_s[17:22]
v_f4=ufloat(np.mean(d/t_f4),np.std(d/t_f4))
v_s4=ufloat(np.mean(d/t_s4),np.std(d/t_s4))
#Teilchen5
t_f5=t_f[22:27]
t_s5=t_s[22:27]
v_f5=ufloat(np.mean(d/t_f5),np.std(d/t_f5))
v_s5=ufloat(np.mean(d/t_s5),np.std(d/t_s5))
#Teilchen6
t_f6=t_f[27:32]
t_s6=t_s[27:32]
v_f6=ufloat(np.mean(d/t_f6),np.std(d/t_f6))
v_s6=ufloat(np.mean(d/t_s6),np.std(d/t_s6))
#Teilchen7
t_f7=t_f[32:37]
t_s7=t_s[32:37]
v_f7=ufloat(np.mean(d/t_f7),np.std(d/t_f7))
v_s7=ufloat(np.mean(d/t_s7),np.std(d/t_s7))
#Teilchen8
t_f8=t_f[37:42]
t_s8=t_s[37:42]
v_f8=ufloat(np.mean(d/t_f8),np.std(d/t_f8))
v_s8=ufloat(np.mean(d/t_s8),np.std(d/t_s8))
#Teilchen9
t_f9=t_f[42:47]
t_s9=t_s[42:47]
v_f9=ufloat(np.mean(d/t_f9),np.std(d/t_f9))
v_s9=ufloat(np.mean(d/t_s9),np.std(d/t_s9))
#Teilchen10
t_f0=t_f[47:52]
t_s0=t_s[47:52]
v_f0=ufloat(np.mean(d/t_f0),np.std(d/t_f0))
v_s0=ufloat(np.mean(d/t_s0),np.std(d/t_s0))



#Bestimmung der Radien

r1=rad(v_s1,v_f1)
#r2=rad(v_s2,v_f2)  komplex
r3=rad(v_s3,v_f3)
r4=rad(v_s4,v_f4)
r5=rad(v_s5,v_f5)
r6=rad(v_s6,v_f6)
r7=rad(v_s7,v_f7)
r8=rad(v_s8,v_f8)  
r9=rad(v_s9,v_f9)
r0=rad(v_s0,v_f0)

#print(r1,r3,r4,r5,r6,r7,r8,r9,r0)


#Bestimmung q0

Q1=ladung(v_f1,v_s1,r1)
Q3=ladung(v_f3,v_s3,r3)
Q4=ladung(v_f4,v_s4,r4)
Q5=ladung(v_f5,v_s5,r5)
Q6=ladung(v_f6,v_s6,r6)
Q7=ladung(v_f7,v_s7,r7)
Q8=ladung(v_f8,v_s8,r8)
Q9=ladung(v_f9,v_s9,r9)
Q0=ladung(v_f0,v_s0,r0)


e1=korrektur(Q1,r1)
e3=korrektur(Q3,r3)
e4=korrektur(Q4,r4)
e5=korrektur(Q5,r5)
e6=korrektur(Q6,r6)
e7=korrektur(Q7,r7)
e8=korrektur(Q8,r8)
e9=korrektur(Q9,r9)
e0=korrektur(Q0,r0)

e=[e3,e4,e5,e6,e7,e8,e9,e0]

y=[3,4,5,6,7,8,9,10]

fig, ax=plt.subplots(1,1,layout="constrained")

ax.set_xlabel(r"Tröpfchennummer")
ax.set_ylabel(r"$q \mathbin{/} \unit{\coulomb}$")

ax.errorbar(y, unp.nominal_values(e), yerr=unp.std_devs(e), fmt="rx")
ax.set_yticks(np.arange(1.5*10**(-19),9.5*10**(-19),1*10**(-19)))
yTickPos,_ = plt.yticks()
yTickPos = yTickPos[:-1] 
ax.barh(yTickPos, [max(plt.xticks()[0])] * len(yTickPos), height=(10**(-19)), color=['b','w'])
#print(yTickPos)
#fig.savefig("build/Daten.pdf")

#print(e[7])
print((1.6*10**(-19)-e[7])/(1.6*10**(-19)))

F=96485.309
N=F/e[7]
#print(N)
Nt=6.02*10**23
print((Nt-N)/Nt)