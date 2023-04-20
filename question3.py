# Itai Zaretsky 205946114

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as const
from sklearn.linear_model import LinearRegression
import sympy as sp
k = const.Boltzmann * 6.25e18
e = const.elementary_charge
m_0 = const.electron_mass
h = const.h


def calc_energy(t):
    temperature = np.array([1/(15+273), 1/(30+273), 1/(80+273), 1/(110+273), 1/(125+273),
    1/(160+273), 1/(175+273),  1/(195+273)]).reshape(-1, 1)
    resistance = [7180, 3170, 345, 120, 75, 28.5, 20, 12.5]
    resistance = [sp.ln(r) for r in resistance]
    model = LinearRegression()
    model.fit(temperature, resistance)
    slope = model.coef_[0]
    e_g = slope*2*k
    rho = sp.exp(slope/t)*sp.exp(model.intercept_)
    print("The Band Gap is: Eg =", round(e_g, 3), "[eV]")
    calc_mobility(t, slope, e_g, rho)


def calc_mobility(t, slope, e_g, rho):
    nc = 2*((2*np.pi*0.18*m_0*1.38e-23*t)/(h**2))**(3/2)
    nc_t = nc/100**3
    nv = 2*((2*np.pi*0.37*m_0*1.38e-23*t)/(h**2))**(3/2)
    nv_t = nv/100**3
    ni_t = np.sqrt(nc_t*nv_t)*np.exp(-e_g/(2*k*t))
    mu_p = 1100*(t/300)**(-3/2)
    sigma = 1/rho
    mu_n = (sigma-(e*ni_t*mu_p))/(e*ni_t)
    print("The electron mobility is: Mu_n =", round(mu_n, 3), "[cm^2/Vs]")
    calc_electron_d(t, mu_n)
    print("The Conduction Band Density of States is: Nc =", nc_t, "[cm^-3]")
    print("The Valence Band Density of States is: Nv =", nv_t, "[cm^-3]")


def calc_electron_d(t, mu_n):
    d_n = (1.38e-23*t*mu_n)/e
    print("The electron Diffusion Coefficient is: D =", round(d_n, 3), "[cm^2/s]")


def menu():
    while 1:
        print("Enter Temperature in [K]:")
        t = int(input())
        if t < 0:
            print("Try Again! Temperature must be positive.")
        else:
            break
    calc_energy(t)


menu()

