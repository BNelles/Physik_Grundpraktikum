import matplotlib.pyplot as plt
import numpy as np

fig, ax=plt.subplots()
d,I=np.genfromtxt("data1.txt", unpack=True)
x=np.linspace(3.5,8)
params, covariance_matrix = np.polyfit(d, I, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

ax.plot(d,I,"o")
ax.plot(
    x,
    params[0]*x+params[1],
    "--r",
    label="Lineare Regression"
)
ax.legend()
print(params)
print(errors)
fig.savefig("plot1.pdf")