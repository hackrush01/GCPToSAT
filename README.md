# GCP To SAT
A simple python code which reduces the Graph Colorablity Problem to Boolean Satisfiability Problem.

# Requirements
0. Python 3  
0. minisat solver from https://github.com/niklasso/minisat  

# Install Instructions
0. cd to your home directory `cd ~`
0. create new folder for git repositories `mkdir gitRepos`
0. cd to the newly created folder `cd gitRepos`
0. clone this repo to you folder `git clone https://github.com/hackrush01/GCP_To_SAT.git`
0. run using `python3 GCP_To_SAT.py <path-to-graph-file>`

> Note: Complete installation instructions for MiniSat Solver are mentioned in it's respective repository but in short:

0. cd to your git repo folder created above `cd ~/gitRepos`
0. clone minisat `git clone https://github.com/niklasso/minisat.git`
0. cd to minisat directory `cd minisat`
0. install using `sudo make install`

# How to run
Just install the minisat solver in your preferred linux distro. After that just execute the python file. 

# Input Format
Make a graph.txt file in the same directory as the git repository or run the program as follows
`python3 GCP_To_SAT.py <path-to-graph-file>`.

It's important to note that the graph text file must adhere to the standard input format i.e.

0. First line contains exactly one number defining the number of vertices.
0. After that each line should contain exactly one edge with space separated vertices.(e.g. 5 8, indicates an edge between 5th and 8th vertices)
0. All edges are 1-indexed.
0. Since the graph is undirectional, so the edges should not be repeated. It doesn't change the solution but the number of clauses increases, decreasing the performance. One example graph.txt file is included.

