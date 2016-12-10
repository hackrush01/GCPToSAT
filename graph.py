import sys

def getGraph():
	
	if len(sys.argv) == 1:
		print ("\nSince no file is specified: Opening Default Graph File\n")
		file = open("graph.txt", mode="r")
	else:
		try:
			print ("\nTrying To Open User Specified Graph File...")
			file = open(sys.argv[1], mode="r")
			print ("File Successfully Opened\n")
		except:
			print ("Invalid file or file path")
			print ("Exiting...")
			exit()
	
	content = file.read().splitlines()
	
	numOfV = int(content[0])
	numOfE = 0

	graph = {(vtex + 1) : [] for vtex in range(numOfV)}
	
	for edge in content[1:]:
	
		edge = [int(n) for n in edge.split()]
		graph[edge[0]].append(edge[1])
		numOfE += 1
	
	file.close()
	return (graph, numOfE)
