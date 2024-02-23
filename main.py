
import random

startNode=0
goalNode=0
barriers=[]
#function to create random maze
def maze():
    maze = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23],
             [24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35]]

#assigning a list for barriers
    barriers= []
#assigning barriers to the list
    while len(barriers)<4:
        b1= random.randint(0,35)
        if b1 not in barriers:
            barriers.append(b1)
    def s0_check(barriersList):
        if(1 in barriersList and 6 in barriersList and 7 in barriersList):
            return True
    def s5_check(barriersList):
        if (4 in barriersList and 10 in barriersList and 11 in barriersList):
            return True
    def g30_check(barriersList):
        if(24 in barriersList and 25 in barriersList and 31 in barriersList):
            return True
    def g35_check(barriersList):
        if(28 in barriersList and 29 in barriersList and 34 in barriersList):
            return True


#generating a start node for the maze
    while True:
        s= random.randint(0,11)
        if(s==0 and s0_check(barriers)):
            print("check point detected!!!")
            continue
        elif(s==5 and s5_check(barriers)):
            print("check point detected!!!")
            continue
        else:
            startNode=s
            break

    # generating a goal node for the maze
    while True:
        g= random.randint(24,35)
        if(g==30 and g30_check(barriers)):
            print("check point detected!!!")
            continue
        elif(g==35 and g35_check(barriers)):
            print("check point detected!!!")
            continue
        else:
            goalNode=g
            break

    barNum=0
#a fake maze for displaying purpose
    fakeMaze= [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            for k in range(len(barriers)):
                if barriers[k]==maze[i][j]:
                    barNum+=1
                    fakeMaze[i][j]='B'
            if maze[i][j]==startNode:
                fakeMaze[i][j]='S'
            if maze[i][j] == goalNode:
                fakeMaze[i][j]='G'

#displaying the maze with goal, start and barriers
    for i in range(0,6):
        print(fakeMaze[0][i], fakeMaze[1][i],fakeMaze[2][i],fakeMaze[3][i],fakeMaze[4][i],fakeMaze[5][i])

    print()
# final return statement with random maze
    return maze,startNode,goalNode,barriers

#functions to get cordinates (X and Y)
def getXcord(node,maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if node== maze[x][y]:
                return x
    else:
        print("no value!!!")
        return -1
def getYcord(node,maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if node== maze[x][y]:
                return y
    else:
        print("no value!!!")
        return -1


#Function to do Depth first search fo the passing maze
def DFS(maze, startNode, goalNode, barriers):
    visited_Node_List = []
    visitedPath = []
    stack = [startNode]
    print(stack)
    currNode=startNode
    time=1

    while stack and currNode!=goalNode:
        currNode = stack[-1]
        stack.pop()
        visitedPath.append(currNode)
        x = getXcord(currNode, maze)
        y = getYcord(currNode, maze)

        if currNode == goalNode:
            print("GOAL reached")
            break

        # Process neighbors in increasing order
        #considererd diagoanl processing also
        #at the end of each process time will be added
        if x == 0:
            if y == 0:
                addToStack(currNode + 1, stack, visitedPath, barriers)
                addToStack(currNode+6 ,stack ,visitedPath, barriers)
                addToStack(currNode + 7, stack, visitedPath, barriers)
                time+=3
            elif y == 5:
                addToStack(currNode - 1, stack, visitedPath, barriers)
                addToStack(currNode +5, stack, visitedPath, barriers)
                addToStack(currNode +6, stack, visitedPath, barriers)
                time+=3
            else:
                addToStack(currNode - 1, stack, visitedPath, barriers)
                addToStack(currNode + 1, stack, visitedPath, barriers)
                addToStack(currNode +5, stack, visitedPath, barriers)
                addToStack(currNode + 6, stack, visitedPath, barriers)
                addToStack(currNode + 7, stack, visitedPath, barriers)
                time +=5
        elif x == 5:

            if y == 0:
                addToStack(currNode -6, stack, visitedPath, barriers)
                addToStack(currNode-5 ,stack ,visitedPath, barriers)
                addToStack(currNode + 1, stack, visitedPath, barriers)
                time +=3
            elif y == 5:
                addToStack(currNode - 7, stack, visitedPath, barriers)
                addToStack(currNode -6, stack, visitedPath, barriers)
                addToStack(currNode -1, stack, visitedPath, barriers)
                time +=3
            else:
                addToStack(currNode - 7, stack, visitedPath, barriers)
                addToStack(currNode -6, stack, visitedPath, barriers)
                addToStack(currNode -5, stack, visitedPath, barriers)
                addToStack(currNode -1, stack, visitedPath, barriers)
                addToStack(currNode +1, stack, visitedPath, barriers)
                time +=5
        else:

            if y == 0:
                addToStack(currNode -6, stack, visitedPath, barriers)
                addToStack(currNode-5 ,stack ,visitedPath, barriers)
                addToStack(currNode + 1, stack, visitedPath, barriers)
                addToStack(currNode +6, stack, visitedPath, barriers)
                addToStack(currNode + 7, stack, visitedPath, barriers)
                time +=5
            elif y == 5:
                addToStack(currNode - 7, stack, visitedPath, barriers)
                addToStack(currNode -6, stack, visitedPath, barriers)
                addToStack(currNode -1, stack, visitedPath, barriers)
                addToStack(currNode + 5, stack, visitedPath, barriers)
                addToStack(currNode + 6, stack, visitedPath, barriers)
                time +=5
            else:
                addToStack(currNode - 7, stack, visitedPath, barriers)
                addToStack(currNode -6, stack, visitedPath, barriers)
                addToStack(currNode -5, stack, visitedPath, barriers)
                addToStack(currNode -1, stack, visitedPath, barriers)
                addToStack(currNode +1, stack, visitedPath, barriers)
                addToStack(currNode + 5, stack, visitedPath, barriers)
                addToStack(currNode + 6, stack, visitedPath, barriers)
                addToStack(currNode + 7, stack, visitedPath, barriers)
                time +=8


    print("time comlexity : ", time, " Mins")

    return visitedPath  # Return the visited nodes list

#addin a node to the stack
def addToStack(node, stack, visitedList, barriers):
    if node not in stack and node not in visitedList and node not in barriers:
        stack.append(node)

#Calculating Heuristic = Manhattan Value (assumed cost as 0)
def manhattanD(maze,currNode, goalNode):
    currX=getXcord(currNode,maze)
    currY = getYcord(currNode, maze)

    goalX = getXcord(goalNode,maze)
    goalY =getYcord(goalNode,maze)

    manD = abs(currX- goalX) + abs(currY - goalY)
    return manD

#Function for A* Search
def Astar(maze,startNode, goalNode, barriers):

    currentNode = startNode
    visited_list=[startNode]
    low_hue_node = startNode

# checking weather the goal is catched
    while  currentNode!=goalNode:
        low_hue= manhattanD(maze, currentNode, goalNode)
        x = getXcord(currentNode, maze)
        y = getYcord(currentNode, maze)

#processing evvery node and catch the node with lowest Hueristic Value
        if x==0:
            if y==0:
                low_hue_node = hue_check(currentNode + 1, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 7, low_hue_node, visited_list, barriers, maze, goalNode)

            elif y == 5:
                low_hue_node = hue_check(currentNode - 1, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 5, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 6, low_hue_node, visited_list, barriers, maze, goalNode)


            else:
                low_hue_node = hue_check(currentNode - 1, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 1, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 5, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 7, low_hue_node, visited_list, barriers, maze, goalNode)


        elif x==5:
            if y == 0:
                low_hue_node = hue_check(currentNode - 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 5, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 1, low_hue_node, visited_list, barriers, maze, goalNode)



            elif y == 5:
                low_hue_node = hue_check(currentNode - 7, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 1, low_hue_node, visited_list, barriers, maze, goalNode)



            else:
                low_hue_node = hue_check(currentNode - 7, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 5, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 1, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 1, low_hue_node, visited_list, barriers, maze, goalNode)



        else:
            if y == 0:
                low_hue_node = hue_check(currentNode - 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 5, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 1, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 7, low_hue_node, visited_list, barriers, maze, goalNode)

            elif y == 5:
                low_hue_node = hue_check(currentNode - 7, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 1, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 5, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 6, low_hue_node, visited_list, barriers, maze, goalNode)

            else:
                low_hue_node = hue_check(currentNode - 7, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 5, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode - 1, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 1, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 5, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 6, low_hue_node, visited_list, barriers, maze, goalNode)
                low_hue_node = hue_check(currentNode + 7, low_hue_node, visited_list, barriers, maze, goalNode)

#appending the node with lowest  Heuristi value to the Visited list
        visited_list.append(low_hue_node)
        currentNode=low_hue_node

#calculating time as per lowest hueristic node
    time2 = 1 * (len(visited_list)-1)
    print("time comlexity : ", time2, " Mins")

    return visited_list
    print(visited_list)


# Function to check th eHeuristi value
def hue_check(node,low_hue_node, visited_list, barriers,maze,goal_node):
    if node not in visited_list and node not in barriers:
        current_node_hue= manhattanD(maze,node,goal_node)
        low_hue =manhattanD(maze,low_hue_node,goalNode)
        if current_node_hue<low_hue:
            low_hue=current_node_hue
            return node

        else:
            return low_hue_node
    else:
        return low_hue_node




# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    returnList = maze()
    maze1 = returnList[0]

    startNode=returnList[1]
    goalNode= returnList[2]
    barriers = returnList[3]

    for i in range(6):
        print(maze1[i])

    print("Start Node is : ",startNode)
    print("Goal Node is : ", goalNode)
    print("Barriers is : ", barriers)
    print("DFS Search >>>")

    vlDFS=DFS(maze1,startNode,goalNode,barriers)
    print("Visited path ----")
    for i in range(len(vlDFS)):
        print(vlDFS[i] ,end="  ")
    print()
    print()
    print("A STAR SEARCH>>>>>")
    print("Visited path ----")
    vlAstar = Astar(maze1,startNode,goalNode,barriers)

    for i in range(len(vlAstar)):
        print(vlAstar[i] ,end="  ")
    Astar(maze1,startNode,goalNode,barriers)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
