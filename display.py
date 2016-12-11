import networkx as nex
import matplotlib.pyplot as plot
import sys, random
from graph import getGraph

def plotGraph(graph, k):
	G = nex.from_dict_of_lists(graph)

	file = open("GCP_To_SAT.sol", mode='r').read().splitlines()
	result = file[1].split()

	colors = ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(k)]

	colorMap = []
	for i in result:
		color = int(i)
		if color > 0:
			colorMap.append(colors[color%k])
	
	nex.draw(G, node_color=colorMap, node_size=800, with_labels = True)
	plot.show()