import numpy as np
import matplotlib.pyplot as plt

a,b=np.genfromtxt("data1.txt",unpack=True)
x=1/(a+273.15)
y=np.log(b/0.993)



params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

x_plot = np.linspace(1/386.15,1/291.15)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, y, ".k", label="Messwerte p<1bar")
ax.plot(
    x_plot,
    params[0] * x_plot + params[1],
    "--b",
    label="Lineare Regression",
    linewidth=1.5,
)
ax.set(
    xlabel=r"$\dfrac{1}{T}/\dfrac{1}{K}$",
    ylabel=r"$\dfrac{log(p)}{p_0}$",
)
print(params[0])
print(params[1])
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.3f} ± {error:.3f}")
ax.legend();
fig.savefig("plot.pdf")