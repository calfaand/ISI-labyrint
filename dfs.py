from collections import deque
from main import maps


class GridPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, pos: GridPosition, cost):  # cost aka counter
        self.pos = pos
        self.cost = cost


def create_node(x, y, c):
    val = GridPosition(x, y)
    return Node(val, c + 1)


def dfs(Grid, dest: GridPosition, start: GridPosition):
    adj_cell_x = [1, 0, 0, -1]
    adj_cell_y = [0, 1, -1, 0]
    row, col = (len(maps), len(maps[0]))
    visited_blocks = [[False for i in range(row)]  # nastavi vsetko na nenavstivene
                      for j in range(col)]
    visited_blocks[start.x][start.y] = True
    stack = deque()
    sol = Node(start, 0)
    stack.append(sol)
    neigh = 4
    neighbors = []
    cost = 0
    while stack:
        curr_block = stack.pop()
        curr_pos = curr_block.pos
        if (curr_pos.x == dest.x and curr_pos.y == dest.y):  # nastavit asi jak global v main ze maps dest.x a dest.y
            print("Algorithm used = DFS")
            print("Path found!!")
            print("Total nodes visited = ", cost)
            return curr_block.cost
        x_pos = curr_pos.x
        y_pos = curr_pos.y

        for i in range(neigh):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = curr_pos.x
                y_pos = curr_pos.y
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = curr_pos.x + adj_cell_x[i]
                y_pos = curr_pos.y
            else:
                x_pos = curr_pos.x + adj_cell_x[i]
                y_pos = curr_pos.y + adj_cell_y[i]
                if x_pos != len(maps) and x_pos !=-1 and y_pos != len(maps[0]) and y_pos != -1:
                    if Grid[x_pos][y_pos]==1:       #TODO: mozno treba dat tu 0 ..... 1 v GH ako volno, tuto 1 ako stena
                        if not visited_blocks[x_pos][y_pos]:
                            cost+=1
                            visited_blocks[x_pos][y_pos] = True
                            stack.append(create_node(x_pos,y_pos, curr_block.cost ))
    return -1