# -*- coding: utf-8 -*-
"""module1-scratchpad.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AHl2wDKsml7lsJsj03GuMxYlgpd3zB7D

The Z-test based on CLT
"""

from scipy.stats import norm
import math

x_bar = 39/31000
mu = 63/31000

sigma = math.sqrt(mu * (1-mu))
se = sigma/math.sqrt(31000)

test_stats = (x_bar-mu)/se
norm.cdf(-3.0268)

"""T-test for small samples"""

import numpy as np
X = np.array([0.9, -0.9, 4.3, 2.9, 1.2, 3, 2.7, 0.6, 3.6, -0.5])
X_bar = np.mean(X)

N = len(X)
print(N)

sigma_hat = math.sqrt(np.var(X, ddof=1))
se = sigma_hat/math.sqrt(N)

T = X_bar/se

print(T)

from scipy.stats import t
1-t.cdf(T, df=N-1)

"""The following are for LRT: Likelihood Ratio Test"""

N_t = 31000
X_t = 39
N_c = 31000
X_c = 63
X = X_t + X_c
N = N_t + N_c
pi_MLE_null = X/N
pi_MLE_t = X_t/N_t
pi_MLE_c = X_c/N_c

from scipy.stats import binom, chi2
L_null = binom.pmf(X_t, N_t, pi_MLE_null) * binom.pmf(X_c, N_c, pi_MLE_null) 
L_all = binom.pmf(X_t, N_t, pi_MLE_t) * binom.pmf(X_c, N_c, pi_MLE_c)

import numpy as np
LRTs = -2 * np.log(L_null/L_all)

print(LRTs)

#p-value > LRTs in Chi square 1
p_val = 1-chi2.cdf(LRTs, 1)

print(p_val)

"""Multiple testing discussions"""

#Benjamini-Hochberg correction

import numpy as np
N = 5 
p_val = np.array([0.007, 0.016, 0.09, 0.17, 0.265])
rank = np.arange(1, 6)
alpha = 0.05
sig_adjusted = (rank/N)*alpha
print(sig_adjusted)

p_val < sig_adjusted

"""Linear regression, and correlation etc"""

import numpy as np
import matplotlib.pyplot as plt # import the library
Xs = np.random.normal(0, 2, 100)
Ys = 2*Xs + np.random.normal(0, 0.5, 100)
#scatter plot
plt.scatter(Xs, Ys) # Create the scatter plot, Xs and Ys are two numpy arrays of the same length
plt.show()

#line plot
plt.plot(Xs, Ys)


#matrix inversion
Zs = np.random.normal(2, 5, size=(4,4))
print(Zs)
Z_inv = np.linalg.inv(Zs)
print(Z_inv)

#Distribution utils
import scipy.stats
T = 2.7
num_degrees_of_freedom = 90
scipy.stats.t.sf(T, num_degrees_of_freedom)

Y2s = Xs**2
from scipy.stats import pearsonr
print("Correlation coefficient is: ", pearsonr(Xs, Y2s))

"""Astronomy exercise on correlation"""

Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503, 0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41, 
1.72, 2.03, 2.02, 2.02, 2.02])

Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 320.0, 373.0, 93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 608.0, 1.04E3, 1.10E3, 840.0, 801.0, 519.0])

N = 24

import numpy as np

mean_X = np.mean(Xs)
print("Mean of Xs is", mean_X)
mean_Y = np.mean(Ys)
print("Mean of Y is", mean_Y) 

#Standard dev
sd_X = np.std(Xs, ddof=1)
sd_Y = np.std(Ys, ddof=1)
print("Std for Xs: ", sd_X)
print("Std for Ys: ", sd_Y) 

cov_XY = np.std(Ys, ddof=1)
print("Covariance of Xs and Ys are: ", cov_XY) 

from scipy.stats import pearsonr
cor_XY = pearsonr(Xs, Ys)[0]
print("Correlation coefficient is: ", cor_XY)

beta1 = cor_XY * sd_Y / sd_X
beta0 = mean_Y - beta1 * mean_X

print("beta0 is", beta0, "beta1 is: ", beta1)

#Calculate R2 

Y_hat = beta0 + beta1*Xs

SumResidual = np.sum((Ys-Y_hat)**2)
SumTotal = np.sum((Ys-mean_Y)**2)

R2 = 1-SumResidual/SumTotal

print("R2 is: ", R2)

"""Non-linear transformation for regression:

Each data point is one planet in our solar system (with the addition of the planetoid Pluto, which will be henceforth referred to as a planet for simplicity).

The  values are the semi-major axis of each planet's orbit around the Sun. A planetary orbit is elliptical in shape, and the semi-major axis is the longer of the two axes that define the ellipse. When the ellipse is nearly circular (which is true for most planets), the semi-major axis is approximately the radius of said circle. The  values are measured in units of Astronomical Units (AU). One AU is very close to the average distance between the Sun and Earth (defined as 149597870700 meters), hence, the Earth's semi-major axis is essentially 1 AU due to its very circular orbit.

The  values are the orbital period of the planet, measured in Earth years (365.25 days), so Earth also has a  year.
"""

import numpy as np

    
Xs = np.array([ 0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5 ])

Ys = np.array([ 0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248 ])

N = 9

#plot first for visual inspection
import matplotlib.pyplot as plt # import the library
#scatter plot
plt.scatter(Xs, Ys) # Create the scatter plot, Xs and Ys are two numpy arrays of the same length
#line plot
plt.plot(Xs, Ys)
plt.show()
#does not look very linear to me

#correlation
from scipy.stats import pearsonr
cor_XY = pearsonr(Xs, Ys)[0]
print("Correlation coefficient is: ", cor_XY)

#linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()

X_prime = Xs.reshape(-1, 1)
model.fit(X_prime, Ys)
Y_hat = model.predict(X_prime)
residuals = Ys - Y_hat

#plot residuals
plt.scatter(Xs, residuals)
plt.show()

plt.scatter(Y_hat, residuals)
plt.show()

#QQ plot to test normality
import statsmodels.api as sm
sm.qqplot(Xs, line='s')
plt.title("X distribution")
plt.show()

sm.qqplot(Ys, line='s')
plt.title("Y distribution")
plt.show()

sm.qqplot(residuals, line='s')
plt.title("Residuals distribution")
plt.show()



#Explore some transformation
LogY = np.log(Ys)
plt.plot(Xs, LogY)
plt.title("Log Y vs X")
plt.show()

LogX = np.log(X_prime)
plt.plot(LogX, Ys)
plt.title("Y vs Log X")
plt.show()

plt.plot(LogX, LogY)
plt.title("LogY vs Log X")
plt.show()


#Linear regression with transformed variables

model2 = LinearRegression()
model2.fit(LogX, LogY)

print("Transformed linear model params: intercept", model2.intercept_, "slope: ", model2.coef_)

"""Exoplanet mass data.

For this exercise, we will perform multiple linear regression on some exoplanetary data to see if we can find a relationship that can predict the mass of an exoplanet.
"""

import numpy as np

LogPlanetMass = np.array([-0.31471074,  1.01160091,  0.58778666,  0.46373402, -0.01005034,
         0.66577598, -1.30933332, -0.37106368, -0.40047757, -0.27443685,
         1.30833282, -0.46840491, -1.91054301,  0.16551444,  0.78845736,
        -2.43041846,  0.21511138,  2.29253476, -2.05330607, -0.43078292,
        -4.98204784, -0.48776035, -1.69298258, -0.08664781, -2.28278247,
         3.30431931, -3.27016912,  1.14644962, -3.10109279, -0.61248928])

LogPlanetRadius = np.array([ 0.32497786,  0.34712953,  0.14842001,  0.45742485,  0.1889661 ,
         0.06952606,  0.07696104,  0.3220835 ,  0.42918163, -0.05762911,
         0.40546511,  0.19227189, -0.16251893,  0.45107562,  0.3825376 ,
        -0.82098055,  0.10436002,  0.0295588 , -1.17921515,  0.55961579,
        -2.49253568,  0.11243543, -0.72037861,  0.36464311, -0.46203546,
         0.13976194, -2.70306266,  0.12221763, -2.41374014,  0.35627486])

LogPlanetOrbit = np.array([-2.63108916, -3.89026151, -3.13752628, -2.99633245, -3.12356565,
        -2.33924908, -2.8507665 , -3.04765735, -2.84043939, -3.19004544,
        -3.14655516, -3.13729584, -3.09887303, -3.09004295, -3.16296819,
        -2.3227878 , -3.77661837, -2.52572864, -4.13641734, -3.05018846,
        -2.40141145, -3.14795149, -0.40361682, -3.2148838 , -2.74575207,
        -3.70014265, -1.98923527, -3.35440922, -1.96897409, -2.99773428])

StarMetallicity = np.array([ 0.11 , -0.002, -0.4  ,  0.01 ,  0.15 ,  0.22 , -0.01 ,  0.02 ,
        -0.06 , -0.127,  0.   ,  0.12 ,  0.27 ,  0.09 , -0.077,  0.3  ,
         0.14 , -0.07 ,  0.19 , -0.02 ,  0.12 ,  0.251,  0.07 ,  0.16 ,
         0.19 ,  0.052, -0.32 ,  0.258,  0.02 , -0.17 ])

LogStarMass = np.array([ 0.27002714,  0.19144646, -0.16369609,  0.44468582,  0.19227189,
         0.01291623,  0.0861777 ,  0.1380213 ,  0.49469624, -0.43850496,
         0.54232429,  0.02469261,  0.07325046,  0.42133846,  0.2592826 ,
        -0.09431068, -0.24846136, -0.12783337, -0.07364654,  0.26159474,
         0.07603469, -0.07796154,  0.09440068,  0.07510747,  0.17395331,
         0.28893129, -0.21940057,  0.02566775, -0.09211529,  0.16551444])

LogStarAge = np.array([ 1.58103844,  1.06471074,  2.39789527,  0.72754861,  0.55675456,
         1.91692261,  1.64865863,  1.38629436,  0.77472717,  1.36097655,
         0.        ,  1.80828877,  1.7837273 ,  0.64185389,  0.69813472,
         2.39789527, -0.35667494,  1.79175947,  1.90210753,  1.39624469,
         1.84054963,  2.19722458,  1.89761986,  1.84054963,  0.74193734,
         0.55961579,  1.79175947,  0.91629073,  2.17475172,  1.36097655])

N = 30

"""Choice of variable transformation.

All of these observed quantities have been transformed by taking the natural logarithm. When performing linear regression, it can help to have a general idea on how the predictors contribute to the predicted quantity.

For example, if one were attempting to predict the sales of a store based on the population of surrounding region, then we might expect that the sales will be cumulative in the population variables. In this case, it would be best to leave these variables as they are, performing the linear regression directly on them.

However, in astronomy and physics, it is very common for the predicted variable to be multiplicative in the predictors. For example, the power that a solar cell produces is the product of the amount of solar radiation and the efficiency of the cell. In that case, it is better to transform the variables by taking the logarithm as discussed previously.

LogPlanetMass is the logarithm of the observed exoplanet's mass in units of Jupiter's mass. A LogPlanetMass of zero is an exoplanet with the same mass as Jupiter. Jupiter is used as a convenient comparison, as large gas giants are the most easily detected, and thus most commonly observed, kind of exoplanet. LogPlanetRadius is the logarithm of the observed exoplanet's radius in units of Jupiter's radius, for much the same reason. LogPlanetOrbit is the logarithm of the observed planet's semi-major axis of orbit, in units of AU. StarMetallicity is the relative amount of metals observed in the parent star. It is equal to the logarithm of the ratio of the observed abundance of metal to the observed abundance of metal in the Sun. The Sun is a quite average star, so it serves as a good reference point. The most common metal to measure is Iron, but astronomers define any element that isn't Hydrogen or Helium as a metal. LogStarMass is the logarithm of the parent star's mass in units of the Sun's mass. LogStarAge is the logarithm of the parent star's age in giga-years.
"""

import numpy as np
Xs = np.concatenate((np.ones(N), LogPlanetRadius, LogPlanetOrbit, StarMetallicity, LogStarMass, LogStarAge)).reshape(6, N).transpose()
Ys = LogPlanetMass

model = LinearRegression()
model.fit(Xs, Ys)

print(model.coef_)

"""T-test for the Exoplanet datasets"""

import numpy as np

#Test stats calculation

#Answers from course
Ys = LogPlanetMass
# Concatenate the variables into a matrix, np.ones_like inserts a row of ones into the start of the matrix for the intercept term.
# Taking the transpose places each variable as columns.
Xmat = np.array((np.ones_like(LogPlanetRadius), LogPlanetRadius, LogPlanetOrbit, StarMetallicity, LogStarMass, LogStarAge)).T
from numpy.linalg import inv
# The beta estimator using the matrix inversion formula
betaVec = inv(Xmat.T.dot(Xmat)).dot(Xmat.T).dot(Ys)

print("beta estimated: ", betaVec)
residuals = Ys - Xmat.dot(betaVec)
print("residuals: ", residuals.shape)

P = betaVec.shape[0]
print("number of features: ", P)
sigma_cov = inv(Xmat.T.dot(Xmat))
var_hat = np.sum(residuals**2)/(N-P)

print("signma hat2", var_hat)

Ts = betaVec/(var_hat*sigma_cov)

print("Test stats: ", Ts)