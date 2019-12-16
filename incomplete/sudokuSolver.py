# sooo
# solving a sudoku



# strategy
# each lline must have a number k and just one k 
# so eliminate nos for each square using different rules
# and hit the same algos once you narrow down one or more squares




# to use for elimination 
# check 3x3 square, check row and column.
# after elimination and full narrow down start guessing, use backtracking or some kind of a number game
# check unique elements from deleted elements, ie in any row, if only one spot has 9 possible then that is 9
#  
# min 1 and max 1 occurence of no in row, col, box   




class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        