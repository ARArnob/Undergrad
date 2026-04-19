class GC:
    def __init__(self):
        self.found = False
        self.winning_colors = []
    def init(self):
        self.N = 6
        self.K = 4
        self.color_list = [0] * self.N
        self.graph = [[0] * self.N for _ in range(self.N)]
        for i in range(9):
            u, v = map(int, input().split())
            self.graph[u][v] = 1
            self.graph[v][u] = 1
        print("Adjacency Matrix representation of the graph: ")
        for i in self.graph:
            print(i)
        self.Nodes = ['a', 'b', 'c', 'd', 'e', 'f']
        self.colors = ["red", "green", "blue", "yellow"]

        for i in range(self.K):
            if self.st_gc(0, i):
                for j in range(self.N):
                    print(f"{self.Nodes[j]}={self.colors[self.winning_colors[j]-1]}")
                print(f"Minimum number of colors: {i}")
                return
        
    def is_possible(self, v, color):
        for i in range(self.N):
            if self.graph[v][i] == 1 and self.color_list[i] == color:
                return False
        return True
    
    def st_gc(self, v, limit):
        if v == self.N:
            self.found = True
            self.winning_colors = self.color_list.copy()
            return True
        for i in range(1, limit+1):
            if self.is_possible(v, i):
                self.color_list[v] = i
                if self.st_gc(v+1, limit):
                    return True
                self.color_list[v] = 0
        return False


gc = GC()
gc.init()
