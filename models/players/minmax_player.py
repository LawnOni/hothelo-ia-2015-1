class MinmaxPlayer:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    moves = board.valid_moves(self.color)
    for move in moves:
      boardPossibility = board.get_clone()
      boardPossibility.play(move, self.color)
      print boardPossibility

    return moves[0]
