# -*- coding: utf-8 -*-
"""

Numerical calculation of tau

@author: Stephanie Buchanan

"""

import numpy as np

# Values used for the original heights and widths of the core and wings
##     hc = 0.04    
##     wc = 0.01    
##     hw = 0.02    
##     ww = 0.005  

epsilon_pre = 0.1                 # Pre-strain
nu = 0.45                         # Poisson's ratio
A_c = 0.0007                      # Area of the core
A_w = 0.0007                      # Total area of the wings
K = 3.420950723500016e-08         # Torsion constant (found using MATLAB code)
J_c_2 = 1.11667e-07               # Second moment of area for core (found using Mathematica code)
J_w_2 = 3.99792e-07               # Second moment of area for wings (found using Mathematica code)
J_c_4 = 2.74389e-11               # Fourth moment of area for core (found using Mathematica code)
J_w_4 = 2.58596e-10               # Fourth moment of area for wings (found using Mathematica code)

# Values used for the Thick widths design
##  hc = 0.04    
##  wc = 0.0125    
##  hw = 0.02    
##  ww = 0.00625  

#epsilon_pre = 0.1
#nu = 0.45
#A_c = 0.00084375
#A_w = 0.00084375
#K = 8.40774731437578E-08
#J_c_2 = 1.42285e-07
#J_w_2 = 4.98645e-07
#J_c_4 = 3.5629e-11
#J_w_4 = 3.34465e-10

# Values used for the Thin widths design
##   hc = 0.04    
##   wc = 0.005    
##   hw = 0.02    
##   ww = 0.0025  

# epsilon_pre = 0.051
# nu = 0.45
# A_c = 0.000375
# A_w = 0.000375
# K = 4.168233812155960e-09
# J_c_2 = 5.40625e-08
# J_w_2 = 2.03945e-07
# J_c_4 = 1.30247e-11
# J_w_4 = 1.2497e-10


# Expression for tau obtained using 'substitute_epsilon_solve_tau.py'
tau = np.sqrt((2.0*A_c*J_w_2*epsilon_pre*nu + 2.0*A_c*J_w_2*epsilon_pre - A_c*K - 2.0*A_w*J_c_2*epsilon_pre*nu - 2.0*A_w*J_c_2*epsilon_pre - A_w*K)/((nu + 1.0)*(A_c*J_c_4 + A_c*J_w_4 + A_w*J_c_4 + A_w*J_w_4 - J_c_2**2 - 2.0*J_c_2*J_w_2 - J_w_2**2)))

print('The (positive) solution for twist per unit length, tau =', tau)
