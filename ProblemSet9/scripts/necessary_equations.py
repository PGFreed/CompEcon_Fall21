import numpy as np


# eqn 5
def get_L(n_s):
    '''
    Function to compute agg labor supply
    '''
    L = n_s.sum()
    return L


# eqn 6
def get_K(b):
    '''
    Function to compute agg capital supply
    '''
    K = b.sum()
    return K


# eqn 3
def get_r(K, L, params):
    '''
    Compute the interest rate from the firm's FOC
    '''
    alpha, delta, A = params
    r = alpha * A * (L/K) ** (1 - alpha) - delta
    return r


# find r as a fn of K/L to plug into eqn 4 to imply w
def get_w(r, params):
    '''
    Solve for the w that is consistant with r from the
    firm's FOC
    '''
    alpha, delta, A = params
    w = (1 - alpha) * A * ((alpha * A) / (r + delta)) ** (alpha / (1 - alpha))
    return w


# u(c) is equation 4.8
def mu_c_func(c, sigma):
    '''
    Marginal utility of consumption
    '''
    mu_c = c ** -sigma
    return mu_c


def get_c(r, w, b_s, b_sp1, n_s):
    '''
    Find consumption using the budget constraint
    and the choice of savings (b_sp1)
    '''
    c= np.dot(r+1,b_s) + np.dot(w, n_s) - b_sp1
    # c = ((1 + r) * b_s) + (w * n_s) - b_sp1
    return c


def mu_n_func(chi, b_param, l_tilde, n_s, nu):
    '''
    Marginal utility of n
    '''
    # a_ = chi * (b_param/l_tilde)
    # b_ = (n_s/l_tilde)**(nu - 1)
    # c_ = (1 - ((n_s/l_tilde)**nu)) ** ((1-nu)/nu)
    # mu_n = np.dot(a_,b_,c_)
    mu_n = chi * (b_param/l_tilde) * ((n_s/l_tilde) ** (nu-1)) * (1 - ((n_s/l_tilde) ** nu)) ** ((1-nu)/nu)
    return mu_n

# original eqn 1
# want to ensure they hold.  Make equation = euler_error
# in eqm the euler_error = 0 and need to find b's to make it 0
# solve for b2 and b3, given r and w, from hh_foc
def hh_foc(bn_list, r, w, params):
    '''
    Define the household first order conditions
    '''
    sigma, beta, S, chi, b_param, l_tilde, nu = params
    # bn_list = np.zeros((2 * S -1), dtype=int)
    b_s = bn_list[0:S] # from period 0 to 80
    b_s[0] = 0
    b_sp1 = bn_list[1:S+1] # from period 1 to 80
    b_sp1[-1] = 0
    n_s = bn_list[S+1:2*S+1]
    c = get_c(r, w, b_s, b_sp1, n_s)
    mu_c = mu_c_func(c, sigma)
    mu_n = mu_n_func(chi, b_param, l_tilde, n_s, nu)
    euler_error = mu_c[:-1] - beta * (1+r) * mu_c[1:]
    euler_error_2 = w * mu_c - mu_n
    return euler_error, euler_error_2

