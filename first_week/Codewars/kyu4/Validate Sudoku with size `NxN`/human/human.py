class Sudoku(object):
    def __init__(self, data):
        self.data = data
        
    def is_valid(self):
        board = self.data
        valid = set(range(1, len(board)+1))
        check = int(len(board)**0.5)
        
        if any(type(i)!=int for rows in board for i in rows):
            return False
        
        for row in board:
            if set(row) != valid: 
                return False
            
        for col in [[row[i] for row in board] for i in range(check)]:
            if set(col) != valid: return False        
        
        for x in range(check):
            for y in range(check):
                if set(sum([row[x*check:(x+1)*check] for row in board[y*check:(y+1)*check]], [])) != valid:
                    return False
        return True