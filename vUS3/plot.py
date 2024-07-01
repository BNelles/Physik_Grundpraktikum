import matplotlib.pyplot as plt
import numpy as np

v,f1= np.genfromtxt("data/data1.txt",unpack=True)

a1=90-np.rad2deg(np.arcsin(np.sin(np.deg2rad(15))*18/27))
a2=90-np.rad2deg(np.arcsin(np.sin(np.deg2rad(30))*18/27))
a3=90-np.rad2deg(np.arcsin(np.sin(np.deg2rad(60))*18/27))


f1_15=f1[0:5]/(np.cos(np.deg2rad(a1)))

f1_30=f1[5:10]/(np.cos(np.deg2rad(a2)))

f1_60=f1[10:15]/(np.cos(np.deg2rad(a3)))






v1=(v[0:5]/(np.pi*(0.035**2)))*0.1/60

v2=(v[0:5]/(np.pi*(0.05**2)))*0.1/60
a=15
c=1800




fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(v1, f1_15,".", label="7mm und 15°")
#ax1.plot(v1,v1*params15[0]+params15[1],label="Fit")
#ax1.set_xlabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
#ax1.set_ylabel(r"$\frac{\increment \nu}{\cos{\alpha}} \mathbin{/} \unit{\hertz}$")
ax1.legend(loc="best")

ax1.plot(v1, f1_30,".", label="7mm und 30°")
#ax1.plot(v1,v1*params30[0]+params30[1],label="Fit")
#ax1.set_xlabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
#ax1.set_ylabel(r"$\frac{\increment \nu}{\cos{\alpha}} \mathbin{/} \unit{\hertz}$")
ax1.legend(loc="best")

ax1.plot(v1, f1_60,".", label="7mm und 60°")
#ax1.plot(v1,v1*params45[0]+params45[1],label="Fit")
#ax1.set_xlabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
#ax1.set_ylabel(r"$\frac{\increment \nu}{\cos{\alpha}} \mathbin{/} \unit{\hertz}$")
ax1.legend(loc="best")











f2_15=f1[15:20]/(np.cos(np.deg2rad(a1)))

f2_30=f1[20:25]/(np.cos(np.deg2rad(a2)))

f2_45=f1[25:30]/(np.cos(np.deg2rad(a3)))








a=15
c=1800


f_all=np.reshape(np.array([f1_15,f1_30,f1_60,f2_15,f2_30,f2_45]),30)

v_1=np.reshape(np.array([v1,v1,v1]),15)
v_2=np.reshape(np.array([v2,v2,v2]),15)

params,err=np.polyfit(v_1,f_all[0:15],deg=1,cov=True)
params2,err2=np.polyfit(v_2,f_all[15:30],deg=1,cov=True)
params3=(params+params2)/2

errr=(err+err2)/2
print(np.sqrt(np.diag(errr)))
STD=np.sqrt(np.diag(errr))
print(params3[0],STD[0])

x=np.linspace(0,3,15)
ax1.plot(v2, f2_15,".", label="16mm und 15°")
ax1.plot(x,x*params3[0]+params3[1],label="Fit")

ax1.set_xlabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
ax1.set_ylabel(r"$\frac{\increment \nu}{\cos{\alpha}} \mathbin{/} \unit{\hertz}$")
ax1.legend(loc="best")

ax1.plot(v2, f2_30,".", label="16mm und 30°")

ax1.set_xlabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
ax1.set_ylabel(r"$\frac{\increment \nu}{\cos{\alpha}} \mathbin{/} \unit{\hertz}$")
ax1.legend(loc="best")

ax1.plot(v2, f2_45,".", label="16mm und 60°")

ax1.set_xlabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
ax1.set_ylabel(r"$\frac{\increment \nu}{\cos{\alpha}} \mathbin{/} \unit{\hertz}$")
ax1.legend(loc="best")


#print(p2arams15[0],p2arams30[0],p2arams45[0])


fig.savefig("build/plot.pdf")