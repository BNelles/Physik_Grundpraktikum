import numpy as np
import matplotlib.pyplot as plt

x,y=np.genfromtxt("data.txt",unpack=True)


params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)


x_plot = np.linspace(0, 0.5)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, y, ".k", label="Messwerte")
ax.plot(
    x_plot,
    params[0] * x_plot + params[1],
    "--r",
    label="Lineare Regression",
    linewidth=1.5,
)
print(params[0])
ax.legend();
fig.savefig("plot.pdf")
