class Node:

    def __init__(self, node_id):
        self.id = node_id
        self.predecessors = {} #Parent id with edge cost
        self.successors ={}
        self.g = float('inf')
        self.rhs = float('inf')
    
    def get_g(self):
        return self.g
    
    def get_rhs(self):
        return self.rhs

    def get_node_id(self):
        return self.id
    
    def update_predecessors(self, new_predecessor):
        self.predecessors = new_predecessor
    
    def update_successors(self, new_successors):
        self.successors = new_successors

    def set_g(self, g_value):
        self.g = g_value 

    def set_rhs(self, rhs_value):
        self.rhs = rhs_value


# A = "X0Y12"
# print (A.split("Y")[1])