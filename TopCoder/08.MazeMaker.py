TREE = -2
NOT_PASSED = -1

class MazeMaker:
    maze = None
    step = 0
    moves = set()
    maze_size = None

    def longestPath(self, maze, start_row, start_col, move_row, move_col):
        self.init(maze)
        self.start(start_row, start_col)
        self.set_move(move_row, move_col)
        # print(self.maze)
        # print(self.moves)
        # print(self.maze_size)

        self.travel()
        #print(self.maze)
        return self.get_result()

    def travel(self):
        while self.go() == True:
            self.step += 1
            pass

    def go(self):
        new_moved = False
        for r, row in enumerate(self.maze):
            for c, _ in enumerate(row):
                if self.maze[r][c] == self.step:
                    for move in self.moves:
                        new_r, new_c = r + move[0], c + move[1]
                        if self.is_valid_position(new_r, new_c):
                            if self.maze[new_r][new_c] == TREE:
                                pass
                            elif self.maze[new_r][new_c] == NOT_PASSED:
                                new_moved = True
                                self.maze[new_r][new_c] = self.step + 1
        return new_moved

    def is_valid_position(self, r, c):
        return True if 0 <= r < self.maze_size[0] and 0 <= c < self.maze_size[1] else False

    def init(self, maze):
        self.maze = []
        for line in maze:
            one_line = []
            for p in line:
                one_line.append(NOT_PASSED if p == '.' else TREE)
            self.maze.append(one_line)
        self.maze_size = len(self.maze), len(self.maze[0])
        self.moves = set()
        maze_size = None

    def start(self, start_row, start_col):
        self.maze[start_row][start_col] = 0
        self.step = 0

    def set_move(self, move_row, move_col):
        for r, c in zip(move_row, move_col):
            self.moves.add((r, c))

    def get_result(self):
        max_step = 0
        for row in self.maze:
            for e in row:
                if e == NOT_PASSED:
                    return NOT_PASSED
                elif max_step < e:
                    max_step = e
        return max_step


maze_maker = MazeMaker()

print(maze_maker.longestPath(['...','...','...'],0,1,[1,0,-1,0],[0,1,0,-1]))
print(maze_maker.longestPath(['...','...','...'],0,1,[1,0,-1,0,1,1,-1,-1],[0,1,0,-1,1,-1,1,-1]))
print(maze_maker.longestPath(['X.X','...','XXX','X.X'],0,1,[1,0,-1,0],[0,1,0,-1]))
print(maze_maker.longestPath(['.......','X.X.X..','XXX...X','....X..','X....X.','.......'],5,0,[1,0,-1,0,-2,1],[0,1,0,-1,3,0]))
print(maze_maker.longestPath(['.......'],0,0,[1,0,1,0,1,0],[0,1,0,1,0,1]))
print(maze_maker.longestPath(['..X.X.X.X.X.X.'],0,0,[2,0,-2,0],[0,2,0,-2]))

