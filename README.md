# Twister_individual

In this repository:

1. **custom_polygon_for_K.m**
   This MATLAB code provides inputs for the SolveTorsionSimplyConnectedRod.m MATLAB code, which in turn outputs a value for the torsion constant K and its associated error.

2. **secondandFourthPolarMomentsofArea.nb**
   This Mathematica code takes the coordinates of the custom polygon in terms of the heights and widths of the core and wings respectively, and outputs the area of the core, the area of the wings, the Second Polar Moments of Area of the core and wings, and the Fourth Polar Moments of Area of the core and the wings.

3. **substitute_epsilon_solve_tau.py**
   This Python code takes the expression for epsilon derived by minimising the total energy function of the twister structure, substitutes it into the minimised expression with respect to tau, and solves for tau.

4. **numerical_tau_calculation.py**
   This code takes the values obtained and inputs them into the positive solution for tau to yield a numerical value. For the results in this report, epsilon_pre was changed.

5. **cae_jnl_odb_for_pre_03.zip**
   This .zip file contains epre_03.cae, epre_03.jnl, and epre_03.odb, which are the model database, journal, and output database files for epsilon_pre = 0.3 (sigma_33 = 3.75E+05). Changing the sigma_33 value to the corresponding values for epsilon_pre = 0.1 to 0.5 reproduces the results discussed in the report.

6. **tau_calculated_from_simulation.m**
   This is a MATLAB code which takes the deformed x and y coordinates along the z-axis of the nodes at the same (x,y) position, and outputs the twist per unit length (tau), the unwrapped angles in radians (theta_unwrapped), the number of turns, and the total twist. Additionally plots the unwrapped helical shape.

7. **meshconvergence.m**
   This MATLAB code uses the same inputs as for **tau_calculated_from_simulation.m** but was repeated for the same epsilon_pre with changing global seed sizes. 
