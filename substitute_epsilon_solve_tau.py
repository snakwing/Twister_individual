# -*- coding: utf-8 -*-
"""

After setting both the partial derivatives of the total energy
expression to zero, substituting the expression for epsilon
from the first into the second expression and solving for tau

@author: Stephanie Buchanan
"""

import sympy
from sympy import Eq, simplify 

# Define the symbols used
E, epsilon, A_c, A_w, tau, J_c_2, J_w_2, J_c_4, J_w_4, K, G, epsilon_pre, nu = sympy.symbols("E epsilon A_c A_w tau J_c_2 J_w_2 J_c_4 J_w_4 K G epsilon_pre nu")

# Define the expression for epsilon
epsilon_expr = (-A_c*2*epsilon_pre - tau**2*(J_c_2+J_w_2))/(2*(A_c+A_w))

# Define the expression for the partial derivative of the total energy function w.r.t. tau
dE_dtau = (E*0.5)*(2*tau*J_c_2*(epsilon+epsilon_pre)+(tau**3)*J_c_4+2*epsilon*tau*J_w_2+(tau**3)*J_w_4)+ G*K*tau

# Substitute epsilon into dE/dtau
dE_dtau_with_epsilon = dE_dtau.subs(epsilon, epsilon_expr)

# Define the conversion between shear modulus G and Young's modulus E
G_expr = E/(2*(1+nu))

# Substitute this into dE_dtau_with_epsilon
dE_dtau_with_epsilon_G_subbed = dE_dtau_with_epsilon.subs(G, G_expr)

# Simplify the expression after substitution
dE_dtau_with_epsilon_G_subbed = simplify(dE_dtau_with_epsilon_G_subbed)

# Print the expression
print('dE/dtau with epsilon substituted: ')
sympy.pprint(dE_dtau_with_epsilon_G_subbed)

# Set the expression to zero and solve for tau
tau_solutions = sympy.solve(Eq(dE_dtau_with_epsilon_G_subbed, 0), tau)

#Print the solutions for tau
print("Tau solutions:", tau_solutions)
