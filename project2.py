import sys
import os
import time
import xlsxwriter

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

def timeFunction(functionToCall, inputSizes):
    timeList = []
    #go through all input Sizes
    for i in inputSizes:
        VLists = []
        #need to make 10 arrays given
        for j in range(10):
            VLists = []
            #append i random integers to a list
            for k in range(i):
                a.append(random.randint(-1000,1000))
            currLists.append(a)


        #currLists now holds 10 arrays of size i
        #call and time the function with 10 different arrays for each inputSize
        times = []
        for j in range(10):
            startTime = time.time()
            functionToCall(currLists[j])
            times.append(time.time() - startTime)
        avgTime = sum(times) / 10.0
        timeList.append(avgTime) #timeList holds the averages for all
    return timeList

'''
Brute Force algorithm
'''
def changeslow(A, V):
    C = []
    changeMade = 0
    denomCoins = {}
    for i in V:
        C.append(0)

    for i in range(len(V)):
        coin = V[i]
        denom = V[i]
        denomCoins[denom] = [0, C[:]]
        while changeMade < A:
            if changeMade + coin <= A:
                denomCoins[denom][0] += 1
                denomCoins[denom][1][i] += 1
                changeMade += coin

            else:
                for j in reversed(range(i)):
                    coin = V[j]
                    while changeMade + coin <= A:
                        denomCoins[denom][0] += 1
                        denomCoins[denom][1][j] += 1
                        changeMade += coin

        changeMade = 0

    lowestCombination = min(denomCoins.values())
    lowestList = lowestCombination[1]
    C = lowestList[:]
    return C

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

'''Greedy algorithm
'''

def changegreedy(A, V):
	coinsCount = [0 for x in range(len(V))]
	#V.reverse()
	#for i in V:
	#	while A >= i:
	#		A -= i
	#		coinsUsed.append(i)
	x = len(V) - 1

	while(A > 0):
		if (A >= V[x]):
			A -= V[x]
			coinsCount[x] += 1
		else:
			x -= 1

	return coinsCount



'''
Takes in function of algorithm
returns a list of the number of coins for each A
also prints time taken for each A
'''
def problem3(function):
    V = [1, 5, 10, 25, 50]
    A = []
    timeList = []
    numCoinsList = []
    for i in range(2010, 2201, 5): #might need to change these
        A.append(i)
    for i in A:
        startTime = time.time()
        C = function(i, V)
        timeList.append(time.time() - startTime)
        numCoinsList.append(sum(C))

    outputData(A, numCoinsList, timeList, 'problem3.xlsx')
    '''
    print("Times for each amount:")
    for i in range(len(A)):
        print( "A = " + str(A[i]) + ": " + str(timeList[i]) + "sec")
    '''
    return numCoinsList

def problem4V1(function):
    V = [1, 2, 6, 12, 24, 48, 60]
    A = []
    timeList = []
    numCoinsList = []
    for i in range(2010, 2201, 5): #might need to change these
        A.append(i)
    for i in A:
        startTime = time.time()
        C = function(i, V)
        timeList.append(time.time() - startTime)
        numCoinsList.append(sum(C))

    outputData(A, numCoinsList, timeList, 'problem4V1.xlsx')
    '''
    print("Problem 4 for list V1")
    print("Times for each amount:")
    for i in range(len(A)):
        print( "A = " + str(A[i]) + ": " + str(timeList[i]) + "sec")
    '''
    return numCoinsList

def problem4V2(function):
    V = [1, 6, 13, 37, 150]
    A = []
    timeList = []
    numCoinsList = []
    for i in range(2010, 2201, 5): #might need to change these
        A.append(i)
    for i in A:
        startTime = time.time()
        C = function(i, V)
        timeList.append(time.time() - startTime)
        numCoinsList.append(sum(C))

    outputData(A, numCoinsList, timeList, 'problem4V2.xlsx')
    '''
    print("Problem 4 for list V2")
    print("Times for each amount:")
    for i in range(len(A)):
        print( "A = " + str(A[i]) + ": " + str(timeList[i]) + "sec")
    '''
    return numCoinsList

def problem5(function):
    V = []
    for i in range(30):
        V.append(i+1)
    A = []
    timeList = []
    numCoinsList = []
    for i in range(2000, 2201): #might need to change these
        A.append(i)
    for i in A:
        startTime = time.time()
        C = function(i, V)
        timeList.append(time.time() - startTime)
        numCoinsList.append(sum(C))
    outputData(A, numCoinsList, timeList, 'problem5.xlsx')
    '''
    print("Problem 5")
    print("Times for each amount:")
    for i in range(len(A)):
        print( "A = " + str(A[i]) + ": " + str(timeList[i]) + "sec")
    '''
    return numCoinsList

def outputData(A, numCoinsList, timeList, filename):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for i in range(len(A)):
        worksheet.write(row, 0, A[i])
        worksheet.write(row, 1, timeList[i])
        worksheet.write(row, 2, numCoinsList[i])
        row += 1
    workbook.close()

#Return usage error if incorrect number of arguments
if len(sys.argv) != 2:
    print "Usage: " + os.path.basename(__file__) + " <input filename>"



'''
This command takes in the data from a file and
fills global list amounts and list of lists denoms
where amounts[i] corresponds to denoms[i]
'''

getInputData(sys.argv[1])
for i in range(len(amounts)):
    C = changegreedy(amounts[i], denoms[i])
    print "C = ",
    print C,
    print "; m = " + str(sum(C))


'''
These commands will print the list of the number of coins for each
amount asked for in the problems. They will also output time data
to problemX.xlsx, with the amount, A, in the first column, number of coins
in the 2nd, and time in the 3rd.
'''
'''
print(problem3(changedp))
print(problem4V1(changedp))
print(problem4V2(changedp))
print(problem5(changedp))
'''

print(problem3(changegreedy))
print(problem4V1(changegreedy))
print(problem4V2(changegreedy))
print(problem5(changegreedy))
'''
print(problem3(changeslow))
print(problem4V1(changeslow))
print(problem4V2(changeslow))
print(problem5(changeslow))
'''
