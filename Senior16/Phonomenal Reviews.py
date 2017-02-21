
"""
Take in input for the amount of nodes in the tree

Take in input for the amount of special nodes in the tree

Take in a list of all the special nodes names

Take n-1 lines of node attatchments
"""

NumberOfNodes = 0
NumberOfSpecialNodes = 0
NodeList = []
listOfSpecialNodes = []

class Nodes(object):

	"""
	each node is made an object with a name and list that shows its paths
	"""

	def __init__(self, number):


		self.number = number
		self.listPos = [0]*NumberOfNodes
		self.connections = 0

	def addConnection(self,otherNodeNumber):
		self.listPos[otherNodeNumber] = 2
		self.connections += 1

class SpecialNodes(Nodes):

	def __init__(self, number):
		super(SpecialNodes, self).__init__(number)
		self.listPos[self.number] = 3
		self.distanceFromSpecialNodes = [0]*NumberOfSpecialNodes

	def setDistanceFromOtherNodes(self,distance):
		pass
		

#Takes input of number of nodes and special nodes
NumberOfNodes,NumberOfSpecialNodes = input().split(" ")

#Turns them into ints
NumberOfNodes = int(NumberOfNodes)
NumberOfSpecialNodes = int(NumberOfSpecialNodes)

#Takes input of names of all special nodes
listOfSpecialNodes = input().split(" ")
listOfSpecialNodes = [int(x) for x in listOfSpecialNodes]

NodeList = [SpecialNodes(x) if x in listOfSpecialNodes else Nodes(x) for x in range(0,NumberOfNodes)]


#Takes in the connections between nodes
for i in range(0,NumberOfNodes-1):
	x,y = input().split(" ")
	x = int(x)
	y = int(y)
	NodeList[x].addConnection(y)
	NodeList[y].addConnection(x)

"""print("    {1, 2, 3, 4, 5, 6, 7, 8}")

for nodes in NodeList:
	print(("{%s} " + str(nodes.listPos)) %  str((nodes.number)) )"""

def specialNodeDistance():
	'''
	This thing traverses the matrix 

	    {1, 2, 3, 4, 5, 6, 7, 8}
	{0} [3, 2, 2, 0, 0, 0, 0, 0]
	{1} [2, 0, 0, 0, 0, 2, 2, 0]
	{2} [2, 0, 0, 2, 0, 0, 0, 0]
	{3} [0, 0, 2, 3, 2, 0, 0, 2]
	{4} [0, 0, 0, 2, 3, 0, 0, 0]
	{5} [0, 2, 0, 0, 0, 0, 0, 0]
	{6} [0, 2, 0, 0, 0, 0, 3, 0]
	{7} [0, 0, 0, 2, 0, 0, 0, 3]

	and finds the amount of turns it takes to reach each 3 from a single randomly chose node
	'''

	initalStartingSpecialNode = listOfSpecialNodes[0]

	nodeMatrix = [ x.listPos for x in NodeList]

	#print(nodeMatrix)

	def distanceTracker(x,y):

		for i in range(nodeMatrix):

			for j in range(nodeMatrix):




specialNodeDistance()