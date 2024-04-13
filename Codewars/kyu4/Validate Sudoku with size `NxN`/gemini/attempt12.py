class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        N = len(self.data)

        # Helper function to validate sets of numbers
        def is_valid_set(numbers):
            return set(numbers) == set(range(1, N + 1))

        # Check rows
        for row in self.data:
            if not is_valid_set(row):
                return False

        # Check columns
        for col in range(N):
            if not is_valid_set([row[col] for row in self.data]):
                return False

        # Check subgrids
        subgrid_size = int(N**0.5)
        for i in range(0, N, subgrid_size):
            for j in range(0, N, subgrid_size):
                subgrid = [self.data[x][y] for x in range(i, i + subgrid_size) for y in range(j, j + subgrid_size)]
                if not is_valid_set(subgrid):
                    return False

        return True