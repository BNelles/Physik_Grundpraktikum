import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,0.1)

fig, ax=plt.subplots()
ax.plot(x,0.003-0.1305*x*x)
fig.savefig("Eigenträgheit_PLot.pdf")