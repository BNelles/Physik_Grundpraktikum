import matplotlib.pyplot as plt
import numpy as np

f1,A1=np.genfromtxt("data1.txt",unpack=True)
f2,A2=np.genfromtxt("data2.txt",unpack=True)
f3,A3=np.genfromtxt("data3.txt",unpack=True)

fig, ax=plt.subplots()

U1=10**(A1/20)

ax.plot(
    f1,
    A1,
    "o",
    color='b'
)
#ax.plot(    f1,    U1,"o",    color='r')
ax.plot(
    f2,
    A2,
    "o",
    color='r'
)
ax.plot(
    f3,
    A3,
    "o",
    color='g'
)
plt.show()