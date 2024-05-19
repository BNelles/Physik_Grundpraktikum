import matplotlib.pyplot as plt
import numpy as np

#U,n1,n2=np.genfromtxt("data/data2.txt",unpack=True)
U=550
N1=158675/120
N2=142577/120
N12=264863/120
t=(N1+N2-N12)/(2*N1*N2)
print(N1,N2,N12)