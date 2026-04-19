import math
class AB:
    def __init__(self):
        self.Node = [8, 5, 4, 9, 7, 6, 2, 1]
        self.optimal_value = 0
        self.number_of_nodes_evaluated = 0
        self.max_depth = int(math.log(8, 2))

    def init(self):
        self.optimal_value = self.alpha_beta(0, 0, True, -1000, 1000)
        print(f"Optimal Value = {self.optimal_value}")
        print(f"Number of nodes evaluated = {self.number_of_nodes_evaluated}")
        print(f"Number of nodes pruned = {15-self.number_of_nodes_evaluated}")
    
    def alpha_beta(self, current_depth, current_node, maxTurn, alpha, beta):
        self.number_of_nodes_evaluated += 1
        if current_depth == self.max_depth:
            return self.Node[current_node]
        elif maxTurn:
            best_value = self.alpha_beta((current_depth + 1), ((current_node * 2) + 1), False, alpha, beta)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                return best_value
            left_value = self.alpha_beta((current_depth + 1), (current_node * 2), False, alpha, beta)
            return max(best_value, left_value)
        
        else:
            best_value = self.alpha_beta((current_depth + 1), ((current_node * 2) + 1), True, alpha, beta)
            beta = min(beta, best_value)
            if beta <= alpha:
                return best_value
            left_value = self.alpha_beta((current_depth + 1), (current_node * 2), True, alpha, beta)
            return min(best_value, left_value)

ab = AB() 
ab.init()
