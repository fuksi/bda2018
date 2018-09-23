from scipy.stats import beta
from scipy import special
from matplotlib import pyplot
import numpy as np
import math

a_prior = 2
b_prior = 10
a = 46
b = 240

print('Prior mean: ', beta.mean(a_prior, b_prior))
print('Posterior mean : ', beta.mean(a, b))

x = np.arange(0.0, 1.01, 0.01)
y_prior = beta.pdf(x, a_prior, b_prior)
y = beta.pdf(x, a, b)

ax = pyplot.subplot(111)
ax.plot(x, y_prior)
ax.plot(x, y)
# plot.show()

sample_size = 1000
r = beta.rvs(a, b, size=sample_size)
new_mean = np.mean(r)
new_std = np.std(r)

"""
z_critical is the number of std you'd have to go from the mean 
to capture the proportion of data association with the confidence level 
"""
confidence_level = 0.95
z_critical = beta.ppf(q=confidence_level, a=a, b=b)
margin_of_error = z_critical * new_std / math.sqrt(sample_size)
confidence_interval = (new_mean - margin_of_error, new_mean + margin_of_error)

### Answer for question a
print('Point estimate is: ', new_mean)
print('Interval estimate is: ', confidence_interval, ' with confidence level 95%')

### Answer for question b
print('Probability of π < 0.2 is: ', special.btdtr(a, b, 0.2))

### Estimands for question d

# priors
a_1, b_1 = 40, 240
a_2, b_2 = 400, 2400
print('Prior params 1: ', a_1, b_1)
print('Prior params 2: ', a_2, b_2)

#sample
N = 274
z = 44

#posteriors
a_1_p, b_1_p = a_1 + z, N + b_1 - z
a_2_p, b_2_p = a_2 + z, N + b_2 - z

# means:
mean_1 = beta.mean(a_1_p, b_1_p)
mean_2 = beta.mean(a_2_p, b_2_p)
print('Posterior mean 1: ', mean_1)
print('Posterior mean 2: ', mean_2)