from graph import getGraph
import sys, os, subprocess

(graph, numOfE) = getGraph()
cnfFile = open("GCP_To_SAT.cnf", mode='w')

def main():
	global graph, cnfFile
	
	k = 2
	status = getStatus(k)

	while(status != "SAT"):
		k = k + 1
		status = getStatus(k)

	print("INPUT GRAPH")
	for vtex in graph:
		print(vtex, "->", graph[vtex])
	print("The chromatic index of the given graph is: {0:d}\n".format(k))
		

def unityClause(k):
	global graph, cnfFile
	
	for vtex1 in range(len(graph) * k):
		cnfFile.write("{0:d} ".format(vtex1 + 1))

	cnfFile.write("0\n")


def type1Clause(k):
	global graph, cnfFile

	for vtex1 in graph:
		for vtex2 in graph[vtex1]:
			for c in range(1, k + 1):
				a = (vtex1 - 1) * k + c
				b = (vtex2 - 1) * k + c

				cnfFile.write("-{0:d} -{1:d} 0\n".format(a, b))


def type2Clause(k):
	global graph, cnfFile

	for vtex1 in graph:
		for c in range(1, k + 1):
			for d in range(c + 1, k +1):
				a = (vtex1 - 1) * k + c
				b = (vtex1 - 1) * k + d

				cnfFile.write("-{0:d} -{1:d} 0\n".format(a, b))


def type3Clause(k):
	global graph, cnfFile

	for vtex1 in graph:
		for c in range(1, k + 1):
			a = (vtex1 - 1) * k + c
			cnfFile.write("{0:d} ".format(a))

		cnfFile.write("0\n")


def genCNF(k):
	global cnfFile

	numOfV = len(graph)
	global numOfE

	variables = k * numOfV
	clauses = numOfV + ((k * (k-1) * numOfV) / 2) + (k * numOfE) + 1

	cnfFile = open("GCP_To_SAT.cnf", mode='w')

	cnfFile.write("c Graph Coloring to SAT converter\n")
	cnfFile.write("c Code by hackrush\n")
	cnfFile.write("c Under the guidance of D. Mitra Sir\n")
	cnfFile.write("c NIT - Durgapur, WB\n")
	cnfFile.write("p cnf {0:d} {1:d}\n".format(variables, int(clauses)))

	unityClause(k)
	type1Clause(k)
	type2Clause(k)
	type3Clause(k)
		
	cnfFile.close()
	nullOut = open(os.devnull, "w")
	subprocess.call(['minisat', 'GCP_To_SAT.cnf', 'GCP_To_SAT.sol'], stdout=nullOut)


def getStatus(k):
	genCNF(k)
	solFile = open("GCP_To_SAT.sol", mode='r')
	content = solFile.read().splitlines()
	status = content[0]

	return status


if __name__ == '__main__':
	main()
