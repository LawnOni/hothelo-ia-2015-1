class MobilityPlayer:
    def __init__(self, color):
        self.color = color
        self.opponent_color = None
        self.total_plays = 0
    
    def getOppositeColor(self, color, board):
        if color == board.BLACK:
            return board.WHITE
        else:
            return board.BLACK

    def play(self, board):
        alpha = -float('inf')
        beta = float('inf')
        self.opponent_color = self.getOppositeColor(self.color, board)

        import time; start_time = time.time()
        minimax = self.max(board, 4, alpha, beta)
        print("time elapsed: %.1f seconds" %(time.time() - start_time))
        print minimax[0]
        print "total moves = ",self.total_plays
        self.total_plays = 0
        return minimax[0]
        
    def getBestMove(self, board, color):
        best_value = -float('inf')
        moves = board.valid_moves(color)
        self.total_plays += len(moves)
        retMove = None
        movesLength = board.valid_moves(self.getOppositeColor(color, board)).__len__()
        scores = board.score()
        if self.color == board.BLACK:
                oponnent_score = scores[0]
        else:
            oponnent_score = scores[1]
                
        return (moves.__len__() - movesLength - oponnent_score)
        
    def max(self, board, depth, alpha, beta):
        if depth == 0:
            return None, self.getBestMove(board, self.color)
                
        moves = board.valid_moves(self.color)

        if moves.__len__() == 0:
            return self.min(board, depth-1, alpha, beta)

        best_value = -float('inf')

        retMove = None
        for move in moves:
            board_clone = board.get_clone()
            board_clone.play(move,self.color)
            min_value = self.min(board_clone, depth-1, alpha, beta)[1]

            if min_value >= best_value:
                best_value = min_value
                retMove = move

            alpha = max(best_value, alpha)
            if alpha > beta:
                return None, float('inf')

        return retMove, best_value 

    def min(self, board, depth, alpha, beta):       

        if depth == 0:
            return None, self.getBestMove(board, self.color)
        
        moves = board.valid_moves(self.opponent_color)

        if moves.__len__() == 0:
            return self.max(board, depth-1, alpha, beta)

        best_value = float('inf')
        retMove = None
        
        for move in moves:
            board_clone = board.get_clone()
            board_clone.play(move,self.opponent_color)
            max_value = self.max(board_clone, depth-1, alpha, beta)[1]

            if max_value <= best_value:
                best_value = max_value
                retMove = move

            beta = min(best_value, beta)

            if alpha > beta:
                return None, -float('inf')

        return retMove, best_value