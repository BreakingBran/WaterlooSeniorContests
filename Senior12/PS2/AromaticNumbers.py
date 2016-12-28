"""
author: Lance Pereira
date: 2016/12/25
name: Aromatic Numbers
"""

patternDict = {"First":2000,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def main():
	pattern = input("What is the string:")
	counter = 1
	totalSum = 0
	tempSum = 0
	meomarySum = 0
	lastSymbol = "First"
	for values in pattern:
		if counter:
			tempSum = int(values)
			counter = 0
		else:
			tempSum = tempSum*patternDict[values]
			if patternDict[values] > patternDict[lastSymbol]:
				totalSum -= 2*meomarySum
			totalSum += tempSum
			lastSymbol = values
			meomarySum = tempSum
			counter = 1
	print(totalSum)

main()