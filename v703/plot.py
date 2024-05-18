import matplotlib.pyplot as plt
import numpy as np

U,N=np.genfromtxt("data/data1.txt",unpack=True)
LN=np.log(N)


params, covariance_matrix = np.polyfit(U[0:-3], LN[0:-3], deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print(errors)

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(U, LN,".", label="Kennlinie")
ax.plot(U,params[0]*U+params[1], label="Ausgleichsgerade")
ax.set_xlabel(r"$U \mathbin{/} \unit{\volt}$")
ax.set_ylabel(r"$N$")
ax.legend(loc="best")




fig.savefig("build/plot.pdf")
