import numpy as np
from uncertainties import ufloat
import scipy.constants as const

def F(t,e):
    return(t-e)/t


#violet
Ut=ufloat(1.138,0.031)
Ue=1.130
#print(F(Ut,Ue))
#blau
Ut=ufloat(0.966,0.029)
Ue=0.980
#print(F(Ut,Ue))
#grün
Ut=ufloat(0.453,0.017)
Ue=0.546
#print(F(Ut,Ue))
#orange
Ut=ufloat(0.280,0.014)
Ue=0.25
#print(F(Ut,Ue))

#planck
h=(const.h)
he1=ufloat(6.176,0.357)*10**(-34)
he2=ufloat(6.217,0.411)*10**(-34)
#print(F(he1,he2))
#print(F(h,he1))
#print(F(h,he2))

print(const.epsilon_0,const.m_e,const.c,const.hbar)
print((const.e**2)/((8*np.pi*const.epsilon_0*const.m_e*const.c**2)))
print(((const.c**2*6*np.pi*const.epsilon_0*const.hbar)/(const.e**2))/const.c)