class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        N = len(self.data)
        
        # Check row validity
        for row in self.data:
            if len(set(row)) != N:
                return False
        
        # Check column validity
        for col in range(N):
            column = [row[col] for row in self.data]
            if len(set(column)) != N:
                return False

        # Check subgrid validity
        subgrid_size = int(N**0.5)
        for i in range(0, N, subgrid_size):
            for j in range(0, N, subgrid_size):
                subgrid = []
                for x in range(i, i + subgrid_size):
                    for y in range(j, j + subgrid_size):
                        subgrid.append(self.data[x][y])
                if len(set(subgrid)) != N:
                    return False
        return True