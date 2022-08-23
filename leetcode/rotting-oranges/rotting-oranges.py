# solved
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        H, W = len(grid), len(grid[0])
        rotten_coords = [] # a list of tuples
        n_fresh = [0, ]
        for i, row in enumerate(grid): # O(mn)
            for j, item in enumerate(row): 
                if item == 1: 
                    n_fresh[0] += 1
                elif item == 2: 
                    rotten_coords.append((i, j))
        
        if n_fresh[0] == 0: 
            return 0
        
        def update(coord: Tuple[int, int]) -> bool: 
            y, x = coord
            _coords = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
            _updated = False
            for _y, _x in _coords: # O(1)
                if 0 <= _x < W and 0 <= _y < H and grid[_y][_x] == 1: 
                    _updated = True
                    grid[_y][_x] = 2
                    n_fresh[0] -= 1
                    rotten_coords.append((_y, _x))
            return _updated
        
        time_step = -1
        while True: 
            _updated = False
            for rotten in rotten_coords[:]: # O(r)
                _updated |= update(rotten)
            if not _updated: 
                break
            time_step += 1
            if n_fresh[0] == 0: 
                break
        return time_step + 1 if n_fresh[0] == 0 else -1
