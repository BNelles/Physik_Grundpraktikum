import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy.polynomial import Chebyshev

I,x = np.genfromtxt("data/data1.txt",unpack=True)


fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, I, label="Spalt 1")
ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
ax1.set_ylabel(r"$Stromstärke \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")

#def poly(x, a, b, c,d,e):
#    return a*x^4+b*x^3+c*x^2+d*x+e
#
#params, covariance_matrix = curve_fit(poly, x, I)
#
#ax1.plot(x, poly(x, *params), "-", label="Sigmoid Fit")


#c = Chebyshev.fit(x, I, deg=10)
#
#
#ax1.plot(x, c(x), label="Fit")


fig.savefig("build/plot.pdf")
