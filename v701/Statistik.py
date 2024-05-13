import matplotlib.pyplot as plt
import numpy as np

n,z=np.genfromtxt("data3.txt",unpack=True)
z_m=np.mean(z)
z_s=np.std(z)

print(z_m,z_s)