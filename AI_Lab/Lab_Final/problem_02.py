class Node:
    def __init__(self, x, y, level, path_history = None):
        self.x, self.y, self.level = x, y, level
        self.path_history = path_history if path_history is not None else []

class DFS:
    def __init__(self):
        self.found = False
        self.number_of_cells = 1
        self.path = []
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def init(self):
        self.N = 5
        self.graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]
        
        self.sx, self.sy = 0, 2
        self.source = Node(self.sx, self.sy, 0, [(self.sx, self.sy)])

        self.st_dfs()
        print(f"Number of reachable cells: {self.number_of_cells}\n[(0, 2)]")
        for i in self.path:
            print(i)

    def st_dfs(self):
        stack = []
        stack.append(self.source)
        visited = {(self.sx, self.sy): 0}
        
        while stack:
            u = stack.pop()
            for dx, dy in self.directions:
                v_x, v_y = u.x + dx, u.y + dy
                if 0 <= v_x < self.N and 0<= v_y < self.N and self.graph[v_x][v_y] == 1:
                    v_level = u.level + 1
                    if (v_x, v_y) not in visited or visited[(v_x, v_y)] > v_level:
                        visited[(v_x, v_y)] = v_level
                        self.number_of_cells += 1
                        new_path = u.path_history + [(v_x, v_y)]
                        self.path.append(new_path)
                        child = Node(v_x, v_y, v_level, new_path)                              
                        stack.append(child)
                    
dfs = DFS()
dfs.init()
