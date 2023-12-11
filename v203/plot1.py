import numpy as np
import matplotlib.pyplot as plt

a,b= np.genfromtxt("data.txt", unpack=True)
x=1/(a+273.15)
y=np.log(b/0.993)
fig, ax=plt.subplots(1,1,layout="constrained")

ax.set(
    xlabel=r"$\dfrac{1}{T}/\dfrac{1}{K}$",
    ylabel=r"$\dfrac{log(p)}{p_0}$",
)
ax.plot(x,y,".k",label="Messwerte gesamt")
fig.savefig("plot1.pdf")