
def main():
	
	#First accept the 2 string that they give me
	# 2nd check if they're the same length
	# run them through a dictionary to doa frequency analysis

	original = input()
	scrambled = input()

	#First level of checking: sees if they're the same length
	if len(original) == len(scrambled):

		#Finds out the frequency of each characted in both words
		originalDict = frequencyAnalysis(original)
		scrambledDict = frequencyAnalysis(scrambled)

		#Creates 0 values for keys that the scramled dict might not have but which the original dict ahs to have
		for key in originalDict.keys():

			if key not in scrambledDict.keys():
				scrambledDict[key] = 0

		#Checks to see that the 2nd string has atleast 1 * but is not completly made up of them
		# as well as checks to see if the scrambled word has any more characters than original
		if ( scrambledDict["*"] == 0 or scrambledDict["*"] == len(original)) or (set(originalDict.keys()) < set(scrambledDict.keys())):

			return "N"

		else:
			#Makes sure there are not more characters in acrambled word compared to original
			for values in original:
				if (originalDict[values] < scrambledDict[values]) :
					return  "N"
	else:
		return "N"

	return "A"




	#Runs a frequency analysis on the variable

def frequencyAnalysis(variable):

	characterDictionary = {}

	characterDictionary["*"] = 0

	for values in variable:
		if values in characterDictionary:
			characterDictionary[values] += 1
		else:
			characterDictionary[values] = 1

	return characterDictionary

print(main())
