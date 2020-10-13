import numpy as np


###########################################################################
# Modelling what we want to compute

# Hand coded data
# points = [(np.array([2]), 4), (np.array([4]), 2)]
# d = 1

# Generating Artificial Data
true_w = np.array([1, 2, 3, 4, 5])
d = len(true_w)
points = []
for t in range(50000):
    x = np.random.rand(d)
    y = true_w.dot(x) + np.random.randn()

    print(x, y)
    points.append((x, y))

# Regular Gradient Descent


def F(w):
    return sum([(w.dot(x) - y)**2 for x, y in points])/len(points)


def dF(w):
    return sum(2 * (w.dot(x) - y)*x for x, y in points)/len(points)


# Stochastic Gradient Descent
def sF(w, i):
    x, y = points[i]
    return (w.dot(x) - y)**2


def sdF(w, i):
    x, y = points[i]
    return 2*(w.dot(x) - y) * x


###########################################################################
# Algorithms: how we compute it

# Gradient Descent


def gradientDescent(F, dF, d):

    w = np.zeros(d)
    eta = 0.01
    for t in range(1000):

        value = F(w)
        gradient = dF(w)

        w = w - eta * gradient
        print('iteration {}: w = {} , F(w) = {}'.format(t, w, value))


def stochasticGradientDescent(sF, sdF, d, n):

    w = np.zeros(d)
    # eta = 0.1
    numUpdates = 1

    for t in range(1000):
        for i in range(n):
            value = sF(w, i)
            gradient = sdF(w, i)
            numUpdates += 1
            eta = 1.0 / numUpdates
            w = w - eta * gradient
        print('iteration {}: w = {} , F(w) = {}'.format(t, w, value))


# gradientDescent(F, dF, d)
stochasticGradientDescent(sF, sdF, d, len(points))
