from scipy.special import comb

#compute binomial exact prob, sample size: 31000, prob of Bernoulli: 0.00203, num of death: 63
p = 0.00203
N = 31000
K = 63

prob = comb(N, K) * p**K * (1-p)**(N-K)

#prob = 0.05024468664277072

#Fisher exact test computation with SciPy.fisher_exact

#contingency table: horizontal: treatment/control, vertical: death/survival

import numpy as np
from scipy.stats import fisher_exact
table = np.array([[39, 63], [30961, 30937]])
fisher_test = fisher_exact(table, alternative="less")

print(fisher_test)

# -*- coding: utf-8 -*-
"""module1-scratchpad.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AHl2wDKsml7lsJsj03GuMxYlgpd3zB7D

The Z-test based on CLT
"""

from scipy.stats import norm
import math

x_bar = 39 / 31000
mu = 63 / 31000

sigma = math.sqrt(mu * (1 - mu))
se = sigma / math.sqrt(31000)

test_stats = (x_bar - mu) / se
norm.cdf(-3.0268)

"""T-test for small samples"""

import numpy as np

X = np.array([0.9, -0.9, 4.3, 2.9, 1.2, 3, 2.7, 0.6, 3.6, -0.5])
X_bar = np.mean(X)

N = len(X)
print(N)

sigma_hat = math.sqrt(np.var(X, ddof=1))
se = sigma_hat / math.sqrt(N)

T = X_bar / se

print(T)

from scipy.stats import t

1 - t.cdf(T, df=N - 1)

"""The following are for LRT: Likelihood Ratio Test"""

N_t = 31000
X_t = 39
N_c = 31000
X_c = 63
X = X_t + X_c
N = N_t + N_c
pi_MLE_null = X / N
pi_MLE_t = X_t / N_t
pi_MLE_c = X_c / N_c

from scipy.stats import binom, chi2

L_null = binom.pmf(X_t, N_t, pi_MLE_null) * binom.pmf(X_c, N_c, pi_MLE_null)
L_all = binom.pmf(X_t, N_t, pi_MLE_t) * binom.pmf(X_c, N_c, pi_MLE_c)

import numpy as np

LRTs = -2 * np.log(L_null / L_all)

print(LRTs)

# p-value > LRTs in Chi square 1
p_val = 1 - chi2.cdf(LRTs, 1)

print(p_val)

"""Multiple testing discussions"""

# Benjamini-Hochberg correction

import numpy as np

N = 5
p_val = np.array([0.007, 0.016, 0.09, 0.17, 0.265])
rank = np.arange(1, 6)
alpha = 0.05
sig_adjusted = (rank / N) * alpha
print(sig_adjusted)

p_val < sig_adjusted


