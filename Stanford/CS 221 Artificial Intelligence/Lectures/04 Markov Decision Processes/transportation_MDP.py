# import util
import sys
sys.setrecursionlimit(10000)

# Model (search problem)


class TransportationMDP(object):

    def __init__(self, N):
        '''
         N = Number of blocks
        '''
        self.N = N

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def actions(self, state):
        '''
         Returns list of valid actions
        '''
        result = []
        if state + 1 <= self.N:
            result.append('walk')
        if state * 2 <= self.N:
            result.append('tram')

        # for item in result:
        #     print(result)

        return result

    def succAndCost(self, state, action):
        """
         Returns list of (newState, prob , reward ) triples
         state  = s , action = a , newState = s'
         prob = T(s,a,s') , reward = Reward(s,a,s')
        """
        result = []
        if action == 'walk':
            result.append((state+1, 1., -1.))
        elif action == 'tram':
            result.append((state * 2, 0.5, -2.))
            result.append((state, 0.5, -2.))

        # for item in result:
        #     print(result)

        return result

    def discount(self):
        return 1.

    def state(self):
        return range(1, self.N+1)

# Inference Algorithms


mdp = TransportationMDP(N=10)
print(mdp.actions(3))
print(mdp.succAndCost(3, 'walk'))
print(mdp.succAndCost(3, 'tram'))
