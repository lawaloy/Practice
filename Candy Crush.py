class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        if not board:
            return board
        
        rows = len(board)
        cols = len(board[0])
        done = True
        
        # Tag to crush rows
        for row in range(rows):
            for col in range(cols-2):
                num1 = abs(board[row][col])
                num2 = abs(board[row][col+1])
                num3 = abs(board[row][col+2])
                #check if they are the sames to tag them
                if num1 == num2 == num3 and num1 != 0:
                    board[row][col] = -num1
                    board[row][col+1] = -num2
                    board[row][col+2] = -num3
                    done = False
                    
        # Tag to crush columns
        for col in range(cols):
            for row in range(rows-2):
                num1 = abs(board[row][col])
                num2 = abs(board[row+1][col])
                num3 = abs(board[row+2][col])
                
                #check if they are the same to tag them
                if num1 == num2 == num3 and num1 != 0:
                    board[row][col] = -num1
                    board[row+1][col] = -num2
                    board[row+2][col] = -num3
                    done = False
        # Gravity drop           
        if not done:
            for col in range(cols):
                curIdx = len(board)-1
                for row in range(rows-1, -1, -1):
                    #move all positive numbers down
                    if board[row][col] > 0:
                        board[curIdx][col] = board[row][col]
                        curIdx -=1
                        
                #fill with zero wherever that remains        
                for row in range(curIdx,-1,-1):
                    board[row][col] = 0
        if done:
            return board
        
        return self.candyCrush(board)
