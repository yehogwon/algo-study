# solved
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # target: distance between the start and end position (mile)
        # startFuel: initial amount of gas
        # stations: information of gas stations ([position, fuel])
        
        dp = [startFuel] + [0] * len(stations) # dp[i] is the maximum distance can be reached by refueling at the i-th station
        for i, (pos, fuel) in enumerate(stations): # iterate over each station
            for j in range(i, -1, -1): # back-tracking, kinda
                if dp[j] >= pos: # If the car can reach the current gas staiton with the latest refueled gas
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel) # choice betweeen the previously calculated value and refueling here
        
        for i, dist in enumerate(dp): 
            if dist >= target: 
                return i
        return -1
