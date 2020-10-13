import heapq

# Data structure for supporting uniform cost search


class PriorityQueue:

    def __init__(self):
        """
        Insert | state | into the heap with priority |newPriority| if
        | state | isn't in the heap or |newPriority| is smaller than the existing
        priority
        """
        self.DONE = -100000
        self.heap = []
        self.priorites = {}  # Map from state to priority

    def update(self, state, newPriority):
        """
        Returns whether the priority queue was updated
        """
        oldPriority = self.priorites.get(state)
        if oldPriority == None or newPriority < oldPriority:
            self.priorites[state] = newPriority
            heapq.heappush(self.heap, (newPriority, state))
            return True
        return False

    def removeMin(self):
        """
        Returns (state with minimum priority , priority)
        or (None , None ) if the priority queue is empty
        """
        while len(self.heap) > 0:
            priority, state = heapq.heappop(self.heap)
            if self.priorites[state] == self.DONE:
                continue    # Outdated priority can skip
            self.priorites[state] = self.DONE
            return (state, priority)
        return (None, None)
