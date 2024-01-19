import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


x,y=np.genfromtxt('data2.txt',unpack=True)

def cos_func(times, amplitude, frequency):
    return amplitude * np.cos(frequency * times)

params, covariance = optimize.curve_fit(cos_func, x, y)

x_x=np.linspace(-10,370)
#y_y=2.96*np.cos((2*np.pi*x_x)/360)

fig, ax1 = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, y,"o", label="Messwerte")
ax1.plot(x_x, cos_func((2*np.pi*x_x)/360, params[0], params[1]),
        label='Ausgleichsfunktion')
#ax1.plot(x_x,y_y,label="Ausgleichsfunktion")
ax1.set_xlabel(r"$\varphi \mathbin{/} °$")
ax1.set_ylabel(r"$U_{out} \mathbin{/} \unit{\volt}$")
ax1.legend(loc="best")



fig.savefig("build/plot1.pdf")
