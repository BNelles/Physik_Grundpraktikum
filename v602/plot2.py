import matplotlib.pyplot as plt
import numpy as np

w1,Z1=np.genfromtxt("data/Brom.txt",unpack=True)
w1=w1/2
fig1, ax1=plt.subplots(1,1,layout='constrained')
ax1.set_xlabel(r"$\theta \text{/}°$")
ax1.set_ylabel(r"$R \text{/} \unit{\per\second}$")
ax1.plot(w1,Z1,".")
fig1.savefig("build/brom.pdf")


w2,Z2=np.genfromtxt("data/Gallium.txt",unpack=True)
w2=w2/2
fig2, ax2=plt.subplots(1,1,layout='constrained')
ax2.set_xlabel(r"$\theta \text{/}°$")
ax2.set_ylabel(r"$R \text{/} \unit{\per\second}$")
ax2.plot(w2,Z2,".")
fig2.savefig("build/gallium.pdf")


w3,Z3=np.genfromtxt("data/stromtium.txt",unpack=True)
w3=w3/2
fig3, ax3=plt.subplots(1,1,layout='constrained')
ax3.set_xlabel(r"$\theta \text{/}°$")
ax3.set_ylabel(r"$R \text{/} \unit{\per\second}$")
ax3.plot(w3,Z3,".")
fig3.savefig("build/strontium.pdf")


w4,Z4=np.genfromtxt("data/Zink.txt",unpack=True)
w4=w4/2
fig4, ax4=plt.subplots(1,1,layout='constrained')
ax4.set_xlabel(r"$\theta \text{/}°$")
ax4.set_ylabel(r"$R \text{/} \unit{\per\second}$")
ax4.plot(w4,Z4,".")
fig4.savefig("build/zink.pdf")


w5,Z5=np.genfromtxt("data/Zirkonium.txt",unpack=True)
w5=w5/2
fig5, ax5=plt.subplots(1,1,layout='constrained')
ax5.set_xlabel(r"$\theta \text{/}°$")
ax5.set_ylabel(r"$R \text{/} \unit{\per\second}$")
ax5.plot(w5,Z5,".")
fig5.savefig("build/zirkonium.pdf")