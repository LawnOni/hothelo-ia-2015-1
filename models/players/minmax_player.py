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
		best = -99
		moves = board.valid_moves(self.color)
		for move in moves:
			if self.positions[move.x][move.y] > best:
				retMove = move
				
		return retMove
		# moves = board.valid_moves(self.color)
		# for move in moves:
		  # boardPossibility = board.get_clone()
		  # boardPossibility.play(move, self.color)
		  # print boardPossibility

		# return moves[0]
