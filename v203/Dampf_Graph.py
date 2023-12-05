import matplotlib.pyplot as plt
import numpy as np

A,p = np.genfromtxt("data2.txt", unpack=True)
T=A+273.15
fig1, ax1=plt.subplots()
x=np.linspace(375,500,10)
k,cov1=np.polyfit(T,p,deg=3,cov=True)
unc=np.sqrt(np.diag(cov1))
f=np.poly1d(k)
y=f(x)

ax1.set(
    xlabel=r"$T/°K$",
    ylabel=r"$p/bar$",
)
ax1.plot(T,p,"o")
ax1.plot(x,y,"r--")
print(k,unc)
fig1.savefig("plot2.pdf")


e=k[0]
f=k[1]
g=k[2]
h=k[3]
z=np.linspace(380,480,10)

def L(xx,a,b,c,d):
    return (3*a*xx**3+2*b*xx**2+c*x)/(a*xx**3+b*xx**2+c*xx+d)*((8.32*xx)/2+np.sqrt(((8.32*xx)/2)**2-0.9*(a*xx**3+b*xx**2+c*xx+d)))


fig2, ax2=plt.subplots()
ax2.cla()
ax2.set(
    xlabel=r"$T/°K$",
    ylabel=r"$L/ \frac{J}{mol}$",
)
ax2.plot(z,L(z,e,f,g,h))
fig2.savefig("plot3.pdf")

def l(xx,a,b,c,d):
    return (3*a*xx**3+2*b*xx**2+c*x)/(a*xx**3+b*xx**2+c*xx+d)*((8.32*xx)/2-np.sqrt(((8.32*xx)/2)**2-0.9*(a*xx**3+b*xx**2+c*xx+d)))

fig3, ax3=plt.subplots()
ax3.cla()
ax3.set(
    xlabel=r"$T/°K$",
    ylabel=r"$L/ \dfrac{J}{mol}$",
)
ax3.plot(z,l(z,e,f,g,h))
fig3.savefig("plot4.pdf")