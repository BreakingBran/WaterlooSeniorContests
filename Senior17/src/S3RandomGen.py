import time
import random 

#First get how many boards they are going to give mean

numberOfBoards = int(input())

#Then take in the list of numbers that they're going to give me

#listOfBoardNumbers = input().split(" ") #SUPER IMPORTANT TOOK OUT JUST FOR TESTING

listOfBoardNumbers = [random.randint(0,1000) for r in range(numberOfBoards)]
#print(listOfBoardNumbers)

firstStart = time.time()
start_time = time.time()

#listOfBoardNumbers = [int(x) for x in listOfBoardNumbers] #SUPPPPPPPPPPPPPERR IMPORTANT TOOK OUT FOR TESTING


#SUPER IMPORTANT MAKE SURE TO CHECK ###############################
#listOfBoardNumbers.sort()

#Then create a matrix with the sum of all pairs of numbers 

boardMatrix = [0]*numberOfBoards #Make sure it doesn't make one extra colunm
lengthOfBoardList = len(listOfBoardNumbers)

print("--- %s seconds --- Initializing and sorting list" % (time.time() - start_time))
start_time = time.time()

for colunmValueIndex in range(lengthOfBoardList-1):
    
    boardMatrix[colunmValueIndex] = [0]*numberOfBoards
    boardMatrix[lengthOfBoardList-1] = [0]*numberOfBoards
    
    for rowValueIndex in range( (colunmValueIndex+1), lengthOfBoardList):
        sumofBoardPair = (listOfBoardNumbers[colunmValueIndex] + listOfBoardNumbers[rowValueIndex])
        boardMatrix[colunmValueIndex][rowValueIndex] = sumofBoardPair

"""for colIndex in range(lengthOfBoardList):
    print(values)"""    

print("--- %s seconds --- creating boardMatrix" % (time.time() - start_time))

#create a function that goes through left and bottom side tracing diagnols up to the RIGHT

def diagnolTraverser(colunmValueIndex,rowValueIndex):
    #start_time = time.time()
    valueDictionary = {}
    #Create dictionaries in the function that track the freuqency of a count
    newRowValueIndex = rowValueIndex
    for newColunmValueIndex in range(colunmValueIndex,lengthOfBoardList):
        #print(newColunmValueIndex,newRowValueIndex)
        matrixValue = boardMatrix[newColunmValueIndex][newRowValueIndex]
        if matrixValue != 0:
            valueDictionary[(matrixValue)] = valueDictionary.get(matrixValue, 0) + 1
        else:
            break

        if (newRowValueIndex - 1) > 0:
            newRowValueIndex -= 1
        else:
            break
    maxValue =  max(valueDictionary.values())
    counter = 0
    for keys in valueDictionary.keys():
        if valueDictionary[keys] == maxValue:
            counter += 1
    # points = "%d,%d" % (colunmValueIndex,rowValueIndex)
    #print("--- %s seconds --- at %s iteration of dagnolTraverser" % (time.time() - start_time,points))
    return [maxValue,counter]
        
allBoardMaxPairSumFrequency = 0
allBoardcounter = 0

start_time = time.time()
            
#print(diagnolTraverser(boardMatrix,0,3))  
#Sweet its working)

for rowIndexValue in range(1,lengthOfBoardList):
    
    (maxFreqFromIter,maxCounterFromIter) = diagnolTraverser(0,rowIndexValue)
    if maxFreqFromIter > allBoardMaxPairSumFrequency:
        allBoardMaxPairSumFrequency = maxFreqFromIter
        allBoardcounter = maxCounterFromIter
    elif maxFreqFromIter == allBoardMaxPairSumFrequency:
        allBoardcounter += maxCounterFromIter

print("--- %s seconds --- to go through rows of the matrix and do frequency analysis" % (time.time() - start_time))
start_time = time.time()
        
for colunmIndexValue in range(1,lengthOfBoardList-1): #SHOULD BE 1111 JUANNNNNNNN
    
    (maxFreqFromIter,maxCounterFromIter) = diagnolTraverser(colunmIndexValue,(lengthOfBoardList-1))
    if maxFreqFromIter > allBoardMaxPairSumFrequency:
        allBoardMaxPairSumFrequency = maxFreqFromIter
        allBoardcounter = maxCounterFromIter
    elif maxFreqFromIter == allBoardMaxPairSumFrequency:
        allBoardcounter += maxCounterFromIter

print("--- %s seconds --- to go through colunms of matrix and do frequency analysis" % (time.time() - start_time))

print(allBoardMaxPairSumFrequency,allBoardcounter)

print("--- %s seconds --- to finish the entire program" % (time.time() - firstStart))