import matplotlib.pyplot as plt
import numpy as np

P_L,P_B,B= np.genfromtxt("data/data1.txt",unpack=True)
P_G=25
G=3
V1=B/G

g=P_L-P_G
b=P_B-P_L

V2=b/g
V=V2-V1

f=g*b/(g+b)


print(V1,V2,V)

# fig, (ax1, ax2) = plt.subplots(1, 2, layout="constrained")
# ax1.plot(g, y, label="Kurve")
# ax1.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
# ax1.set_ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
# ax1.legend(loc="best")
# 
# ax2.plot(x, y, label="Kurve")
# ax2.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
# ax2.set_ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
# ax2.legend(loc="best")
# 
# fig.savefig("build/plot.pdf")
