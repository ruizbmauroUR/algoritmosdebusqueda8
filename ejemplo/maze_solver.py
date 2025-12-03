import collections
import heapq

def solve_maze_bfs(maze, start, end):
    """Resuelve el laberinto usando el algoritmo de BÃºsqueda en Amplitud (BFS)."""
    rows, cols = len(maze), len(maze[0])
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (curr_row, curr_col), path = queue.popleft()

        if (curr_row, curr_col) == end:
            return path

        # Movimientos posibles: arriba, abajo, izquierda, derecha
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc
            
            if 0 <= next_row < rows and 0 <= next_col < cols and \
               maze[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                new_path = list(path)
                new_path.append((next_row, next_col))
                queue.append(((next_row, next_col), new_path))
    
    return None # No se encontrÃ³ camino

# Puedes implementar DFS de manera similar, usando una lista como pila (o recursiÃ³n).

def solve_maze_dfs(maze, start, end):
    """Resuelve el laberinto usando el algoritmo de Búsqueda en Profundidad (DFS)."""
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set()
    visited.add(start)

    while stack:
        (curr_row, curr_col), path = stack.pop()

        if (curr_row, curr_col) == end:
            return path

        # Movimientos posibles: arriba, abajo, izquierda, derecha
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc

            if 0 <= next_row < rows and 0 <= next_col < cols and \
                maze[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                new_path = list(path)
                new_path.append((next_row, next_col))
                stack.append(((next_row, next_col), new_path))

    return None  # No se encontró camino

def solve_maze_a_star(maze, start, end):
    """Resuelve el laberinto usando el algoritmo A* (A estrella)."""
    rows, cols = len(maze), len(maze[0])

    def heuristic(a, b):
        # Distancia Manhattan
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Cada entrada en la priority queue es: (costo_estimado_total, costo_g, (row, col), path)
    open_set = []
    heapq.heappush(open_set, (heuristic(start, end), 0, start, [start]))
    visited = set()

    while open_set:
        _, g_cost, (curr_row, curr_col), path = heapq.heappop(open_set)

        if (curr_row, curr_col) == end:
            return path

        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))

        # Movimientos posibles: arriba, abajo, izquierda, derecha
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc

            if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == 0:
                next_pos = (next_row, next_col)
                if next_pos in visited:
                    continue
                new_g = g_cost + 1
                f_cost = new_g + heuristic(next_pos, end)
                new_path = list(path)
                new_path.append(next_pos)
                heapq.heappush(open_set, (f_cost, new_g, next_pos, new_path))

    return None  # No se encontrÃ³ camino

# RepresentaciÃ³n del laberinto (0: camino libre, 1: muro, 2: inicio, 3: fin)
# Un laberinto de ejemplo:

MAZE = [
[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
[1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1],
[1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
[1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1],
[1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1],
[1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1],
[1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1],
[1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1],
[1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1],
[1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1],
[1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1],
[1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1],
[1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1],
[1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
[1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1],
[1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1],
[1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1],
[1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1],
[1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
[1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1],
[1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1],
[1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1],
[1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1],
[1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1],
[1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1],
[1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1],
[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1],
[1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
[1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1],
[1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,1],
[1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1],
[1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1],
[1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1],
[1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]
]    

#MAZE = [
#    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
#    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
#    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
#    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
#    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
#    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#]

START = (0, 1)
END = (36, 30)