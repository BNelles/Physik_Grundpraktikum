import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const


def sigma(e):
        re=2.82*10**(-15)
        return 2*np.pi*re*2*((1+e)/(2*e)*(2*(1+e)/(1+2*e)-1/e*np.log(1+2*e))+1/(2*e)*np.log(1+2*e)-(1+3*e)/((1+2*e)**2))

def mu(z,V,s):
        return (const.N_A*z*s)/V
#print(const.N_A)
#e1=1.295
e2=2.45
#Eisen
ze=26
Ve=7.09*10**(-6)
#se1=sigma(e1)
se2=sigma(e2)
#print(se1)
#me1=mu(ze,Ve,se1)
me2=mu(ze,Ve,se2)
#print(me2)


#Aluminium
za=13
Va=10**(-5)
sa2=sigma(e2)
me2=mu(za,Va,sa2)
#print(me2)








