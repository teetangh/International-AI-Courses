"""
Model (search Problem)
"""


class TransportationProblem(object):

    def __init__(self, N):
        # N = number of blocks
        self.N = N

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def succAndCost(self, state):
        # Return list of (action , newState, cost) triples
        result = []

        if state+1 <= self.N:
            result.append(('walk', state + 1,  1))

        if state * 2 <= self.N:
            result.append(('tram', state * 2, 2))

        return result


"""
Algorithms
"""


def printSolution(solution):
    totalCost, history = solution
    print('totalCost: {}'.format(totalCost))

    for item in history:
        print(item)


def backtrackingSearch(problem):
    # Dictionary of the best solution so far(dictionary because of python scoping technicality)
    best = {
        'cost': float('+inf'),
        'history': None
    }

    def recurse(state, history, totalCost):
        # At State , having undergone history,accumulate
        # Total Cost
        # Explore the rest of the subtree under state
        if problem.isEnd(state):
            # Update the best solution so far
            # TODO
            if totalCost < best['cost']:
                best['history'] = history
                best['cost'] = totalCost
            return

        # Recurse on children
        for action, newState, cost in problem.succAndCost(state):
            recurse(newState, history +
                    [(action, newState, cost)], totalCost + cost)
    recurse(problem.startState(), history=[], totalCost=0)
    return (best['cost'], best['history'])


def dynamicProgramming(problem):

    cache = {}  # start -> futureCost(state)

    def futureCost(state):
        if problem.isEnd(state):
            return 0

        if state in cache:
            return cache[state]

        result = min(cost + futureCost(newState)
                     for action, newState, cost in problem.succAndCost(state))

        return result

    return (futureCost(problem.startState()), [])


"""
Main
"""
# print(problem.succAndCost(3))
# print(problem.succAndCost(9))

print("Backtracking")
problem = TransportationProblem(N=100)
printSolution(backtrackingSearch(problem))

''' OUTPUT
 totalCost: 13
 ('walk', 2, 1)
 ('walk', 3, 1)
 ('tram', 6, 2)
 ('tram', 12, 2)
 ('tram', 24, 2)
 ('walk', 25, 1)
 ('tram', 50, 2)
 ('tram', 100, 2)
'''

# import sys
# sys.setrecursionlimit(100000)
# problem = TransportationProblem(N=1000)
# printSolution(backtrackingSearch(problem))

print("Dyanmmic Programming")
printSolution(dynamicProgramming(problem))
