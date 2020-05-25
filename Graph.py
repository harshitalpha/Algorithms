class Graph: 
	def __init__(self, vertices= 5, typeOfGraph= 'undirected', weight= False): 
		self.vertices = vertices
		self.Adj_list = {}
		self.type = typeOfGraph
		self.have_cycle = False
		self.topo_order = []
		self.back_edges = []
		self.forward_edged = []
		self.tree_edge = []
		self.dfs_done = False
		self.weighted = weight
		self.dfs_tree = {}
		for i in range(vertices):
			self.Adj_list[i] = []


	def add_edge(self, src, dest):  
		# edge from src ---> dest
		self.Adj_list[src-1].append(dest-1)

		if(self.type == 'undirected'):
			# edge from dest ---> src
			self.Adj_list[dest-1].append(src-1)
	

	def remove_edge(self, src, dest):
		try:
			self.Adj_list[src].remove(dest)
			if(self.type == 'undirected'):
				self.Adj_list[dest].remove(src)
		except:
			print("Edge Not Exist")
	

	def get_degree(self,v):
		if(self.type == 'undirected'):
			return len(self.Adj_list[v])
		else:
			out_d = 0
			out_d = len(self.Adj_list[v])
			in_d = 0
			for i in range(self.vertices):
				if v in (self.Adj_list[i]):
					count = 0
					for j in self.Adj_list[i]:
						if j == v:
							count += 1
					in_d = in_d + count
			return out_d,in_d
	
	
	def bfs(self,s):
		level = {s : 0}
		parent = {s : None}

		i = 1

		frontier = [s]
		
		while frontier:
			next_level = []
			for u in frontier:
				for v in self.Adj_list[u]:
					if v not in level.keys():
						level[v] = i
						parent[v] = u
						next_level.append(v)
					else:
						cur_level = level[u]
						after_level = level[v]
						if(cur_level <= after_level):
							self.have_cycle = True
			frontier = next_level
			i = i + 1
		return level, parent
	

	def shortest_path(self, src, dest):
		level, parent = self.bfs(src)
		if dest in level.keys():
			path_len = level[dest]
		else:
			return -1
		
		i = dest
		print(i, end = "->")
		while(parent[i] != src):
			i = parent[i]
			print(i, end = "->")	
		print(src)

		return path_len

	def dfs(self):
		if self.dfs_done == False:
			self.dfs_done = True
			for s in range(self.vertices):
				if s not in self.dfs_tree.keys():
					self.dfs_tree[s] = None
					self.dfs_visit(s)
		else:
			return 


	def can_reach(self,u,v):
		can = False
		while True:
			if self.dfs_tree[u] == v:
				can = True
				return can
			elif self.dfs_tree[u] != None:
				return can
			u = self.dfs_tree[u]


	def dfs_visit(self,s):
		for v in self.Adj_list[s]:
			if v not in self.dfs_tree.keys():
				self.dfs_tree[v] = s
				self.dfs_visit(v)
				self.tree_edge.append([s,v])
			else:
				# todo 
				'''
				if (s in done) and (v in done):
					if done.index(s) > done.index(v):
						self.back_edges.append([s,v])
					elif done.index(s) < done.index(v):
						self.forward_edged.append([s,v])
				'''

		self.topo_order.append(s)




	def topological_sorting(self):
		if (self.type != "undirected") and (not self.is_cycle()):
			self.dfs()
			return self.topo_order[::-1]
		else:
			return "Not Exist, Only exist for DAG"
	




	def is_cycle(self):
		if self.type == 'undirected':
			self.bfs(0)
			return self.have_cycle
		else:
			self.dfs()
			if len(self.back_edges) != 0:
				self.have_cycle = True
				return self.have_cycle
			else:
				self.have_cycle = False
				return self.have_cycle
	

	
	def print_graph(self):
		print(self.Adj_list)





# Driver program to the above graph class 
if __name__ == "__main__": 
	V = 8
	graph = Graph(V, typeOfGraph="directed") 
	graph.add_edge(1,3)
	graph.add_edge(2,3)
	graph.add_edge(2,4)
	graph.add_edge(3,5)
	graph.add_edge(4,6)
	graph.add_edge(5,6)
	graph.add_edge(5,8)
	graph.add_edge(6,7)
	graph.add_edge(8,1)


	graph.print_graph() 


	graph.dfs()

	c = graph.is_cycle()
	print(c)
	
	topo_order = graph.topological_sorting()
	if type(topo_order) != str:
		for i in range(len(topo_order)):
			topo_order[i]+=1
		print(topo_order[::-1])
	else:
		print(topo_order)


	print(graph.back_edges)
	print(graph.tree_edge)
	print(graph.forward_edged)
	
	
	
	#level, parent = graph.bfs(0)
	#print(level)
	#print(parent)
	#print(graph.have_cycle)

	#p_len = graph.shortest_path(2,5)
	#print(p_len)
	'''for i in range(V):
		out_d, in_d = graph.get_degree(i)
		print(out_d, in_d)
	'''
