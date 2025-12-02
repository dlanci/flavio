"""Special mathematical functions"""


import scipy
import math
import numpy as np
import random

def zeta(x):
    """Riemann Zeta function"""
    return scipy.special.zeta(x, 1)

def li2(x):
    r"""Complex Dilogarithm"""
    return scipy.special.spence(1-x)

def ei(x):
    """Exponential integral function"""
    return scipy.special.expi(x)

def normal_logpdf(x, mu, sigma):
    """Logarithm of the PDF of the normal distribution"""
    # this turns out to be 2 orders of magnitude faster than scipy.stats.norm.logpdf
    if isinstance(x, float):
        _x = x
    else:
        _x = np.asarray(x)
    if not isinstance(mu, float) and not isinstance(sigma, float):
        
        mu=mu.reshape(_x.shape[0],1)
        sigma=sigma.reshape(_x.shape[0],1)

    ret = -(_x-mu)**2/sigma**2/2 - np.log(np.sqrt(2*math.pi)*sigma)
    
    return ret

def normal_pdf(x, mu, sigma):
    """PDF of the normal distribution"""
    # this turns out to be 2 orders of magnitude faster than scipy.stats.norm.logpdf
    if isinstance(x, float):
        _x = x
    else:
        _x = np.asarray(x)
    # return np.exp(-(_x-mu)**2/sigma**2/2)/(np.sqrt(2*math.pi)*sigma)

    if not isinstance(mu, float) and not isinstance(sigma, float):

            mu=mu.reshape(_x.shape[0],1)
            sigma=sigma.reshape(_x.shape[0],1)
    ret = np.exp(-(_x-mu)**2/sigma**2/2)/(np.sqrt(2*math.pi)*sigma)


    return ret


def round_to_sig_dig(num, sig_dig=3):

    rounded_number =  np.around(num, sig_dig - int(np.floor(np.log10(np.abs(num)))) - 1)

    return rounded_number

def k_permutation_of_n(k,N):

    n=len(N)
    m = np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k))

    samples = list()

    while len(samples)<m:
        toadd = tuple(sorted(random.sample(N,k)))
        if toadd not in samples:
            samples.append(toadd)

    return np.array(samples)