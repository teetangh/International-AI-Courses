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
for t in range(10000):
    x = np.random.rand(d)
    y = true_w.dot(x) + np.random.randn()

    print(x, y)
    points.append((x, y))

def F(w):
    return sum([(w.dot(x) - y)**2 for x, y in points])/len(points)


def dF(w):
    return sum(2 * (w.dot(x) - y)*x for x, y in points)/len(points)
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


gradientDescent(F, dF, d)
