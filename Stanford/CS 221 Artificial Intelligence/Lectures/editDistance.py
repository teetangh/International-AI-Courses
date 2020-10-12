# import sys
# sys.stdin = open('xinput.txt', 'r') 
# sys.stdout = open('xoutput.txt', 'w')
#main code

def computeEditDistance(s, t):
    def recurse(m, n):
        """
        Return the minimum edit distance between:
        - first m letters of s
        - first n letters of t
        """

        if m == 0:
            result = n
        elif n == 0:
            result = m

        elif s[m-1] == t[n-1]:  # Last Letter matches
            result = recurse(m-1, n-1)
        else:
            subCost = 1 + recurse(m-1, n-1)
            delCost = 1 + recurse(m-1, n)
            insCost = 1 + recurse(m, n-1)
            result = min(subCost, delCost, insCost)
        return result

    return recurse(len(s), len(t))


print(computeEditDistance("a cat!", "the cats!"))
# 4