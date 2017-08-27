import copy

class ChessMetric:

    move_king = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
    move_knight = [(-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1), (-2,-1)]
    moves = move_knight + move_king
    chess = None
    chess_size = 0

    def is_in_chess(self, x, y):
        return 0 <= x < self.chess_size and 0 <= y < self.chess_size

    def how_many(self, size, start, end, num_moves):
        self.chess_size = size
        self.chess = [[0 for _ in range(size)] for _ in range(size)]

        current_kingknight = [[0 for _ in range(size)] for _ in range(size)]
        current_kingknight[start[0]][start[1]] = 1
        self.chess[start[0]][start[1]] = 1

        for i in range(num_moves):
            next_kingknight = [[0 for _ in range(size)] for _ in range(size)]
            before_chess = copy.deepcopy(self.chess)

            for x in range(size):
                for y in range(size):
                    if current_kingknight[x][y] == 1:
                        for x1, y1 in self.moves:
                            x2, y2 = x + x1, y + y1
                            if self.is_in_chess(x2, y2):
                                self.chess[x2][y2] += before_chess[x][y]
                                next_kingknight[x2][y2] = 1
            if i == 0:
                self.chess[start[0]][start[1]] = 0
            current_kingknight = copy.deepcopy(next_kingknight)

        return self.chess[end[0]][end[1]]

C = ChessMetric()
print(C.how_many(3,(0,0),(1,0),1))
print(C.how_many(3,(0,0),(1,2),1))
print(C.how_many(3,(0,0),(2,2),1))
print(C.how_many(3,(0,0),(0,0),2))
print(C.how_many(100,(0,0),(0,99),50))
