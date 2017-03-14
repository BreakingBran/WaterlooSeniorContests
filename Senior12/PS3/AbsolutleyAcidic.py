"""
author: Lance Pereira
date: 2016/12/25
name: Aromatic Numbers
"""

frequencyDictionary = {}

def main():

	numberOfSensors = input("Number of sensors: ")
	frequencyDictionaryValues = []
	highestFreq = 0
	secondHighestFreq = 0

	for i in range(0,int(numberOfSensors)):

		sensorValue = input("Value of sensor: ")

		if sensorValue in frequencyDictionary:
			frequencyDictionary[sensorValue] += 1
		else:
			frequencyDictionary[sensorValue] = 1
	frequencyDictionaryValues = list(frequencyDictionary.values())
	highestFreq = max(frequencyDictionaryValues)
	secondHighestFreq = secondHighest(frequencyDictionaryValues,highestFreq)

	output = maxDiffirence(highestFreq,secondHighestFreq, frequencyDictionary)

	print(output)
	

def secondHighest(Freqlist,maxNumber = 1000):
	Freqlist.sort()
	#print(Freqlist)
	secondHighest = maxNumber
	for values in range(len(Freqlist)-1,-1,-1):
		#print(Freqlist[values])
		if Freqlist[values] < maxNumber:
			secondHighest =  Freqlist[values]
			break
	return secondHighest

def maxDiffirence(highestFreq,secondHighestFreq,frequencyDictionary):
	#print(highestFreq,secondHighestFreq)
	highestFreqList = []
	secondHighestFreqList = []
	for key,value in frequencyDictionary.items():

		if value == highestFreq:
			highestFreqList.append(int(key))

		elif value == secondHighestFreq:
			secondHighestFreqList.append(int(key))

	maxHighestFreq = max(highestFreqList)
	lowestSecondHighestFreq = min(secondHighestFreqList)
	#print(highestFreqList)
	#print(secondHighestFreqList)
	return (maxHighestFreq - lowestSecondHighestFreq)

main()