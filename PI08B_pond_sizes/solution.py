from typing import List

def compute_pond_sizes(land: List[List[int]]) -> List[int]:
    sizes = []
    n_rows = len(land)
    n_cols = len(land[0])
    def compute_size(row: int, col: int, size: int) -> int:
        if row == -1 or col == -1 or row == n_rows or col == n_cols:
            return 0
        if land[row][col] == 0:
            land[row][col] = -1 # mark as visited
            size = 1
            for next_row in [row-1, row, row+1]:
                for next_col in [col-1, col, col+1]:
                    size += compute_size(next_row, next_col, size)
            return size
        return 0


    for row in range(n_rows):
        for col in range(n_cols):
            size = compute_size(row, col, 0)
            if size > 0: 
                sizes.append(size)
    for i, row in enumerate(land):
        land[i] = [0 if r == -1 else r for r in row]
    return sizes

if __name__ ==  "__main__":
    land1 = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
    ]

    land2 = [
        [0]
    ]

    land3 = [
        [1]
    ]

    land4 = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    land5 = [
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
        ]

    print("land1 ", compute_pond_sizes(land1))
    print("land2 ", compute_pond_sizes(land2))
    print("land3 ", compute_pond_sizes(land3))
    print("land4 ", compute_pond_sizes(land4))
    print("land5 ", compute_pond_sizes(land5))

            
            
        

        
        
