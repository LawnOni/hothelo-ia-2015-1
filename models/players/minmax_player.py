class MinmaxPlayer:
    def __init__(self, color):
        self.color = color
        self.positions = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,99,-8,8,6,6,8,-8,99,0],
            [0,-8,-24,-4,-3,-3,-4,-24,-8,0],
            [0,8,-4,7,4,4,7,-4,8,0],
            [0,6,-3,4,0,0,4,-3,6,0],
            [0,6,-3,4,0,0,4,-3,6,0],
            [0,8,-4,7,4,4,7,-4,8,0],
            [0,-8,-24,-4,-3,-3,-4,-24,-8,0],
            [0,99,-8,8,6,6,8,-8,99,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    
    

    def play(self, board):
        return max(board, 4)[1]
        
    def getBestMove(self, board):
        best_value = -99
        moves = board.valid_moves(self.color)
        for move in moves:
            if self.positions[move.x][move.y] > best_value:
                retMove = move
                
        return retMove, best_value
        
    def max(self, board, depth):
        if depth == 0:
            return self.getBestMove(board)
                
        moves = board.valid_moves(self.color)
        best_value = -99
        retMove = None
        for move in moves:
            board_clone = board.get_clone()
            board_clone.play(move,self.color)
            min_move, min_value = self.min(board_clone, depth-1)
            if min_value > best_value:
                best_value = min_value
                retMove = min_move
                
        return retMove, best_value
            
            
            
    def min(self, board, depth):
        if depth == 0:
            return self.getBestMove(board)
            
        if self.color == Board.BLACK:
            p2_color = Board.WHITE
        else:
            p2_color = Board.BLACK
        
        moves = board.valid_moves(p2_color)
        best_value = 99
        retMove = None
        
        for move in moves:
            board_clone = board.get_clone()
            board_clone.play(move,p2_color)
            max_move, max_value = self.max(board_clone, depth-1)
            if max_value < best_value:
                best_value = max_value
                retMove = max_move
                
        return retMove, best_value