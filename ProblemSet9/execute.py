# Tragically, this does not run.
# I think it was very close, but I was unable to resolve the issues I was having.
# Sorry!
# Anyway, thanks for a great class. I've definitely learned a lot.
# Happy holidays!


import SS as ss
import numpy as np
import matplotlib.pyplot as plt


# set parameters
S = 80
beta = 0.8
sigma = 1.5
l_tilde = 1.0
b_param = .501
nu = 1.554
chi = np.ones(S)
A = 1.0
alpha = 0.3
delta = 0.1

params = alpha, delta, A, sigma, beta, S, chi, b_param, l_tilde, nu
# b_s = np.ones(S)
# b_sp1 = np.ones(S-1)
# b_s[0] = 0
# b_sp1[-1] = 0
# n_s = np.ones(S)



# make initial guesses
r_guess = 0.1
bn_guesses = np.ones((2 * S + 1), dtype=int)


r_ss, L_ss, K_ss, success, euler_errors = ss.ss_solver(
    r_guess, bn_guesses, params)

print('The SS interest rate is ', r_ss, 'Did we find the solution?', success)


plt.plot()
plt.title('Savings by Age', y=.92)


plt.plot()
plt.title('Labor Supply by Age', y=.92)

plt.plot()
plt.title('Consumption by Age', y=.92)





