from node import Node

class graph:

    def __init__(self, rows, columns):
        self.graph = {}
        for i in range(rows):
            for j in range(columns):
                self.graph[str(i)+str(j)] = 0
        #print (self.graph)

        self.keys = self.graph.keys()

    def __str__(self):
        msg = 'Graph:'
        for i in self.graph:
            msg += '\n  node: ' + i + ' g: ' + \
                str(self.graph[i].g) + ' rhs: ' + str(self.graph[i].rhs) + \
                ' neighbors: ' + str(self.graph[i].successors)
        return msg

    def setGoal(self, node_id):
        if (node_id) in self.keys:
            self.goal = node_id
            #print (self.goal)
        else :
            print ("Enter a valid goal")
    
    def setStart(self, node_id):
        if (node_id) in self.keys:
            self.start = node_id
        else :
            print ("Enter a valid goal")
        
    def getGoal(self):
        # print (self.goal)
        return self.goal
    
    def getStart(self):
        #print (self.goal)
        return self.start


def CreateGraph(grid,rows, columns):

    Graph = graph(rows,columns)

    for i in range(rows):
        for j in range(columns):
            node = Node(str(i)+str(j))
            if (grid[i][j] == 1): #setting edge costs to infinity

                if (i > 0):
                    node.predecessors[str(i-1)+str(j)] = float('inf')
                    node.successors[str(i-1)+str(j)] = float('inf')

                if (j > 0):
                    node.predecessors[str(i)+str(j-1)] = float('inf')
                    node.successors[str(i)+str(j-1)] = float('inf')

                if (i+1< rows):
                    node.predecessors[str(i+1)+str(j)] = float('inf')
                    node.successors[str(i+1)+str(j)] = float('inf')

                if (j+1< columns):
                    node.predecessors[str(i)+str(j+1)] = float('inf')
                    node.successors[str(i)+str(j+1)] = float('inf')

            else:
                if (i > 0):
                   
                    if (grid[i-1][j] == 1):
                        node.predecessors[str(i-1)+str(j)] = float('inf')
                        node.successors[str(i-1)+str(j)] = float('inf')
                    else :  
                        node.predecessors[str(i-1)+str(j)] = 1
                        node.successors[str(i-1)+str(j)] = 1

                if (j > 0):
                    
                    if (grid[i][j-1] == 1):
                        node.predecessors[str(i)+str(j-1)] = float('inf')
                        node.successors[str(i)+str(j-1)] = float('inf')
                    else :  
                        node.predecessors[str(i)+str(j-1)] = 1
                        node.successors[str(i)+str(j-1)] = 1

                if (i+1< rows):
                    
                    if (grid[i+1][j] == 1):
                        node.predecessors[str(i+1)+str(j)] = float('inf')
                        node.successors[str(i+1)+str(j)] = float('inf')
                    else :  
                        node.predecessors[str(i+1)+str(j)] = 1
                        node.successors[str(i+1)+str(j)] = 1

                if (j+1< columns):
                    
                    if (grid[i][j+1] == 1):
                        node.predecessors[str(i)+str(j+1)] = float('inf')
                        node.successors[str(i)+str(j+1)] = float('inf')
                    else :  
                        node.predecessors[str(i)+str(j+1)] = 1
                        node.successors[str(i)+str(j+1)] = 1

            Graph.graph[str(i)+str(j)] = node
    return Graph



# B = CreateGraph(3, 3)
# C = B.graph["00"].children.keys()
# D = B.graph["00"].parents.keys()
# # print (C)
# # print (D)
# B.setGoal("22")
# B.graph["22"].g = 0

# min_rhs = float('inf')

# print(B.graph["21"].children)
# for i in B.graph["21"].children:#node eke succesorslagen rhs value eka update karagannaw.#keys tiken yann wei maybe
#     # print(B.graph["21"].children[i])
#     # print(B.graph[i].g + B.graph["21"].children[i])
#     # print(min(min_rhs,B.graph[i].g + B.graph["21"].children[i]))
#             # print(i)
#     # print(B.graph[i].g)
#     min_rhs = min(min_rhs,B.graph[i].g + B.graph["21"].children[i]) #last part is the edge cost
#     # print(min_rhs)
            
#     # B.graph["21"].set_rhs(min_rhs)  
#     # rhs = B.graph["21"].get_rhs()
#     # print(rhs)
#     # print (B.graph["21"].g)

#     B.graph["21"].rhs =  min_rhs

# print (B.graph["21"].rhs)


    