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

    cache = {}  # start -> futureCost(state),action,newState, cost

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


def predict(N, weights):
    '''
    Input(x) : N ( number of blocks)
    Output(x) : path(sequence of actions)
    '''
    problem = TransportationProblem(N, weights)
    totalCost, history = dynamicProgramming(problem)
    return [action for action, newState, cost in history]


def generateExamples():
    trueWeights = {'walk': 1, 'tram': 4}
    return [(N, predict(N, trueWeights)) for N in range(1, 10)]


def structuredPerceptron(examples):
    weights = {'walk': 0, 'tram': 0}
    for t in range(100):
        numMistakes = 0
        for N, trueActions in examples:
            # Make a prediction
            predActions = predict(N, weights)
            if predActions != trueActions:
                numMistakes += 1
            # Update weights
            for action in trueActions:
                weights[action] -= 1
            for action in predActions:
                weights[action] += 1

        print("Iteration {} , numMistakes = {} , weights = {}".format(
            t, numMistakes, weights))

        if numMistakes == 0:
            break


examples = generateExamples()
print("Training Dataset")
for example in examples:
    print(" ", example)
structuredPerceptron(examples)
"""OUTPUT
Training Dataset
  (1, [])
  (2, ['walk'])
  (3, ['walk', 'walk'])
  (4, ['walk', 'walk', 'walk'])
  (5, ['walk', 'walk', 'walk', 'walk'])
  (6, ['walk', 'walk', 'walk', 'walk', 'walk'])
  (7, ['walk', 'walk', 'walk', 'walk', 'walk', 'walk'])
  (8, ['walk', 'walk', 'walk', 'tram'])
  (9, ['walk', 'walk', 'walk', 'tram', 'walk'])
Iteration 0 , numMistakes = 3 , weights = {'walk': 0, 'tram': 2}
Iteration 1 , numMistakes = 2 , weights = {'walk': 1, 'tram': 3}
Iteration 2 , numMistakes = 3 , weights = {'walk': 0, 'tram': 4}
Iteration 3 , numMistakes = 2 , weights = {'walk': 1, 'tram': 5}
Iteration 4 , numMistakes = 2 , weights = {'walk': 2, 'tram': 6}
Iteration 5 , numMistakes = 3 , weights = {'walk': 1, 'tram': 7}
Iteration 6 , numMistakes = 2 , weights = {'walk': 3, 'tram': 7}
Iteration 7 , numMistakes = 3 , weights = {'walk': 2, 'tram': 8}
Iteration 8 , numMistakes = 0 , weights = {'walk': 2, 'tram': 8}
"""
