import matplotlib.pyplot as plt
import numpy as np

f1,A1=np.genfromtxt("data1.txt",unpack=True)
f2,A2=np.genfromtxt("data2.txt",unpack=True)
f3,A3=np.genfromtxt("data3.txt",unpack=True)
f_Q,U_Q=np.genfromtxt("data1t.txt",unpack=True)
f_S,U_S=np.genfromtxt("data2t.txt",unpack=True)
f_D,U_D=np.genfromtxt("data3t.txt",unpack=True)

fig, (ax1, ax2, ax3)=plt.subplots(3,1,layout="constrained")

b1=10**(A1/20)
b2=10**(A2/20)
b3=10**(A3/20)
ax1.set_title(r"$Quadratschwingung$")
ax2.set_title(r"$Sägezahnschwingung$")
ax3.set_title(r"$Dreiecksspannung$")

ax1.set_xlabel(r"$f/kHz$")
ax2.set_xlabel(r"$f/kHz$")
ax3.set_xlabel(r"$f/kHz$")
ax1.set_ylabel(r"$U/V$")
ax2.set_ylabel(r"$U/V$")
ax3.set_ylabel(r"$U/V$")

ax1.plot(
    f1,b1,"o",color='c',
    label=r"$experimentelle Daten$"
)
ax1.plot(
    f_Q,U_Q,"x",color='k',
    label=r"$theoretische Daten$"
)

ax2.plot(
    f2,b2,"o",color='c',
    label=r"$experimentelle Daten$"
)
ax2.plot(
    f_S,U_S,"x",color='k',
    label=r"$theoretische Daten$"
)

ax3.plot(
    f3,b3,"o",color='c',
    label=r"$experimentelle Daten$"
)
ax3.plot(
    f_D,U_D,"x",color='k',
    label=r"$theoretische Daten$"
)

plt.figure().set_figheight(3)

ax1.legend()
ax2.legend()
ax3.legend()
fig.savefig("plot1.pdf")