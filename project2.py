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
 


#Return usage error if incorrect number of arguments
if len(sys.argv) != 2:
    print "Usage: " + os.path.basename(__file__) + " <input filename>"
    


getInputData(sys.argv[1])

for i in range(len(amounts)):
    print ("Amount: " + str(amounts[i]) + "; Denominations: " + str(denoms[i]) + '\n')
    




