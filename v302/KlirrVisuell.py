import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,4*np.pi)
fig, ax=plt.subplots()

y1=np.sin(x)+0.87*np.sin(2*x)
y2=np.sin(x)
y3=np.sin(x)+0.1*np.sin(2*x)

ax.set(
    ylabel=r"$U[mV]$",
    xlabel=r"$t[s]$",
)

ax.plot(x,y1, label=r"$k=0.87$")
ax.plot(x,y2, label=r"$k=0$")
ax.plot(x,y3, label=r"$k=0.1$")

ax.legend()
