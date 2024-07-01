import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,t,t2,d=np.genfromtxt("data/schall.txt",unpack=True)
t=t/2*10**(-6)
x=x*10**(-3)

fig, ax=plt.subplots(1,1,layout="constrained")

ax.plot(t,x,".",label="Messdaten")

params, covariance_matrix=np.polyfit(t,x,deg=1,cov=True)
errors=np.sqrt(np.diag(covariance_matrix))
#print(params[0],errors[0])
x_plot=np.linspace(0,0.00003,100)
ax.plot(x_plot,params[0]*x_plot+params[1],label="lineare Regression")
ax.set_xlabel(r"$\increment t_1 \text{/} \unit{\second}$")
ax.set_ylabel(r"$x_{\symup{A}} \text{/} \unit{\meter}$")

fig.savefig("build/schall.pdf")

#print(params[1]*10**3,errors[1]*10**3)
c=ufloat(params[0],errors[0])
xd=ufloat(params[1],errors[1])
t2=t2/2
d=d*10**(-3)
h=80*10**(-3)

x=c*t+xd
x2=c*t2*10**(-6)+xd
d2=h-(x+x2)
#print(x*10**3)
#print(d2*10**3)
#print((d2-d)/d*100)
