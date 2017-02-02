import sys
import os

##Do you guys think keeping these as global vars is okay?
denoms = []
amounts = []

'''
fills 2 global arrays: amounts (a list of amounts from the file) and
denoms (a list of lists of denominations)
Note that indices of arrays correspond.
e.g. amounts[0] corresponds with denoms[0]
'''
def getInputData(filename):
    lineNum = 0
    with open(filename) as inFile:
        for line in inFile:
            lineNum += 1
            if lineNum %2 == 1:
                line = line.split()
                line = [int(i) for i in line]
                denoms.append(line)
            else:
                amounts.append(int(line))
 
'''
Used "Coin Changing Minimum Coins Dynamic Programming"
at https://www.youtube.com/watch?v=NJuKJ8sasGk&t=953s
to learn how to solve this last week. Used again to see
how to determine which coins were used. No code was copied.
'''

def changedp(A, V):
    T = []
    C = []
    coinUsed = []

    #initialize arrays
    for i in range(len(V)):
        C.append(0)
    for i in range(A+1):
        coinUsed.append(-1)
    T.append(-1)
    for i in range(A+1):
        T.append(A+1)
    for i in range(len(V)):
        for j in range(V[i], A+1):
            if T[j] > 1 + T[j - V[i]]:
                T[j] = 1 + T[j - V[i]]
                coinUsed[j] = i
    index = A
    while index > 0:
        C[coinUsed[index]] += 1
        index -= V[coinUsed[index]]
    return C
            

#Return usage error if incorrect number of arguments
if len(sys.argv) != 2:
    print "Usage: " + os.path.basename(__file__) + " <input filename>"

getInputData(sys.argv[1])



for i in range(len(amounts)):
    print(changedp(amounts[i], denoms[i]))



