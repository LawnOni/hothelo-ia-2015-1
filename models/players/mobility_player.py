from models.board import Board

class MobilityPlayer:
    def __init__(self, color):
        self.color = color
        self.opponent_color = self.getOppositeColor(color)
    
    def getOppositeColor(self, color):
        if color == Board.BLACK:
            return Board.WHITE
        else:
            return Board.BLACK

    def play(self, board):
        minimax = self.max(board, 2)
        return minimax[0]
        
    def getBestMove(self, board, color):
        best_value = -99
        moves = board.valid_moves(color)
        retMove = None
        movesLength = 99
        for move in moves:
            board_clone = board.get_clone()
            board_clone.play(move,color)

            valid_moves = board_clone.valid_moves(self.getOppositeColor(color))

            if valid_moves.__len__() < movesLength:
                movesLength = valid_moves.__len__()
                retMove = move
                
        return retMove, (moves.__len__() - movesLength)
        
    def max(self, board, depth):
        if depth == 0:
            return self.getBestMove(board, self.color)
                
        moves = board.valid_moves(self.color)

        if moves.__len__() == 0:
            return None, 99

        best_value = -99
        retMove = None
        for move in moves:
            board_clone = board.get_clone()
            board_clone.play(move,self.color)
            min_move, min_value = self.min(board_clone, depth-1)
            if min_value >= best_value:
                best_value = min_value
                retMove = move

        return retMove, best_value
            
            
            
    def min(self, board, depth):       

        if depth == 0:
            return self.getBestMove(board, self.opponent_color)
        
        moves = board.valid_moves(self.opponent_color)

        if moves.__len__() == 0:
            return None, -99

        best_value = 99
        retMove = None
        
        for move in moves:
            board_clone = board.get_clone()
            board_clone.play(move,self.opponent_color)
            max_move, max_value = self.max(board_clone, depth-1)
            if max_value <= best_value:
                best_value = max_value
                retMove = move

        return retMove, best_value