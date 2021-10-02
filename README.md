# vaccine_development
Map which vaccines are effective against which strains

## Problem Statement
Since the advent of different viral strains, governments across the world are researching combining available vaccines to enhance immunity. Vaccines can be deployed after a gap of a few months to battle various strains. Assume that you are a global COVID vaccine researcher and you want to map which vaccines have been found effective against a virus strain (either in the past or present). For this you need to have some system of storing these vaccines and the strains they have neutralized.

Assume that you have a list of N strains and M vaccines. For the sake of this assign ment, let us assume that a particular vaccine could neutralize only two strains at max.

Write an application that maps COVID Strains and Vaccines and can answer the below queries

1. List the unique strains and vaccines the researcher has collected in the system.
2. For a particular strain, help the reporter recollect the vaccines it has been
neutralized by.
3. For a particular vaccine, list the strains that have been neutralized with it (past or
present).
4. Identify if two vaccines neutralize similar strains. Vaccine A and vaccine B are
considered to neutralize similar strains if they have been associated with the same
strains (not necessarily at the same time or in the same year)
5. Can two vaccines A and B be connected such that there exists another vaccine C
where A and C are neutralizing similar strains and C and B are neutralizing similar strains

## Solution Design

As we can see that vaccines are connected to strains, and strains are vice versa connected to vaccines, so we can easily see a network getting formed.

So taking into consideration the graph formed, we formed the following class for our problem statement:

* def addToStrains(self, strain, vaccines): # function to add strains
* def constructMatrix(self, lines): # to construct matrix of relations from input def readInputFile(self, inputFile): # to read input file for strain data
* def writeToOutput(output): # to write to output file
* def displayAll(self): # to display all distinct vaccine and strains in input def addToVaccineList(self, vaccines): # function to add vaccines
* def updateVaccineAssociations(self): # establish vaccine to strain relations def displayStrains(self, vaccine): # display distinct strains for vaccine
* def displayVaccine(self, strain): # display a vaccine for a specific strain def commonStrain(self, vacA, vacB): # common strain connection b/w 2 vaccines def findVaccineConnect(self, vacA, vacB): # find if 2 vaccines are connected

We are checking a graph's connectivity between two vaccines using the following principles:
1. Start a DFS traversal at the source vaccine, vacA
2. Check, after the algorithm halts, whether we have successfully traced the path till destination vaccine vacB.
3. If they have, the vaccines are connected; otherwise, vaccines are not connected


## Solution and Algorithm Design
We have chosen to use the DFS(Depth First Search) algorithm for solving this problem. For
traversing the vaccine and strains path which are

### Five general scenarios of DFS which we have used in our algorithm are:

1. If a child node exists and it has not yet been explored, traverse to the child.
2. If a right sibling exists and it has not yet been explored, traverse to the right.
3. If we are at the rightmost child and we can retreat to the left, traverse to the left. (retreat)
4. If we are not at the leftmost child but we have already explored siblings to the right, traverse
to the left. (retreat)
5. Otherwise, traverse to the parent. Note: If none of the previous conditions are true, we must
be at the leftmost child and all siblings to the right have already been explored. (retreat)


### Pseudo code for Depth First Search or DFS Traversal to find path b/w 2 vaccines:

```
findVaccineConnect(vacA, vacB):
find all strains for vacA and initialize a stack with strains initialize path and visited queues with vacA
while stack is not empty:
top = strain stack.pop()
path.add(top) => add top to path
if top == vacB: => checking if we have reached vacB
break loop
if top is not visited:
explore its children (vaccines/strain) and add to stack
mark top as visited
if last entry of path != vacB: => checking if the path’s last entry is not vacB
return err else:
return path => On success, return the path of the relation found

```

### Runtime analysis and algorithm description
V= Vertices (Vaccines + Strains)
E= Relations b/w Vaccines & Strains


### Time Complexity

In the worst case scenario, all the nodes and vertices are visited, the average time complexity for DFS on a graph is O(V + E), where V is the number of vertices and E is the number of edges.

In case of DFS on a tree, the time complexity is O(V), where V is the number of vertices strongly connected we have used DFS which produces a path from vaccine A to vaccine B. So, we can successfully concur that there exists a relation between 2 vaccines through strains and vice versa.

Asymptomatically speaking, it would tend to approach linear time complexity in worst case, i.e. O(n), since the maximum number of nodes traversed in the worst case would be a combined set of all vaccines and strains in the network.

In all the functions, we never exceed O(n) because we never exceed O(V) in each function.

### Space Complexity
Since 2 extra visited arrays are needed of size Vaccines and Strains to store all the siblings to be explored in the graph, so total space complexity would be, O(No. of Vaccines) + O(No. of Strains) + O(Elements in Path Queue)= 2*O(V) where V is the total number of vertices, (since # vaccines + # strains = V).

So total space complexity asymptomatically speaking would be O(V) which would again mean linear time complexity or O(n).

## Alternate way of modelling the problem with the cost implications

### Breadth First Search or BFS:

We could have used BFS as well, where we could have used an approach to explore all the nodes breadth wise, and BFS is also O(V+E) in the worst case scenario, which is again linear time complexity. But DFS is treated as the best way to explore the path between two nodes, since the average case scenario for DFS is marginally better as it explores the existing connection further, hence we used DFS instead of BFS in this problem statement.
