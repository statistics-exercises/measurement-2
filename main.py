import numpy as np

radii = np.loadtxt("bubbles.dat")

print("The smallest bubble has a radius of", dmin)
print("25% of the bubbles have a radius that is less than or equal to", lowq)
print("The median radius of the bubbles is", median)
print("75% of the bubbles have a radius that is less than or equal to", highq)
print("The largest bubble has a radius of", dmax)
