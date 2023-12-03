import numpy as np
import matplotlib.pyplot as plt

a,b=np.genfromtxt("data.txt",unpack=True)
x=a*a*0.0001
y=(b*b)/25

params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

x_plot = np.linspace(0, 0.09)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, y, ".k", label="Messwerte")
ax.plot(
    x_plot,
    params[0] * x_plot + params[1],
    "--r",
    label="Lineare Regression",
    linewidth=1.5,
)
ax.set(
    xlabel=r"$a^2[m^2]$",
    ylabel=r"$T^2[s^2]$",
)
print(params[0])
print(params[1])
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.3f} ± {error:.3f}")
ax.legend();
fig.savefig("plot.pdf")