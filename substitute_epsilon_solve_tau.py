# -*- coding: utf-8 -*-
"""

After setting both the partial derivatives of the total energy
expression to zero, substituting the expression for epsilon
from the first into the second expression and solving for tau

@author: Stephanie Buchanan
"""

import sympy
from sympy import Eq, symbols, simplify 

# Define the symbols used
E, epsilon, A_c, A_w, tau, J_c_2, J_w_2, J_c_4, J_w_4, K, G, epsilon_pre = sympy.symbols("E epsilon A_c A_w tau J_c_2 J_w_2 J_c_4 J_w_4 K G epsilon_pre")

# Define the expression for epsilon
epsilon_expr = (-A_c*2*epsilon_pre - tau**2*(J_c_2+J_w_2))/(2*(A_c+A_w))

# Define the expression for the partial derivative of the total energy function w.r.t. tau
dE_dtau = (E*0.5)*(2*tau*J_c_2*(epsilon+epsilon_pre)+4*(tau**3)*J_c_4*(0.25+0.5*epsilon_pre)+2*epsilon*tau*J_w_2+(tau**3)*J_w_4)+ G*K*tau

# Substitute epsilon into dE/dtau
dE_dtau_with_epsilon = dE_dtau.subs(epsilon, epsilon_expr)

# Simplify the expression after substitution
dE_dtau_with_epsilon = simplify(dE_dtau_with_epsilon)

# Print the expression
print('dE/dtau with epsilon substituted: ')
sympy.pprint(dE_dtau_with_epsilon)

# Set the expression to zero and solve for tau
tau_solutions = sympy.solve(Eq(dE_dtau_with_epsilon, 0), tau)

#Print the solutions for tau
print("Tau solutions:", tau_solutions)
