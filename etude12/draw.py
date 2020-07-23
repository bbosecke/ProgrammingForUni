from collections import deque, namedtuple
import sys
import re
import pprint
import argparse
import networkx as nx
import matplotlib.pyplot as plt

# Etude 12, Drawing Bus Routes
# Drawing bus routes finds the shortest path first from an input file containing a key route as line one (e.g. A, B\n)
# and lines 2->n as (e.g. A, E, 22\nB, C, 15\n...)
# It draws to a .png file
# Brodie Bosecke
#

key_route = []
routes = []
index = 1
start = ''
end = ''
final_route_start = []
final_route_end = []
final_route_cost = []
#graph = ""


def file():
	global index
	import sys

	#checks if no input is parsed, if so program exits
	if not sys.stdin.isatty():
		tempo = sys.stdin.readlines()
	else:
		sys.exit("Invalid: No input")

	for element in tempo:

		if(index == 1):
			key_route.append(element.strip('\n').rstrip().lstrip().lower())
			index = 5
		else:
			routes.append(element.strip('\n').rstrip().lstrip().lower())

# This function checks to ensure that there is a 2 comma seperated value
#	i.e. "christchurch, dunedin". Also checks if alnum
def check_key_route(i):
	party = i.split(', ')
	county = len(party)
	#checks if there is 2 'parts' to county (i.e. "start, end")
	if(county != 2):
		return False
	for a in party:
		blah = a.replace(' ', '')
		isAlnum = blah.isalnum()
		if(isAlnum == False):
			return False

# This function checks to ensure that there is a 3 comma seperated value
#	i.e. "christchurch, timaru, 12.5". It removes any '.' for an alnum check
def check_main_route(i):
	#for j in i:
	parts = i.split(',  ')
	partsy = str(parts).split(', ')
	#print(partsy)
	count2 = len(partsy)
	#checks if there is 3 'parts' to each line (i.e. "start, end, cost")
	if(count2 != 3):
		return False
	temp = str(parts).replace('.', '')
	if(temp.isalnum == False):
		return False


# This stores the start and end destination into VAR start and VAR end respectively
def key_route_split(key_route):
	global start
	global end
	parts = []
	parts = key_route.split(', ')
	start = parts[0]
	end = parts[1]
		
# This splits the routes into the correct end, start and cost lists
def main_route_split(routes):
	global final_route_end
	global final_route_start
	global final_route_cost
	for i in routes:
		k = i.replace(' , ', ',')
		l = k.replace(' ,', ',')
		m = l.replace(', ', ',')
		n = m.replace(',', ', ')
		parts = n.split(', ')
		count2 = len(parts)
		if(count2 == 3):
			final_route_start.append(parts[0])
			final_route_end.append(parts[1])
			final_route_cost.append(parts[2])
		else:
			return False

file()
for i in key_route:
	k = i.replace(' , ', ',')
	l = k.replace(' ,', ',')
	m = l.replace(', ', ',')
	n = m.replace(',', ', ')
	checker = check_key_route(n)
	if(checker == False):
		sys.exit("Invalid: route")
		#exit program

"""checkered = check_main_route(routes)
if(checkered == False):
	sys.exit("Invalid: route set")"""
	#exit program
key_route_split(n)
#main_route_split(routes)
#print(len(final_route_start))
#print(len(final_route_end))
#print(len(final_route_cost))
#print(final_route_start[5])
#print(final_route_end[5])
#print(final_route_cost[5])

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)

#https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
class Graph:
	def __init__(self, edges):
		# let's check that the data is right
		wrong_edges = [i for i in edges if len(i) not in [2, 3]]
		if wrong_edges:
			raise ValueError('Wrong edges data: {}'.format(wrong_edges))

		self.edges = [make_edge(*edge) for edge in edges]

	@property
	def vertices(self):
		return set(
			sum(
				([edge.start, edge.end] for edge in self.edges), []
			)
		)

	def get_node_pairs(self, n1, n2, both_ends=True):
		if both_ends:
			node_pairs = [[n1, n2], [n2, n1]]
		else:
			node_pairs = [[n1, n2]]
		return node_pairs

	def remove_edge(self, n1, n2, both_ends=True):
		node_pairs = self.get_node_pairs(n1, n2, both_ends)
		edges = self.edges[:]
		for edge in edges:
			if [edge.start, edge.end] in node_pairs:
				self.edges.remove(edge)

	def add_edge(self, n1, n2, cost=1, both_ends=True):
		node_pairs = self.get_node_pairs(n1, n2, both_ends)
		for edge in self.edges:
			if [edge.start, edge.end] in node_pairs:
				return ValueError('Edge {} {} already exists'.format(n1, n2))

		self.edges.append(Edge(start=n1, end=n2, cost=cost))
		if both_ends:
			self.edges.append(Edge(start=n2, end=n1, cost=cost))

	@property
	def neighbours(self):
		neighbours = {vertex: set() for vertex in self.vertices}
		for edge in self.edges:
			neighbours[edge.start].add((edge.end, edge.cost))

		return neighbours

	def dijkstra(self, source, dest):
		assert source in self.vertices, 'Such source node doesn\'t exist'
		distances = {vertex: inf for vertex in self.vertices}
		previous_vertices = {
			vertex: None for vertex in self.vertices
		}
		distances[source] = 0
		vertices = self.vertices.copy()

		while vertices:
			current_vertex = min(
				vertices, key=lambda vertex: distances[vertex])
			vertices.remove(current_vertex)
			if distances[current_vertex] == inf:
				break
			for neighbour, cost in self.neighbours[current_vertex]:
				alternative_route = distances[current_vertex] + float(cost)
				if alternative_route < distances[neighbour]:
					distances[neighbour] = alternative_route
					previous_vertices[neighbour] = current_vertex

		path, current_vertex = deque(), dest
		while previous_vertices[current_vertex] is not None:
			path.appendleft(current_vertex)
			current_vertex = previous_vertices[current_vertex]
		if path:
			path.appendleft(current_vertex)
		return path

# this function creates a list of tuples to use with the Graph function. It appends each tuple to the
# list, listOfTuples
listOfTuples = []
def makeTuples(routes):
	for i in routes:
		k = i.replace(' , ', ',')
		l = k.replace(' ,', ',')
		m = l.replace(', ', ',')
		n = m.replace(',', ', ')
		checkered = check_main_route(n)
		if(checkered == False):
			sys.exit("Invalid: route set")
		res = tuple(map(str, n.split(', ')))
		listOfTuples.append(res)

def checkDuplicates(i):
	one = []
	two = []
	y = 0
	for j in i:
		one.append(j[0])
		two.append(j[1])
	for i in one:
		uniqueCheck = one[y] + ", " + two[y]
		uniqueChecker = two[y] + ", " + one[y]
		unList.append(uniqueCheck)
		unList.append(uniqueChecker)
		y += 1

#https://stackoverflow.com/questions/28202634/check-for-duplicates-in-a-python-list
def check_list(arg):
	for i in arg:
		if arg.count(i) > 1:
			return True
	return False

unList = []
makeTuples(routes)
#duplicate route check happens here
checkDuplicates(listOfTuples)
#unList contains list to check for dupes
gobletOfFire = check_list(unList)
if(gobletOfFire != False):
	sys.exit("Invalid: Non-unique routes")
graph = Graph(listOfTuples)
#print(graph.dijkstra(start, end))

final =str(graph.dijkstra(start, end)).replace("deque","").replace("]","").replace("[","").replace('',"").replace(",","").replace("(","").replace(")","").replace("'","").replace(" ","-")

#print(final)
shortestRoute = final.split('-')
#print(shortestRoute)

#----------------- EVERYTHING UNDER HERE IS FOR THE E12 ------------------------------------------------
G=nx.Graph()

#This function adds the nodes to the graph
def addNode(node):
	for j in node:
		G.add_node(j)

def addEdge(start, end, cost):
	j = 0
	for i in start:
		G.add_edge(start[j], end[j], weight = float(cost[j]))
		j += 1

main_route_split(routes)
addNode(final_route_start)
addEdge(final_route_start, final_route_end, final_route_cost)

#IMPT - THIS WILL SHOW MY GRAPH LABELS

#https://stackoverflow.com/questions/27173581/networkx-color-the-nodes-in-path
# is where I got the idea 
pos = nx.spring_layout(G)
path = nx.shortest_path(G, source=start, target=end, method='dijkstra', weight='weight')
labels = nx.get_edge_attributes(G,'weight')
node_colors = ["orange" if n in path else "blue" for n in G.nodes()]
alphas = [0.8 if n in path else 0.5 for n in G.nodes()]
edgeColor = ['green' if n in path else 'blue' for n in G.nodes()]
dashed = ['solid' if n in path else 'dashed' for n in G.nodes()]

pathLines = [(u,v) for (u,v,d) in G.edges(data=True) if n in path]
notPathLines = [(u,v) for (u,v,d) in G.edges(data=True) if n not in path]
#print(pathLines)
#print(notPathLines)

#https://stackoverflow.com/questions/34120957/python-networkx-mark-edges-by-coloring-for-graph-drawing
# shortest path lines color green, else color blue
for e in G.edges():
	G[e[0]][e[1]]['color'] = 'blue'
for i in range(len(path)-1):
	G[path[i]][path[i+1]]['color'] = 'green'
edge_color_list = [ G[e[0]][e[1]]['color'] for e in G.edges() ]

#https://stackoverflow.com/questions/34120957/python-networkx-mark-edges-by-coloring-for-graph-drawing
# shortest path lines solid else dashed
for e in G.edges():
	G[e[0]][e[1]]['color'] = 'dashed'
for i in range(len(path)-1):
	G[path[i]][path[i+1]]['color'] = 'solid'
dottedAndSolid = [ G[e[0]][e[1]]['color'] for e in G.edges() ]

#whole graph
#nx.draw_networkx(G, pos, node_color='blue', node_size=500, alpha=0.5)

#add labels
#nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#shortest route
#nx.draw_networkx_nodes(G, pos, nodelist=path, node_color=['orange'], node_size=500, alpha=0.8)

plt.title("Cheapest Bus Route - COSC326 - Author: Brodie Bosecke")
#nx.draw_networkx_nodes(G, pos=pos, nodelist=notPathLines, node_color=node_colors, node_size=500, alpha=0.5) #draw nodes

nx.draw_networkx_nodes(G, pos=pos, node_color=node_colors, node_size=500, alpha=alphas) #draw nodes
#nx.draw_networkx_nodes(G, pos=pos, node_color=node_colors, nodelist=notPathLines, node_size=500, alpha=0.5)
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels) #edge 'prices' i.e. '5.5'
nx.draw_networkx_labels(G, pos=pos, edge_labels=labels) #node labels i.e. 'christchurch'
nx.draw_networkx_edges(G, pos=pos, edgelist=pathLines, style=dottedAndSolid, edge_color=edge_color_list, width=2.0, alpha=1.0) #draw lines
nx.draw_networkx_edges(G, pos=pos, edgelist=notPathLines, style=dottedAndSolid, edge_color=edge_color_list, width=2.0, alpha=0.5) #draw lines
#nx.draw_networkx_edges(G, pos=pos, style=dottedAndSolid, edge_color=edge_color_list, width=2.0, alpha=lineTrans) #draw lines

#path lines

#just need to fixe _edges(alpha=lineTrans) then I'm done
plt.savefig('DrawShortestPath.png')