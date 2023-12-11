import matplotlib.pyplot as plt
import numpy as np

f1,A1=np.genfromtxt("data1.txt",unpack=True)
f2,A2=np.genfromtxt("data2.txt",unpack=True)
f3,A3=np.genfromtxt("data3.txt",unpack=True)
f,U=np.genfromtxt("data4.txt",unpack=True)

fig, ax=plt.subplots()

b1=10**(A1/20)
b2=10**(A2/20)
b3=10**(A3/20)


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