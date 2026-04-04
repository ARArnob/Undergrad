class GC:
    def __init__(self):
        self.winning_colors = []
    def init(self):
        try:
            with open("input.txt", "r") as f:
                self.N, self.M, self.K = map(int, f.readline().split())
                graph = [[0] * self.N for _ in range(self.N)]
        
                for _ in range(self.M):
                    u, v = map(int, f.readline().split())
                    graph[u][v] = 1
                    graph[v][u] = 1
        except FileNotFoundError:
            print("File not found!")
            return
                
        self.color_list = [0] * self.N

        if self.st_gc(graph, 0):
            print(f"Coloring Possible with {self.K} Colors")
            print(f"Color Assignment: {self.winning_colors}")
        else:
            print(f"Coloring Not Possible with {self.K} Colors")
    
    def check_colors(self, graph, v, color):
        for i in range(self.N):
            if graph[v][i] == 1 and self.color_list[i] == color:
                return False
        return True
    
    def st_gc(self, graph, v):
        if v == self.N:
            self.winning_colors = self.color_list.copy()
            return True
        for i in range(1, self.K+1):
            if self.check_colors(graph, v, i):
                self.color_list[v] = i

                if self.st_gc(graph, v+1):
                    return True
                
                self.color_list[v] = 0
        return False

if __name__ == "__main__":
    gc = GC()
    gc.init()
