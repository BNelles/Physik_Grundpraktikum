import numpy as np
import matplotlib.pyplot as plt

d,t,N=np.genfromtxt("data/data2",unpack=True)

n=N/t

fig, ax=plt.subplots(1,1,layout="constrained")

ax.plot(d,n,".k")
fig.savefig("aluminium.pdf")