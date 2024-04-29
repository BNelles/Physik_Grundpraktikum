import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import scipy.constants as const

I_q,s=np.genfromtxt("data/Querstrom.txt",unpack=True)

D_s=0.5*(s[0]+s[-1])
print(D_s)
U_s=s-D_s
U_s=U_s*10**(-3)
params, covariance_matrixs = np.polyfit(I_q, U_s, deg=1, cov=True)
uncertainties = np.sqrt(np.diag(covariance_matrixs))

fig, (s) = plt.subplots(1, 1, layout="constrained")
s.plot(I_q, U_s,"." ,label="Kurve")
s.set_xlabel(r"$I_1 \mathbin{/} \unit{\milli\tesla}$")
s.set_ylabel(r"$U_H \mathbin{/} \unit{\milli\volt}$")
s.legend(loc="best")

s.plot(
    I_q,
    params[0] * I_q + params[1],
    label="Lineare Regression",
    linewidth=2,
)

fig.savefig("build/quer.pdf")

m=ufloat(params[0],uncertainties[0])
n=-(349.5*10**(-3))/(0.263*10**(-3)*m*const.e)

n_0=ufloat(-1.11e28,0.04e28)

A=(n_0-n)/n
print(A)

