import pygame
from node import Node
from graph import graph, CreateGraph
from d_star_lite_algo import initialize, GetTopKey, heuristic_from_s, CalculateKey, ComputeShortestPath, UpdateVertex, NextNodeInShortestPath, MoveToNextNode
import heapq

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)


#width and height of a cell
width = 40
height = 40
margin = 1

#num of cells in a row and colum
y_length = 9  #same as y_length
x_length = 9

pygame.init()
text_font = pygame.font.SysFont('Comic Sans MS', 36)

# Set the width and height of the screen [width, height]
size = ((width + margin) * x_length + margin, (height + margin) * y_length + margin)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

grid = [[0 for x in range(x_length)] for y in range(y_length)]  #x kiyanne row ekak dige, y kiyanne column ekak dige
# print (grid)
# grid[8][8] = 1

# Loop until the user clicks the close button.
done = False
place_obstacles_done = False
initialize_grid = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



rows = y_length
columns = x_length
queue = []
k_m = 0
GRAPH = {}  #hadenakotama okkoma g = inf and rhs = inf wenawa
start = "00"
goal = "43"
start_current_node =""




# -------- Main Program Loop -----------
while not done:

    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    # y = pos[0]   #making as matrix notation
    # x = pos[1]

    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        elif pygame.mouse.get_pressed()[0]:
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # Debug prints
            print("Click ", pos, "Grid coordinates: ", row, column)
            grid[row][column] = 1

        elif pygame.mouse.get_pressed()[2]:
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # Debug prints
            print("Click ", pos, "Grid coordinates: ", row, column)
            grid[row][column] = 0
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # print('space bar! call next action')
            # print ("Hey")
            place_obstacles_done = True
            if (initialize_grid):
                new_start_node = MoveToNextNode(GRAPH, start_current_node)
                if new_start_node == "goal":
                    print('Goal Reached!')
                    done = True
                else:
                    # print('setting start_current_node to ', new_start_node)
                    start_current_node = new_start_node

    screen.fill(BLACK)

    if (not place_obstacles_done):
        
        for row in range(y_length):  #3
            for column in range(x_length):  #4
                if grid[row][column] == 1:
                    color = BLACK
                else:
                    color = WHITE
                #pygame.draw.rect function gets x coordinate as its 3rd argument, then y coordinate
                pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
        # print (grid)
			
    else:
        # --- Drawing code should go here

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        if (not initialize_grid):
            # print (grid)
            # print(grid[1][3])
            GRAPH = CreateGraph(grid,y_length, x_length)
            corrected_goal = goal[1]+goal[0]
            corrected_start = start[1]+start[0]
            GRAPH.setGoal(corrected_goal)
            GRAPH.setStart(corrected_start)
            GRAPH.graph[corrected_goal].rhs = 0
            GRAPH.getGoal()
    
            heapq.heappush(queue, list(CalculateKey(GRAPH, corrected_goal, corrected_start, k_m))+[corrected_goal])
            # g,q,s,go,k_m = initialize(x_length, y_length, start, goal)
            ComputeShortestPath(GRAPH,queue,corrected_start,k_m)
            # print ("done")

            start_current_node = corrected_start
# print (g, q, )
            # print(GRAPH)
            initialize_grid = True

    

        for row in range(y_length):
            for column in range(x_length):
                if grid[row][column] == 1:
                    color = BLACK
                else:
                    color = WHITE
                # else:
                #     color = WHITE
                pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
                node_id = str(row) + str(column)
        
                if (GRAPH.graph[node_id].g != float('inf')):
                    text = text_font.render(str(GRAPH.graph[node_id].g), True, (0, 0, 200))
                    textrect = text.get_rect()
                    textrect.centerx = int(column * (width + margin) + width / 2) + margin
                    textrect.centery = int(row * (height + margin) + height / 2) + margin
                    screen.blit(text, textrect)

        

        pygame.draw.rect(screen, GREEN, [(margin + width) * int(corrected_goal[1]) + margin,
                                            (margin + height) * int(corrected_goal[0]) + margin, width, height])
            # print('drawing robot pos_coords: ', pos_coords)
            # draw moving robot, based on pos_coords  for now we have used starting node but later we need to replace this with the current robot position
        robot_center = [int(int(start_current_node[1]) * (width + margin) + width / 2) +
                            margin, int(int(start_current_node[0]) * (height + margin) + height / 2) + margin]
        pygame.draw.circle(screen, RED, robot_center, int(width / 2) - 2)

	
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()