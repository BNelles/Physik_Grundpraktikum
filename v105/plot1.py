import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unp
import scipy.constants as const

fig, ax=plt.subplots()
d,I=np.genfromtxt("data1.txt", unpack=True)
x=np.linspace(3.5,8)
params, covariance_matrix = np.polyfit(d, I, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

ax.plot(d,I,"o")
ax.set(
        xlabel=r"$d \mathbin{/} \unit{\meter}$",
        ylabel=r"$I \mathbin{/} \unit{\ampere}$",
        )
ax.plot(
    x,
    params[0]*x+params[1],
    "--r",
    label="Lineare Regression"
    )
ax.legend()
#print(params)
#print(errors)
fig.savefig("plot1.pdf")

a=unp.ufloat(0.19*10**(2),0.006*10**(2))
n=const.mu_0
g=const.g
m=(0.0014*g*(0.109**2+(0.138/2)**2)**(3/2))/(n*195*0.109**2*a)
#print(m)

I2,t=np.genfromtxt("data2.txt", unpack=True)
fig2, ax2=plt.subplots()
T=t/10
B=(195*n*0.109**2)/(((0.138/2)**2+0.109**2)**(3/2))*I2
ax2.plot(1/B,T**2,"o")
ax2.set(
        xlabel=r"$\frac{1}{B} \mathbin{/} \unit{\per\tesla}$",
        ylabel=r"$T^2 \mathbin{/} \unit{\second\squared}$",
        )

C=1/B
V=T**2

params2, covariance_matrix = np.polyfit(C, V, deg=1, cov=True)
errors2 = np.sqrt(np.diag(covariance_matrix))
y=np.linspace(200,500)

ax2.plot(
    y,
    params2[0]*y+params2[1],
    "--r",
    label="Lineare Regression"
)
ax2.legend()

fig2.savefig("plot2.pdf")
a2=unp.ufloat(params2[0],errors2[0])
m2=(4*(np.pi**2)*3.7*10**(-5))/a2
#print(m2)
#print(a2)
#print(params2[1], errors2[1])#
#print((195*n*0.109**2)/(((0.138/2)**2+0.109**2))**(3/2))