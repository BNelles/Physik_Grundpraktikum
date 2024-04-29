import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties.umath import sqrt
from uncertainties.umath import pow
                                #Hallspannung
I_s,B_s,U_s=np.genfromtxt("data/silber.txt",unpack=True)
I_k,B_k,U_k=np.genfromtxt("data/kupfer.txt",unpack=True)
I_z,B_z,U_z=np.genfromtxt("data/zink.txt",unpack=True)

D_s=0.5*(U_s[0]-0.158)
U_s=U_s-D_s

D_k=0.5*(U_k[0]-0.335)
U_k=U_k-D_k

D_z=0.5*(U_z[0]+0.004)
U_z=U_z-D_z

params, covariance_matrixs = np.polyfit(B_s, U_s, deg=1, cov=True)
paramk, covariance_matrixk = np.polyfit(B_k, U_k, deg=1, cov=True)
paramz, covariance_matrixz = np.polyfit(B_z, U_z, deg=1, cov=True)

errors=np.sqrt(np.diag(covariance_matrixs))
errork=np.sqrt(np.diag(covariance_matrixk))
errorz=np.sqrt(np.diag(covariance_matrixz))
#print(params[0],errors[0])

s=ufloat(params[0],errors[0])
k=ufloat(paramk[0],errork[0])
z=ufloat(paramz[0],errorz[0])
                                
k=ufloat(0.104,0.001)
s=ufloat(0.263,0.001)
                                #spezifischer Widerstand
A_k=np.pi*(k/2)**2
A_s=np.pi*(s/2)**2

R_k=2.7050
R_s=0.6086

l_k=1.37
l_s=1.73

p_k=(A_k*R_k)/l_k*10**(-6)
p_s=(A_k*R_s)/l_s*10**(-6)

#print(const.e**2)
#print(p_k,p_s)
p_z=0.06*10**(-6)
                                #zu berechnende Variablen
def n(x):       #s,z,k
    return 10/((0.263*10**(-3))*x*(const.e))
def tau(x,y):   #n,p
    return 2*const.m_e/((const.e)**2*x*y)

def drift(x):   #n
    return -10**6/(x*const.e)

def µ(x):       #tau
    return (const.e)/(2*const.m_e)*x
def total(x):   #fermi
    return sqrt(2*x/const.m_e)
def weg(x,y):   #total,tau
    return x*y
def fermi(x):   #n
    return ((const.h)**2)/(2*const.m_e)*pow((3/(8*np.pi)*x)**2,(1/3))

#Silber
n_s=n(s)
tau_s=tau(n_s,p_s)
drift_s=drift(n_s)
mu_s=µ(tau_s)
E_s=fermi(n_s)
v_s=total(E_s)
l_s=weg(tau_s,v_s)
print("Silber:","n=",n_s,"tau=",tau_s,"v_d=",drift_s,"µ=",mu_s,"v_t=",v_s,"l=",l_s)

#Kupfer
n_k=n(k)
tau_k=tau(n_k,p_k)
drift_k=drift(n_k)
mu_k=µ(tau_k)
E_k=fermi(n_k)
v_k=total(E_k)
l_k=weg(tau_k,v_k)
print("Kupfer:","n=",n_k,"tau=",tau_k,"v_d=",drift_k,"µ=",mu_k,"v_t=",v_k,"l=",l_k)
#Zink
n_z=n(z)
tau_z=tau(n_z,p_z)
drift_z=drift(n_z)
mu_z=µ(tau_z)
E_z=fermi(n_z)
v_z=total(E_z)
l_z=weg(tau_z,v_z)
print("Zink:","n=",n_z,"tau=",tau_z,"v_d=",drift_z,"µ=",mu_z,"v_t=",v_z,"l=",l_z)