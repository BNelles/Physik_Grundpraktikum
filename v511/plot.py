import matplotlib.pyplot as plt
import numpy as np


I_s,B_s,U_s=np.genfromtxt("data/silber.txt",unpack=True)
I_k,B_k,U_k=np.genfromtxt("data/kupfer.txt",unpack=True)
I_z,B_z,U_z=np.genfromtxt("data/zink.txt",unpack=True)


<<<<<<< HEAD
fig.savefig("build/plot.pdf")
||||||| 9713c04
fig.savefig("build/plot.pdf")
=======
params, covariance_matrixs = np.polyfit(B_s, U_s, deg=1, cov=True)
paramk, covariance_matrixk = np.polyfit(B_k, U_k, deg=1, cov=True)
paramz, covariance_matrixz = np.polyfit(B_z, U_z, deg=1, cov=True)


fig, (s, k, z) = plt.subplots(1, 3, layout="constrained")
s.plot(B_s, U_s,"." ,label="Kurve")
s.set_xlabel(r"$B \mathbin{/} \unit{\milli\tesla}$")
s.set_ylabel(r"$U_H \mathbin{/} \unit{\milli\volt}$")
s.legend(loc="best")


s.plot(
    B_s,
    params[0] * B_s + params[1],
    label="Lineare Regression",
    linewidth=3,
)

k.plot(B_k, U_k,".", label="Kurve")
k.set_xlabel(r"$B \mathbin{/} \unit{\milli\tesla}$")
k.set_ylabel(r"$U_H \mathbin{/} \unit{\milli\volt}$")
k.legend(loc="best")

k.plot(
    B_k,
    paramk[0] * B_k + paramk[1],
    label="Lineare Regression",
    linewidth=3,
)

z.plot(B_z, U_z,".", label="Kurve")
z.set_xlabel(r"$B \mathbin{/} \unit{\milli\tesla}$")
z.set_ylabel(r"$U_H \mathbin{/} \unit{\milli\volt}$")
z.legend(loc="best")

z.plot(
    B_z,
    paramz[0] * B_z + paramz[1],
    label="Lineare Regression",
    linewidth=3,
)



fig.savefig("build/plot.pdf")
>>>>>>> 12153f882c8ccb2183d582bf702baea0271e4d1b
