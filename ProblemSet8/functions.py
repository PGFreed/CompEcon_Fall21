
# %%

def utility(f, fprime):

    W = ((f - (1 + (delta)) * fprime) + (phi) * (f)) ** (1/time) #Equation 1 
    
    U = np.log(W) #log utility

    return U

#%%

def bellmanoperator(V, f_grid, beta):
    #I also found success using quadratic instead of cubic
    V_func = interpolate.interp1d(f_grid, V, kind='cubic', fill_value='extrapolate')

    #Apply the nessecary empty arrays
    TV = np.empty_like(V)
    optf = np.empty_like(TV)

    # Here I apply: max_f' { u(f,f') + beta V(f')}
    #This is Equation 2 
    for i, f in enumerate(f_grid):
        def objective(fprime):
            return - utility(f, fprime) - (beta * V_func(fprime))  
        fprime_star = fminbound(objective, 1e-6, f - 1e-6)
        optf[i] = fprime_star
        TV[i] = - objective(fprime_star)
    return TV, optf


# %% 
