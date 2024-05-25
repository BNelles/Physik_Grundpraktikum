import numpy as np
import matplotlib.pyplot as plt

d,t,N=np.genfromtxt("data/data1.txt", unpack=True)

h=971/900
n=N/t-h

fig, ax=plt.subplots(1,1,layout="constrained")

ax.plot(d,n,".k")
fig.savefig("eisen.pdf")
