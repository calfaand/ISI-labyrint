from collections import deque
import queue
import main
import pygame

pygame.init()
MARGIN = 24
WHITE = (255, 255, 255)


WIDTH, HEIGHT = 500, 500
X = pygame.image.load('assets/x.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WALL = pygame.image.load('assets/wall.png')
MARIO = pygame.image.load('assets/mario.png')



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
    screen.fill(WHITE)
    pygame.display.flip()
    for row in range(len(Grid)):  # ze pocet rows
        for col in range(len(Grid[0])):  # pocet cols
            if Grid[row][col] == '2':
                screen.blit(MARIO, (col * MARGIN, row * MARGIN))

                continue
            if Grid[row][col] == '0' or Grid[row][col] == '3':
                continue

            screen.blit(WALL, (col * MARGIN, row * MARGIN))

    pygame.display.flip()
    adj_cell_x = [1, 0, 0, -1] #hore, dole
    adj_cell_y = [0, 1, -1, 0] # vpravo, vlavo
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
                x_pos = curr_pos.y
                y_pos = curr_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = curr_pos.x + adj_cell_x[i]
                y_pos = curr_pos.y
            else:
                x_pos = curr_pos.x + adj_cell_x[i]
                y_pos = curr_pos.y + adj_cell_y[i]
                if x_pos != len(Grid) and y_pos != -1 and x_pos != len(Grid[0]) and y_pos != -1:
                    if Grid[x_pos][y_pos] == '0' or Grid[x_pos][y_pos] == '3':
                        if not visited_blocks[x_pos][y_pos]:
                            cost += 1
                            visited_blocks[x_pos][y_pos] = True
                            screen.blit(X, (y_pos * MARGIN, x_pos * MARGIN))
                            pygame.time.delay(200)
                            print(x_pos, ' ', y_pos)
                            pygame.display.update()
                            stack.append(create_node(x_pos, y_pos, curr_block.cost))
    return -1


def bfs(Grid, dest: GridPosition, start: GridPosition):
    screen.fill(WHITE)
    pygame.display.flip()
    for row in range(len(Grid)):  # ze pocet rows
        for col in range(len(Grid[0])):  # pocet cols
            if Grid[row][col] == '2':
                screen.blit(MARIO, (col * MARGIN, row * MARGIN))

                continue
            if Grid[row][col] == '0' or Grid[row][col] == '3':
                continue

            screen.blit(WALL, (col * MARGIN, row * MARGIN))

    pygame.display.flip()
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
                        screen.blit(X, (y_pos * MARGIN, x_pos * MARGIN))
                        pygame.time.delay(200)
                        print(x_pos, ' ', y_pos)
                        pygame.display.update()

                        queue.append(next_cell)
    return -1

def heuristic_value(curr_node,dest):
    return (abs(curr_node.x-dest.x)+abs(curr_node.y-dest.y))

def greedybfs(Grid, dest: GridPosition, start: GridPosition):
    screen.fill(WHITE)
    pygame.display.flip()
    for row in range(len(Grid)):  # ze pocet rows
        for col in range(len(Grid[0])):  # pocet cols
            if Grid[row][col] == '2':
                screen.blit(MARIO, (col * MARGIN, row * MARGIN))

                continue
            if Grid[row][col] == '0' or Grid[row][col] == '3':
                continue

            screen.blit(WALL, (col * MARGIN, row * MARGIN))

    pygame.display.flip()


    adj_cell_x = [-1, 0, 0, 1]
    adj_cell_y = [0, -1, 1, 0]
    m, n = (len(Grid), len(Grid[0]))
    visited_blocks = [[False for i in range(m)]
                      for j in range(n)]
    visited_blocks[start.x][start.y] = True
    q = queue.PriorityQueue()
    sol = Node(start, 0)
    q.put((0, sol))
    cells = 4
    cost = 0
    while q:
        current = q.get()  # Dequeue the front cell
        current_block = current[1]
        current_pos = current_block.pos

        # if goal found than return cost
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Algorithm used = GBFS")
            print("No. of moves utilized = ", cost)
            return current_block.cost

        # if current block not in visited than add in visited
        if current_block not in visited_blocks:
            visited_blocks[current_pos.x][current_pos.y] = True
            cost = cost + 1

        x_pos = current_pos.x
        y_pos = current_pos.y

        for i in range(cells):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
                post = GridPosition(x_pos, y_pos)
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
                post = GridPosition(x_pos, y_pos)
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
                post = GridPosition(x_pos, y_pos)
            if x_pos < len(Grid) and y_pos < len(Grid[0]) and x_pos >= 0 and y_pos >= 0:
                if Grid[x_pos][y_pos] == 1:
                    if not visited_blocks[x_pos][y_pos]:
                        h = heuristic_value(post, dest)  # getting heuristic value of the neighbours
                        next_cell = Node(GridPosition(x_pos, y_pos), current_block.cost + 1)
                        visited_blocks[x_pos][y_pos] = True
                        screen.blit(X, (y_pos * MARGIN, x_pos * MARGIN))
                        pygame.time.delay(200)
                        print(x_pos, ' ', y_pos)
                        pygame.display.update()
                        q.put((h, next_cell))

    return -1
