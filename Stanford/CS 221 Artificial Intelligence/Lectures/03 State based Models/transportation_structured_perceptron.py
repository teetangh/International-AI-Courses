import util

"""
Model (search Problem)
"""


class TransportationProblem(object):

    def __init__(self, N, weights):
        # N = number of blocks
        # weights = weights of different actions
        self.N = N
        self.weights = weights

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def succAndCost(self, state):
        # Return list of (action , newState, cost) triples
        result = []

        if state+1 <= self.N:
            result.append(('walk', state + 1,  self.weights['walk']))

        if state * 2 <= self.N:
            result.append(('tram', state * 2, self.weights['tram']))

        return result


"""
Algorithms
"""


def printSolution(solution):
    totalCost, history = solution
    print('totalCost: {}'.format(totalCost))

    for item in history:
        print(item)


def dynamicProgramming(problem):

    cache = {}  # start -> futureCost(state)

    def futureCost(state):
        if problem.isEnd(state):
            return 0

        if state in cache:
            return cache[state][0]

        result = min((cost + futureCost(newState), action, newState, cost)
                     for action, newState, cost in problem.succAndCost(state))
        cache[state] = result
        return result[0]

    state = problem.startState()
    totalCost = futureCost(state)

    # Recover history
    history = []
    while not problem.isEnd(state):
        _, action, newState, cost = cache[state]
        history.append((action, newState, cost))
        state = newState

    return (futureCost(problem.startState()), history)


"""
Main
"""
