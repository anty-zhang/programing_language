# -*- coding: utf-8 -*-
"""
(1+1)-ES with 1/5th success rule with visualization.

Visit my tutorial website for more: https://morvanzhou.github.io/tutorials/
"""
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


DNA_SIZE = 1        # DNA (real number)
DNA_BOUND = [0, 5]  # solution upper and lower bounds
N_GENERATION = 200
MUT_STRENGTH = 5.   # initial step size(dynamic mutation strength)


def F(x):
    return np.sin(10*x)*x + np.cos(2*x)*x     # to find the maximum of this function


# find non-zero fitness for selection
def get_fitness(pred):
    return pred.flatten()


def make_kid(parent):
    # no crossover, only mutation
    kids = parent + MUT_STRENGTH * np.random.randn(DNA_SIZE)
    kids = np.clip(kids, *DNA_BOUND)

    return kids


def kill_bad(parent, kids):
    global MUT_STRENGTH
    fitness_parent = get_fitness(F(parent))[0]
    fitness_kids = get_fitness(F(kids))[0]
    p_target = 1/5

    if fitness_parent < fitness_kids:       # kid better than parent
        parent = kids
        ps = 1.                             # kid win -> ps=1 (successful offspring)
    else:
        ps = 0.

    # adjust global mutation strength

    MUT_STRENGTH *= np.exp(1/np.sqrt(DNA_SIZE+1) * (ps - p_target)/ (1 - p_target))
    return parent


parent = 5 * np.random.rand(DNA_SIZE)   # parent DNA

# something about plotting
plt.ion()
x = np.linspace(*DNA_BOUND, 200)
plt.plot(x, F(x))

for _ in range(N_GENERATION):
    # ES part
    kid = make_kid(parent)
    py, ky = F(parent), F(kid)  # for later plot
    parent = kill_bad(parent, kid)

    # something about plotting
    plt.cla()
    plt.scatter(parent, py, s=200, lw=0, c='red', alpha=0.5, )
    plt.scatter(kid, ky, s=200, lw=0, c='blue', alpha=0.5)
    plt.text(0, -7, 'Mutation strength=%.2f' % MUT_STRENGTH)
    plt.plot(x, F(x))
    plt.pause(0.05)

plt.ioff()
plt.show()
