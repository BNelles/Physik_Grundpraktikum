import matplotlib.pyplot as plt
import numpy as np

n,z=np.genfromtxt("data/data3.txt",unpack=True)
z_m=np.mean(z)
z_s=np.std(z)

def poisson(x,k):
    return (x**k/np.prod(range(1,k+1)))*np.exp(-x)

fig, ax=plt.subplots(1,1,layout="constrained")

ax.hist(z,bins=100)
#bin_centers = z[:-1] + np.diff(z) / 2


fig.savefig("stat.pdf")