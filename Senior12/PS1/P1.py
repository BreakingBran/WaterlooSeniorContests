"""
author: Lance Pereira
date: 2016/12/25
name: Don't Pass me the ball
"""

pathDict = {}

def main():
	maxPath = 0
	pathGenerator()
	maxNumber = int(input("What is the max number: "))
	#print("Max number is %d" % (maxNumber))
	layer2list = listCreator(maxNumber,2)
	#print (layer2list)
	for values in layer2list:
		#print ("The path term is %d and it's value is %d" % (values,pathDict[values]))
		maxPath += pathDict[values]
	print(maxPath)
	return maxPath

	
def pathGenerator():
	global pathDict
	sum = 0
	for values in range(1,99):
		sum += values
		pathDict[values] = sum
		#print("The term is %d and the sum is %d" % (values,sum))

def listCreator(maxNumber,minNumber):
	return [x-2 for x in range(maxNumber-1,minNumber,-1)]

main()
