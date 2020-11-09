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
            node = Node("X"+str(j)+"Y"+str(i)) #node eka X3Y2 nam grid eke 3,2 wenna one
            if (grid[i][j] == 1): #setting edge costs to infinity if the cell is an obstacle, but we can remove this node directly from the graph, to do that remove Node(str(i)+str(j))
                # continue
                if (i > 0):
                    node.predecessors["X"+str(j)+"Y"+str(i-1)] = float('inf')
                    node.successors["X"+str(j)+"Y"+str(i-1)] = float('inf')

                    if (j+1< columns):
                        node.predecessors["X"+str(j+1)+"Y"+str(i-1)] = float('inf')
                        node.successors["X"+str(j+1)+"Y"+str(i-1)] = float('inf')
                    
                    if (j > 0):
                        node.predecessors["X"+str(j-1)+"Y"+str(i-1)] = float('inf')
                        node.successors["X"+str(j-1)+"Y"+str(i-1)] = float('inf')
                    

                if (j > 0):
                    node.predecessors["X"+str(j-1)+"Y"+str(i)] = float('inf')
                    node.successors["X"+str(j-1)+"Y"+str(i)] = float('inf')

                    if (i > 0):
                        node.predecessors["X"+str(j-1)+"Y"+str(i-1)] = float('inf')
                        node.successors["X"+str(j-1)+"Y"+str(i-1)] = float('inf')

                    if (i+1< rows):
                        node.predecessors["X"+str(j-1)+"Y"+str(i+1)] = float('inf')
                        node.successors["X"+str(j-1)+"Y"+str(i+1)] = float('inf')
               

                if (i+1< rows):
                    node.predecessors["X"+str(j)+"Y"+str(i+1)] = float('inf')
                    node.successors["X"+str(j)+"Y"+str(i+1)] = float('inf')

                    if (j > 0):
                        node.predecessors["X"+str(j-1)+"Y"+str(i+1)] = float('inf')
                        node.successors["X"+str(j-1)+"Y"+str(i+1)] = float('inf')
              
                    if (j+1< columns):
             
                        node.predecessors["X"+str(j+1)+"Y"+str(i+1)] = float('inf')
                        node.successors["X"+str(j+1)+"Y"+str(i+1)] = float('inf')

                if (j+1< columns):
                    node.predecessors["X"+str(j+1)+"Y"+str(i)] = float('inf')
                    node.successors["X"+str(j+1)+"Y"+str(i)] = float('inf')

                    if (i > 0): 
                        node.predecessors["X"+str(j+1)+"Y"+str(i)] = float('inf')
                        node.successors["X"+str(j+1)+"Y"+str(i)] = float('inf')
                      
                    if (i+1< rows):  
                        node.predecessors["X"+str(j+1)+"Y"+str(i+1)] = float('inf')
                        node.successors["X"+str(j+1)+"Y"+str(i+1)] = float('inf')
               
                    

            else:
                if (i > 0):
                   
                    if (grid[i-1][j] == 1):  #setting edge costs to infinity if the neighbour cell is an obstacle
                        node.predecessors["X"+str(j)+"Y"+str(i-1)] = float('inf')
                        node.successors["X"+str(j)+"Y"+str(i-1)] = float('inf')
                    else :  
                        node.predecessors["X"+str(j)+"Y"+str(i-1)] = 1
                        node.successors["X"+str(j)+"Y"+str(i-1)] = 1

                    if (j+1< columns):
                        if (grid[i-1][j+1] == 1):
                            node.predecessors["X"+str(j+1)+"Y"+str(i-1)] = float('inf')
                            node.successors["X"+str(j+1)+"Y"+str(i-1)] = float('inf')
                        else:
                            node.predecessors["X"+str(j+1)+"Y"+str(i-1)] = 1.4
                            node.successors["X"+str(j+1)+"Y"+str(i-1)] = 1.4
                    
                    if (j > 0):
                        if (grid[i-1][j-1] == 1):
                            node.predecessors["X"+str(j-1)+"Y"+str(i-1)] = float('inf')
                            node.successors["X"+str(j-1)+"Y"+str(i-1)] = float('inf')
                        else:
                            node.predecessors["X"+str(j-1)+"Y"+str(i-1)] = 1.4
                            node.successors["X"+str(j-1)+"Y"+str(i-1)] = 1.4



                if (j > 0):
                    
                    if (grid[i][j-1] == 1):
                        node.predecessors["X"+str(j-1)+"Y"+str(i)] = float('inf')
                        node.successors["X"+str(j-1)+"Y"+str(i)] = float('inf')
                    else :  
                        node.predecessors["X"+str(j-1)+"Y"+str(i)] = 1
                        node.successors["X"+str(j-1)+"Y"+str(i)] = 1
                    
                    if (i > 0):
                        if (grid[i-1][j-1] == 1): 
                            node.predecessors["X"+str(j-1)+"Y"+str(i-1)] = float('inf')
                            node.successors["X"+str(j-1)+"Y"+str(i-1)] = float('inf')
                        else:
                            node.predecessors["X"+str(j-1)+"Y"+str(i-1)] = 1.4
                            node.successors["X"+str(j-1)+"Y"+str(i-1)] = 1.4

                    if (i+1< rows):
                        if (grid[i+1][j-1] == 1): 
                            node.predecessors["X"+str(j-1)+"Y"+str(i+1)] = float('inf')
                            node.successors["X"+str(j-1)+"Y"+str(i+1)] = float('inf')
                        else:
                            node.predecessors["X"+str(j-1)+"Y"+str(i+1)] = 1.4
                            node.successors["X"+str(j-1)+"Y"+str(i+1)] = 1.4


                if (i+1< rows):
                    
                    if (grid[i+1][j] == 1):
                        node.predecessors["X"+str(j)+"Y"+str(i+1)] = float('inf')
                        node.successors["X"+str(j)+"Y"+str(i+1)] = float('inf')
                    else :  
                        node.predecessors["X"+str(j)+"Y"+str(i+1)] = 1
                        node.successors["X"+str(j)+"Y"+str(i+1)] = 1

                    if (j > 0):
                        if (grid[i+1][j-1] == 1):
                            node.predecessors["X"+str(j-1)+"Y"+str(i+1)] = float('inf')
                            node.successors["X"+str(j-1)+"Y"+str(i+1)] = float('inf')
                        else :  
                            node.predecessors["X"+str(j-1)+"Y"+str(i+1)] = 1.4
                            node.successors["X"+str(j-1)+"Y"+str(i+1)] = 1.4
                    
                    if (j+1< columns):
                        if (grid[i+1][j+1] == 1):
                            node.predecessors["X"+str(j+1)+"Y"+str(i+1)] = float('inf')
                            node.successors["X"+str(j+1)+"Y"+str(i+1)] = float('inf')
                        else :  
                            node.predecessors["X"+str(j+1)+"Y"+str(i+1)] = 1.4
                            node.successors["X"+str(j+1)+"Y"+str(i+1)] = 1.4

                if (j+1< columns):
                    
                    if (grid[i][j+1] == 1):
                        node.predecessors["X"+str(j+1)+"Y"+str(i)] = float('inf')
                        node.successors["X"+str(j+1)+"Y"+str(i)] = float('inf')
                    else :  
                        node.predecessors["X"+str(j+1)+"Y"+str(i)] = 1
                        node.successors["X"+str(j+1)+"Y"+str(i)] = 1

                    if (i > 0):
                        if (grid[i-1][j+1] == 1):
                            node.predecessors["X"+str(j+1)+"Y"+str(i-1)] = float('inf')
                            node.successors["X"+str(j+1)+"Y"+str(i-1)] = float('inf')
                        else :  
                            node.predecessors["X"+str(j+1)+"Y"+str(i-1)] = 1.4
                            node.successors["X"+str(j+1)+"Y"+str(i-1)] = 1.4
                    
                    if (i+1< rows):
                        if (grid[i+1][j+1] == 1):
                            node.predecessors["X"+str(j+1)+"Y"+str(i+1)] = float('inf')
                            node.successors["X"+str(j+1)+"Y"+str(i+1)] = float('inf')
                        else :  
                            node.predecessors["X"+str(j+1)+"Y"+str(i+1)] = 1.4
                            node.successors["X"+str(j+1)+"Y"+str(i+1)] = 1.4

            Graph.graph["X"+str(j)+"Y"+str(i)] = node
    # print (Graph)
    return Graph



def getcoordinates(value):
    return [int(value.split('X')[1].split('Y')[0]), int(value.split('Y')[1])]

# x = "12"
# print (list(x))


    