from node import Node
from graph import graph, CreateGraph
import heapq
import pygame
import math
import sys


# rows = 3
# columns =3
# B = CreateGraph(rows, columns)
# C = B.graph["00"].children.keys()
# print (C)
# B.setStart("00");
# B.setGoal("22")
# B.getGoal()


#order to run the algorithm
#Give rows and colmns and make the graph first
#Set a goal and a starting point
#write a code for initialize procedure..in there we will make rhs value of the goal node to zero
#and finally it should be put into the heap(priority queue)
#Then the algorithm will call f0r computer shortest path algorithm

def heuristic_from_s(node_id, start_current_node_id):  #considering diagonal distance
    x_distance = abs(int(node_id[0]) - int(start_current_node_id[0]))
    y_distance = abs(int(node_id[1]) - int(start_current_node_id[1]))
    eucledian_distance = math.sqrt(x_distance**2 + y_distance**2)
    return eucledian_distance

def CalculateKey(graph, node_id, start_current_node_id, k_m):
    list = [round(min(graph.graph[node_id].g,graph.graph[node_id].rhs) + heuristic_from_s(node_id,start_current_node_id),1)+ k_m, min(graph.graph[node_id].g, graph.graph[node_id].rhs)]
    return (list)

def GetTopKey(queue):
    queue.sort()
    if len(queue) > 0:
        list = []
        list.append(queue[0][0])
        list.append(queue[0][1])
        return list  #only getting the key pair, not with the node id
    else:
        # print('empty queue!')
        list = [float('inf'), float('inf')]
        return (list)


def UpdateVertex(graph, queue, node_id, start_current_node_id, k_m ): #RHS valuse of predecessors will be updates here
    goal_id = graph.goal
    # start_id = graph.getStart()

    if (node_id != goal_id): #updating rhs values of neighbours
        min_rhs = float('inf')
        # print(node_id)
        # print(graph.graph[node_id].children)
        for i in graph.graph[node_id].successors:#node eke succesorslagen rhs value eka update karagannaw.#keys tiken yann wei maybe
            # print(graph.graph[i].g)
            min_rhs = min(min_rhs,graph.graph[i].g + graph.graph[node_id].successors[i]) #last part is the edge cost
            # print(min_rhs)
            
        graph.graph[node_id].rhs = round(min_rhs,1)
        

    #rhs value update karala balanna one inconsistent nathi a wa tiyenwada kiyala..inconsistent nattn queuen eken ain karanna one 
    if graph.graph[node_id].rhs == graph.graph[node_id].g:
        nodes_in_queue = []
        #print ("I'm here")
        for key in queue:
            if node_id in key:
                nodes_in_queue.append(key)
        #check whether th key is present in the queue
        if len(nodes_in_queue) != 0:
            queue.remove(nodes_in_queue[0])  #adala key value eka ain karanawa priprity queue eken

    #checking if the current node is inconsistent, is so put it to the priority queue, with the node id
    if graph.graph[node_id].rhs != graph.graph[node_id].g:
        heapq.heappush(queue, list(CalculateKey(graph, node_id, start_current_node_id, k_m))+[node_id])  






def ComputeShortestPath(graph, queue, start_node_id, k_m): #input ekak widihata start node eka dunnata wade wenne priority list eke piliwelata..a ka nisa patan ganne goal eken. bu h values calculate wenne start eke idan mokada dan api yanne goal to start nisa
    
    while ((graph.graph[start_node_id].rhs != graph.graph[start_node_id].g) or (GetTopKey(queue) < CalculateKey(graph, start_node_id, start_node_id, k_m))):#patan gannkota start node eke ke value eka tiyenne <inf, inf>.. a ka greater than goal eke <key pair > ekata wada.. so loop eka athulata ynwa. SO meka ewara wenna nma aniwa strt node eke g=rhs wennath one, start node eke key pair eka prioriry list eke top value ekata adu wennath one..so simply shortest path kiyana eka
        k_old = GetTopKey(queue) #key value currently on top of the prority queue
        # print(k_old)
        priority_queue_top_value = heapq.heappop(queue)
        u = priority_queue_top_value[2]  #id of the node in the top of priority queue
        k_new = CalculateKey(graph, u, start_node_id, k_m )

        if (k_old < k_new):
            heapq.heappush(queue, list(k_new)+[u])

        if (graph.graph[u].g > graph.graph[u].rhs):#Overconsistent
            graph.graph[u].g = graph.graph[u].rhs
            
            for i in graph.graph[u].predecessors:  #since we are coming back from goal to start
                # print (graph.graph[u].parents)
                UpdateVertex(graph, queue, i, start_node_id, k_m)
                

        elif (graph.graph[u].g < graph.graph[u].rhs):#Underconsistent
            graph.graph[u].g = float('inf')
            for i in graph.graph[u].predecessors:
                UpdateVertex(graph, queue, u, start_node_id, k_m)
   

    # print (graph.graph["22"].rhs)



def initialize(rows, columns,start, goal):
    rows = rows
    columns = columns
    queue = []
    k_m = 0
    GRAPH = CreateGraph(rows, columns)  #hadenakotama okkoma g = inf and rhs = inf wenawa
    goal = goal
    start = start
    GRAPH.setGoal(goal)
    GRAPH.setStart(start)
    GRAPH.graph[goal].rhs = 0
    
    heapq.heappush(queue, list(CalculateKey(GRAPH, goal, start, k_m))+[goal])

    # test = CalculateKey(GRAPH, goal, start, k_m)
    # print (test)

    # queue = [[1,2,"12"],[1,0,"24"]]
    # # y = GetTopKey(queue)
    # # print (y)       
    # count = 0
    # while (GetTopKey(queue) < CalculateKey(GRAPH, goal, start, k_m)):
    #     count += 1
    #     print ("hey")
    #     if (count > 10):
    #         break
    
    return (GRAPH, queue, start, goal, k_m)

def NextNodeInShortestPath(graph, start_current_node_id):
    min_rhs = float('inf')
    s_next = None

    for i in graph.graph[start_current_node_id].successors:
        # print(i)
        cost_to_current_node = graph.graph[i].g + graph.graph[start_current_node_id].successors[i]
        # print(cost_to_current_node)

        #finding who gives the lowest g cost to the current  node
        if (cost_to_current_node) < min_rhs:
            min_rhs = cost_to_current_node
            s_next = i
    if s_next:
        return s_next
    else:
        print ("cannot find a way")
        sys.exit()


def MoveToNextNode(graph, start_current_node_id):
    if (start_current_node_id == graph.goal):
        return ("goal")
    else :
        previous_start_node_id = start_current_node_id
        next_start_node_id = NextNodeInShortestPath(graph, start_current_node_id)
        # k_m += heuristic_from_s(previous_start_node_id, next_start_node_id)

    # print(next_start_node_id)
    return next_start_node_id
    




# g,q,s,go,k_m = initialize()
# ComputeShortestPath(g,q,s,k_m)
# # print (g, q, )
# print(g)

#sorting and heapq check

# queue_1 = [[1,2, "11"],[0,4,"12"],[1,3,"13"],[1,1, "14"]]
# # heapq.heapify(queue_1)
# # heapq.heappush(queue_1,[0,1])


# # u = heapq.heappop(queue_1)
# # print (u)

# queue_1.sort()
# print(queue_1[0])



# f,G = CalculateKey(B,"22", "00", 0)
# print(f)
# print(G)

