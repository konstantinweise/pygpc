"""
D-optimal sampling
==================

ADD THEORY OF D-GRIDS HERE

Example
-------
In order to create a grid of sampling points, we have to define the random parameters and create a gpc object.
"""

import pygpc
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

# define model
model = pygpc.testfunctions.RosenbrockFunction()

# define random parameters
parameters = OrderedDict()
parameters["x1"] = pygpc.Beta(pdf_shape=[1, 1], pdf_limits=[-np.pi, np.pi])
parameters["x2"] = pygpc.Beta(pdf_shape=[1, 1], pdf_limits=[-np.pi, np.pi])

# define problem
problem = pygpc.Problem(model, parameters)

# create gpc object
gpc = pygpc.Reg(problem=problem,
                order=[5]*problem.dim,
                order_max=5,
                order_max_norm=1,
                interaction_order=2,
                interaction_order_current=2,
                options=None,
                validation=None)

###############################################################################
# A D-optimal grid containing 200 sampling points can be generated by:

grid_d = pygpc.L1(parameters_random=parameters,
                  n_grid=200,
                  gpc=gpc,
                  options={"seed": None,
                           "method": "greedy",
                           "criterion": ["D"],
                           "n_pool": 1000})

###############################################################################
# A hybrid D- and coherence optimal grid containing 200 sampling points can be generated by:

grid_d_coh = pygpc.L1(parameters_random=parameters,
                      n_grid=200,
                      gpc=gpc,
                      options={"seed": None,
                               "method": "greedy",
                               "criterion": ["D-coh"],
                               "n_pool": 1000})

###############################################################################
# The following options are available for D-optimal grids:
#
# - seed: set a seed to reproduce the results (default: None)
# - method:
#    - "greedy": greedy algorithm (default, recommended)
#    - "iter": iterative algorithm (faster but does not perform as good as "greedy")
# - criterion:
#    - "D": D-optimal grid
#    - "D-coh": D- and coherence optimal grid
# - n_pool: number of grid points in overall pool to select optimal points from (default: 10.000)
#
# The grid points are distributed as follows (in the normalized space):

fig, ax = plt.subplots(nrows=1, ncols=2, squeeze=True, figsize=(6.35, 3.2))

ax[0].scatter(grid_d.coords_norm[:, 0], grid_d.coords_norm[:, 1], c="g")
ax[1].scatter(grid_d_coh.coords_norm[:, 0], grid_d_coh.coords_norm[:, 1], c="g")

title = ['D-optimal', 'D-coh optimal']

for i in range(len(ax)):
    ax[i].set_xlabel("$x_1$", fontsize=12)
    ax[i].set_ylabel("$x_2$", fontsize=12)
    ax[i].set_xticks(np.linspace(-1, 1, 5))
    ax[i].set_yticks(np.linspace(-1, 1, 5))
    ax[i].set_xlim([-1, 1])
    ax[i].set_ylim([-1, 1])
    ax[i].set_title(title[i])
    ax[i].grid()

plt.tight_layout()

###############################################################################
# The sampling method can be selected accordingly for each gPC algorithm by setting the following options
# when setting up the algorithm:
options = dict()
...
options["grid"] = pygpc.CO
options["grid_options"] = {"seed": None,
                           "method": "greedy",
                           "criterion": ["D-coh"],
                           "n_pool": 1000}
...

# When using Windows you need to encapsulate the code in a main function and insert an
# if __name__ == '__main__': guard in the main module to avoid creating subprocesses recursively:
#
# if __name__ == '__main__':
#     main()
