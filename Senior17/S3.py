
#First get how many boards they are going to give mean

numberOfBoards = int(input())

#Then take in the list of numbers that they're going to give me

listOfBoardNumbers = input().split(" ")
listOfBoardNumbers = [int(x) for x in listOfBoardNumbers]
listOfBoardNumbers.sort()

#Then create a matrix with the sum of all pairs of numbers 

boardMatrix = [0]*numberOfBoards #Make sure it doesn't make one extra colunm
lengthOfBoardList = len(listOfBoardNumbers)

for colunmValueIndex in range(lengthOfBoardList-1):
    
    boardMatrix[colunmValueIndex] = [0]*numberOfBoards
    boardMatrix[lengthOfBoardList-1] = [0]*numberOfBoards
    
    for rowValueIndex in range( (colunmValueIndex+1), lengthOfBoardList):
        sumofBoardPair = (listOfBoardNumbers[colunmValueIndex] + listOfBoardNumbers[rowValueIndex])
        boardMatrix[colunmValueIndex][rowValueIndex] = sumofBoardPair

print(boardMatrix)    

#create a function that goes through left and bottom side tracing diagnols up to the RIGHT

def diagnolTraverser(colunmValueIndex,rowValueIndex):
    
    valueDictionary = {}
    #Create dictionaries in the function that track the freuqency of a count
    newRowValueIndex = rowValueIndex
    for newColunmValueIndex in range(colunmValueIndex,lengthOfBoardList):
        #print(newColunmValueIndex,newRowValueIndex)
        matrixValue = boardMatrix[newColunmValueIndex][newRowValueIndex]
        if matrixValue != 0:
            valueDictionary[(matrixValue)] = valueDictionary.get(matrixValue, 0) + 1

        if (newRowValueIndex - 1) > 0:
            newRowValueIndex -= 1
        else:
            break
    maxValue =  max(valueDictionary.values())
    counter = 0
    for keys in valueDictionary.keys():
        if valueDictionary[keys] == maxValue:
            counter += 1
    return [maxValue,counter]
        
allBoardMaxPairSumFrequency = 0
allBoardcounter = 0
            
#print(diagnolTraverser(boardMatrix,0,3))  
#Sweet its working)

for rowIndexValue in range(1,lengthOfBoardList):
    
    (maxFreqFromIter,maxCounterFromIter) = diagnolTraverser(0,rowIndexValue)
    if maxFreqFromIter > allBoardMaxPairSumFrequency:
        allBoardMaxPairSumFrequency = maxFreqFromIter
        allBoardcounter = maxCounterFromIter
    elif maxFreqFromIter == allBoardMaxPairSumFrequency:
        allBoardcounter += maxCounterFromIter
        
for colunmIndexValue in range(0,lengthOfBoardList-2):
    
    (maxFreqFromIter,maxCounterFromIter) = diagnolTraverser(colunmIndexValue,(lengthOfBoardList-1))
    if maxFreqFromIter > allBoardMaxPairSumFrequency:
        allBoardMaxPairSumFrequency = maxFreqFromIter
        allBoardcounter = maxCounterFromIter
    elif maxFreqFromIter == allBoardMaxPairSumFrequency:
        allBoardcounter += maxCounterFromIter

print(allBoardMaxPairSumFrequency,allBoardcounter)
    