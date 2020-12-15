"""
Standard Random sampling
========================

Choosing a sampling scheme
--------------------------

To calculate the coefficients of the gPC matrix, a number of random samples needs to be
picked to represent the propability space :math:`\\Theta` and enable descrete evaluations of the
polynomials. As for the computation of the coefficients, the input parameters :math:`\\mathbf{\\xi}`
can be sampled in a number of different ways. In **pygpc** the grid :math:`\\mathcal{G}` for this
application is constructed in `pygpc/Grid.py <../../../../pygpc/Grid.py>`_.

Before we are going to go through the different grid types, we are going to define a test problem.
"""

import pygpc
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import OrderedDict

# define model
model = pygpc.testfunctions.RosenbrockFunction()

# define parameters
parameters = OrderedDict()
parameters["x1"] = pygpc.Beta(pdf_shape=[1, 1], pdf_limits=[-np.pi, np.pi])
parameters["x2"] = pygpc.Beta(pdf_shape=[1, 1], pdf_limits=[-np.pi, np.pi])

# define problem
problem = pygpc.Problem(model, parameters)

###############################################################################
# In the case of random sampling the samples will be randomly from their Probability Density Function (PDF)
# :math:`f(\xi)`.
#
# A simple random grid containing 100 sampling points can be generated by:
# sphinx_gallery_thumbnail_number = 1:

grid_random = pygpc.Random(parameters_random=parameters, n_grid=100)

fig = plt.figure(figsize=(4, 3.5))
plt.scatter(grid_random.coords_norm[:, 0], grid_random.coords_norm[:, 1])
plt.xlabel("$x_1$", fontsize=12)
plt.ylabel("$x_2$", fontsize=12)
plt.xlim([-1, 1])
plt.ylim([-1, 1])
plt.xticks(np.linspace(-1, 1, 5))
plt.yticks(np.linspace(-1, 1, 5))
plt.grid()
plt.tight_layout()

# On Windows subprocesses will import (i.e. execute) the main module at start.
# You need to insert an if __name__ == '__main__': guard in the main module to avoid
# creating subprocesses recursively.
#
# if __name__ == '__main__':
#     main()
