import numpy as np
from uncertainties import ufloat
import scipy.constants as const

def F(t,e):
    return(t-e)/t


#violet
Ut=ufloat(1.138,0.031)
Ue=1.130
print(F(Ut,Ue))
#blau
Ut=ufloat(0.966,0.029)
Ue=0.980
print(F(Ut,Ue))
#grün
Ut=ufloat(0.453,0.017)
Ue=0.546
print(F(Ut,Ue))
#orange
Ut=ufloat(0.280,0.014)
Ue=0.25
print(F(Ut,Ue))

#planck
h=(const.h)
he1=ufloat(6.176,0.357)*10**(-34)
he2=ufloat(6.217,0.411)*10**(-34)
print(F(he1,he2))
print(F(h,he1))
print(F(h,he2))