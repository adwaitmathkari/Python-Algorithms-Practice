def print_mat(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print('')


#strategy
# mark safesquares as true and unsafeas false
# go through mat and mark unsafe squares
# fn markSquares marks unsafe squares due to one piece

class chess:
    def __init__(self, mat):
        self.mat = mat
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.markMatrix = [[True for i in range(
            self.cols)] for j in range(self.rows)]


    def markSquares(self, piece, position, markMatrix):
        if piece != '.':
            markMatrix[position[0]][position[1]] = False
        if piece == 'R':
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            self.markSquaresInDirection(position, markMatrix, dirs)
        elif piece == 'B':
            dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            self.markSquaresInDirection(position, markMatrix, dirs)
        elif piece == 'Q':
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]
            self.markSquaresInDirection(position, markMatrix, dirs)
        elif piece == 'K':
            for dir1 in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                npos = (position[0]+dir1[0], position[1] + dir1[1])
                if self.validSquare(self.rows, self.cols, self.mat, npos):
                    markMatrix[npos[0]][npos[1]] = False
        elif piece == 'S':
            self.markSquaresSpecialPiece(position, markMatrix)


    def markSquaresInDirection(self, position, markMatrix, dirs):
        for dir1 in dirs:
            a = position
            a = (a[0]+dir1[0], a[1]+dir1[1])
            while(self.validSquare(self.rows, self.cols, self.mat, a)):
                markMatrix[a[0]][a[1]] = False
                a = (a[0]+dir1[0], a[1]+dir1[1])


    def markSquaresSpecialPiece(self, pos, markMatrix):
        layer = min(pos[0], self.rows-1-pos[0], pos[1], self.cols-1-pos[1])
        row = pos[0]
        col = pos[1]
        # print(layer)
        for row in [layer, self.rows-1-layer]:
            for col in range(layer, self.cols-layer):
                markMatrix[row][col] = False
        for col in [layer, self.cols-1-layer]:
            for row in range(layer, self.rows-layer):
                markMatrix[row][col] = False

    def validSquare(self, rows, cols, mat, position):
        if not (-1 < position[0] < rows and -1 < position[1] < cols):
            return False
        if mat[position[0]][position[1]] != '.':
            return False
        return True

    # TODO: CRIO_TASK_MODULE_SAFE_SQUARE
    # Input:
    #   1) chess board matrix
    # Task:
    #   1) Implement Rook move
    #   2) Implement Bishop move
    #   3) Implement Queens move
    #   4) Implement knight's move
    #   5) Special move
    # Output:
    #   Count the number of safe square and return it

    def move(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.markSquares(self.mat[row][col],
                                 (row, col), self.markMatrix)
        # print(self.markMatrix)

        safeSquares = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.markMatrix[row][col]:
                    safeSquares += 1

        return safeSquares



# q . . . .
# . . . . .
# . . . . .
# . . . . .
# . . . . .


f=open('crio/safeSqInp', 'r')

for cases in range(int(f.readline())):
    mat=[]
    for i in range(int(f.readline())):
        mat.append(f.readline().strip().split(' '))
    # print(mat)
    c = chess(mat)
    # print(c.markMatrix)
    print(c.move())

# for i in range(len(c.markMatrix)):
#     print(c.markMatrix[i])


# python3 runner.py --problem SafeSquare --lang python --run