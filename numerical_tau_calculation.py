# -*- coding: utf-8 -*-
"""

Numerical calculation of tau

@author: Stephanie Buchanan

"""

import numpy
from numpy import sqrt


# Values used for the heights and widths of the core and wings
#     hc = 0.04    
#     wc = 0.01    
#     hw = 0.02    
#     ww = 0.005  

E = 1.25e6                        # Young's Modulus
epsilon_pre = 0.1                 # Pre-strain
nu = 0.45                         # Poisson's ratio
A_c = 0.0007                      # Area of the core
A_w = 0.0007                      # Total area of the wings
K = 3.420950723500016e-08         # Torsion constant (found using MATLAB code)
J_c_2 = 1.11667e-07               # Second moment of area for core (found using Mathematica code)
J_w_2 = 3.99792e-07               # Second moment of area for wings (found using Mathematica code)
J_c_4 = 2.74389e-11               # Fourth moment of area for core (found using Mathematica code)
J_w_4 = 2.58596e-10               # Fourth moment of area for wings (found using Mathematica code)
G = E/(2*(1+nu))                  # Shear Modulus



# Expression for tau obtained using 'substitute_epsilon_solve_tau.py'
tau = 1.4142135623731*sqrt((A_c*E*J_w_2*epsilon_pre - A_c*G*K - A_w*E*J_c_2*epsilon_pre - A_w*G*K)/(E*(A_c*J_c_4 + A_c*J_w_4 + A_w*J_c_4 + A_w*J_w_4 - J_c_2**2 - 2.0*J_c_2*J_w_2 - J_w_2**2)))
#tau = 1.4142135623731*sqrt((A_c*E*J_w_2*epsilon_pre - A_c*G*K - A_w*E*J_c_2*epsilon_pre - A_w*G*K)/(E*(2.0*A_c*J_c_4*epsilon_pre + A_c*J_c_4 + A_c*J_w_4 + 2.0*A_w*J_c_4*epsilon_pre + A_w*J_c_4 + A_w*J_w_4 - J_c_2**2 - 2.0*J_c_2*J_w_2 - J_w_2**2)))

print('The (positive) solution for twist per unit length, tau =', tau)
