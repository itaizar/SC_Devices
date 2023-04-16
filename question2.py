import numpy as np
import matplotlib.pyplot as plt

from scipy import constants as const
import sympy as sp

# Question 2 - Si intrinsic concentration
me_si = 1.08
mh_si = 0.57
me_ge = 0.56
mh_ge = 0.29
eg_ge = 0.66
eg_si = 1.12
nc_si = 2.8e19
nv_si = 1.05e19
k = const.Boltzmann*6.25e18
T = sp.Symbol('T')
expr = sp.ln(sp.sqrt(nc_si * nv_si)/2.5e13)-(eg_si)/(2*k*T)
sol = sp.solve(expr, T)[0]
print("The temperature in which the Si concentration will be the same as Ge is:\n", round(sol, 3), "[K]")




