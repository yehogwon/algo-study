# solved
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def swaps(data, coords=None): 
            assert type(coords) is list, "indecies has to be a list"
            assert len(coords) == 4, "the length of coords[] must be 4"

            _data = []
            for i in range(4): 
                cur_coord = coords[i % 4]
                _data.append(data[cur_coord[0]][cur_coord[1]])
            for i, val in enumerate(_data): 
                next_coord = coords[(i + 1) % 4]
                y, x = next_coord[0], next_coord[1]
                data[y][x] = val

        def rotate(M, N, ORG): 
            if N <= 1: 
                return
            else: 
                step_in = (ORG - N) // 2
                for i in range(N - 1): 
                    swaps(M, [
                        (step_in, step_in + i), 
                        (i + step_in, step_in + N - 1), 
                        (N - 1 + step_in, N - 1 - i + step_in), 
                        (N - 1 - i + step_in, step_in)]) 
                    # Left-Top, Right-Top, Right-Bottom, Left-Bottom # (height, width ; y, x)
                rotate(M, N - 2, ORG)
        
        N = len(matrix) # width (also height) of the matrix
        rotate(matrix, N, N)
