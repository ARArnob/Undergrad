import random
import math

class MinMax():
    def __init__(self):
        self.Node = []
        for i in range(8):
            self.Node.append(random.randint(2, 25))
            
        self.maxdepth = int(math.log(len(self.Node), 2))
        self.minimax_nodes = 0
        self.ab_nodes = 0
        
        print(f"Generated Leaf Nodes: {self.Node}")
        
        optimal_val = self.minimax(0, 0, True)
        print("Minimax:")
        print(f"  Nodes Evaluated: {self.minimax_nodes}")
        print(f"  Optimal Value: {optimal_val}")
        
        self.alphabeta(0, 0, True, float('-inf'), float('inf'))
        pruned = self.minimax_nodes - self.ab_nodes
        improvement = round((pruned / self.minimax_nodes) * 100, 2)
        
        print("Alpha-Beta Pruning:")
        print(f"  Nodes Evaluated: {self.ab_nodes}")
        print(f"  Nodes Pruned: {pruned}")
        print(f"Efficiency Improvement: {improvement}%")

    def minimax(self, currentDepth, currentNode, maxTurn):
        self.minimax_nodes += 1
        if currentDepth == self.maxdepth:
            return self.Node[currentNode]
        if maxTurn:
            return max(self.minimax(currentDepth+1, currentNode * 2, False), self.minimax(currentDepth+1, (currentNode * 2) + 1, False))
        else:
            return min(self.minimax(currentDepth + 1, currentNode * 2, True), self.minimax(currentDepth + 1, (currentNode * 2) + 1, True))

    def alphabeta(self, currentDepth, currentNode, maxTurn, alpha, beta):
        self.ab_nodes += 1
        if currentDepth == self.maxdepth:
            return self.Node[currentNode]
        if maxTurn:
            best_val = self.alphabeta(currentDepth + 1, currentNode * 2, False, alpha, beta)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                return best_val
            right_val = self.alphabeta(currentDepth + 1, (currentNode * 2) + 1, False, alpha, beta)
            return max(best_val, right_val)
        else:
            best_val = self.alphabeta(currentDepth + 1, currentNode * 2, True, alpha, beta)
            beta = min(beta, best_val)
            if beta <= alpha:
                return best_val
            right_val = self.alphabeta(currentDepth + 1, (currentNode * 2) + 1, True, alpha, beta)
            return min(best_val, right_val)

if __name__ == "__main__":
    mx = MinMax()
