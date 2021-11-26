from collections import deque
import main


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
    row, col = (len(Grid), len(Grid[0]))
    visited_blocks = [[False for i in range(col)]  # nastavi vsetko na nenavstivene
                      for j in range(row)]
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
                if x_pos != len(Grid) and x_pos != -1 and y_pos != len(Grid[0]) and y_pos != -1:
                    if Grid[x_pos][y_pos] == '0' or Grid[x_pos][y_pos] == '3':
                        if not visited_blocks[x_pos][y_pos]:
                            cost += 1
                            visited_blocks[x_pos][y_pos] = True
                            stack.append(create_node(x_pos, y_pos, curr_block.cost))
    return -1


def bfs(Grid, dest: GridPosition, start: GridPosition):
    adj_cell_x = [1, 0, 0, -1]  # sused po x
    adj_cell_y = [0, 1, -1, 0]  # sused po y
    row, col = (len(Grid), len(Grid[0]))
    visited_blocks = [[False for i in range(col)]  # nastavi vsetko na nenavstivene
                      for j in range(row)]
    visited_blocks[start.x][start.y] = True
    queue = deque()
    sol = Node(start, 0)
    queue.append(sol)
    cells = 4  # jak neig v dfs
    cost = 0
    while queue:
        curr_block = queue.popleft() #deq front cell
        curr_pos = curr_block.pos
        if curr_pos.x == dest.x and curr_pos.y == dest.y:
            print("Algorithm used = BFS")
            print("Path found!!")
            print("Total nodes visited = ", cost)
            return curr_block.cost

        if curr_block not in visited_blocks:
            visited_blocks[curr_pos.x][curr_pos.y] = True
            cost = cost + 1
        x_pos = curr_pos.x
        y_pos = curr_pos.y
        for i in range(cells):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = curr_pos.x
                y_pos = curr_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = curr_pos.x + adj_cell_x[i]
                y_pos = curr_pos.y
            else:
                x_pos = curr_pos.x + adj_cell_x[i]
                y_pos = curr_pos.y + adj_cell_y[i]
            if x_pos < len(Grid) and y_pos < len(Grid[0]) and x_pos >= 0 and y_pos >= 0:
                if Grid[x_pos][y_pos] == '0' or Grid[x_pos][y_pos] == '3':
                    if not visited_blocks[x_pos][y_pos]:
                        next_cell = Node(GridPosition(x_pos, y_pos),
                                         curr_block.cost + 1)
                        visited_blocks[x_pos][y_pos] = True
                        queue.append(next_cell)
    return -1