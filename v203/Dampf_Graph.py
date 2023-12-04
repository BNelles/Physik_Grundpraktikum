import matplotlib.pyplot as plt
import numpy as np

T,p = np.genfromtxt("data2.txt", unpack=True)
fig, ax=plt.subplots()
x=np.linspace(100,200,10)
k,cov1=np.polyfit(T,p,deg=3,cov=True)
unc=np.sqrt(np.diag(cov1))
f=np.poly1d(k)
y=f(x)

ax.set(
    xlabel=r"$T/°C$",
    ylabel=r"$p/bar$",
)
ax.plot(T,p,"o")
ax.plot(x,y,"r--")
print(k,unc)
fig.savefig("pk,lot2.pdf")