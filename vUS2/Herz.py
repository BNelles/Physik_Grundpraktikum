import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

h1,t=np.genfromtxt("data/Herz.txt",unpack=True)

h=75-44.21-h1
