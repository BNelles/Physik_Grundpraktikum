import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat


cA=ufloat(2862,91)
t_A=ufloat(5.2,1.3)*10**(-3)

t1=70.17*10**(-6)-t_A/cA
t2=17.51*10**(-6)-t_A/cA
t3=11.56*10**(-6)-t_A/cA
t4=7.57*10**(-6)-t_A/cA

cL=2500
cGK=1410


I=cGK*t4*10**3
L1=cGK*t3*10**3

L2=L1+(t2-t3)*cL*10**3

R=cGK*(t1-t2)*10**3+L2

print(I,L1,L2,R)