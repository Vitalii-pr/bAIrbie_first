class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def _preprocess_data(self, data):
        """Converts non-numeric values to 0, representing empty cells"""
        processed_data = []
        for row in data:
            processed_row = []
            for cell in row:
                try:
                    processed_row.append(int(cell))  # Try converting to integer
                except ValueError:
                    processed_row.append(0)          # Default to 0 if not an integer
            processed_data.append(processed_row)
        return processed_data

    def is_valid(self):
        N = len(self.data)

        # Check row validity
        for row in self.data:
            if not self._is_valid_sequence(row):
                return False

        # Check column validity
        for col in range(N):
            column = [row[col] for row in self.data]
            if not self._is_valid_sequence(column):
                return False

        # Check subgrid validity
        subgrid_size = int(N**0.5)
        for i in range(0, N, subgrid_size):
            for j in range(0, N, subgrid_size):
                subgrid = []
                for x in range(i, i + subgrid_size):
                    for y in range(j, j + subgrid_size):
                        subgrid.append(self.data[x][y])
                if not self._is_valid_sequence(subgrid):
                    return False
        return True

    def _is_valid_sequence(self, seq):
        """Checks if a sequence (row, column or subgrid) is valid"""
        nums = [x for x in seq if x != 0]  # Filter out empty cells
        return len(set(nums)) == len(nums) and all(1 <= x <= len(self.data) for x in nums)
