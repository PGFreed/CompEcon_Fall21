# builds off of inclass_nov30.py


import necessary_equations as ne
import scipy.optimize as opt


# then, let's write a function for the ss algorithm
    # guess r (-> w)
    # solve for b2 and b3 from hh_foc
    # use market clearing with b2, b3, n -> K, L
    # use K, L in get_r -> r'
    # check if r' = guess of r
    # loop again if not


def ss_solver(r_guess, bn_guesses, params):
    '''
    Solves for the SS of the economy
    '''
    alpha, delta, A, sigma, beta, S, chi, b_param, l_tilde, nu = params
    xi = 0.8
    tol = 1e-8
    max_iter = 500
    dist = 7
    iter = 0
    r = r_guess
    bn_list = bn_guesses
    while (dist > tol) & (iter < max_iter):
        w = ne.get_w(r, (alpha, delta, A))
        sol = opt.root(
            ne.hh_foc, bn_list,
            args=(r, w, (sigma, beta, S, chi, b_param, l_tilde, nu)))
        b_sp1 = sol.x[0:S-1]
        n_s = sol.x[S:2*S-1]
        euler_errors = sol.fun
        K = ne.get_K(b_sp1)
        L = ne.get_L(n_s)
        r_prime = ne.get_r(K, L, (alpha, delta, A))
        dist = (r - r_prime) ** 2
        iter += 1
        r = xi * r + (1 - xi) * r_prime
    success = iter < max_iter

    return r, L, K, success, euler_errors
