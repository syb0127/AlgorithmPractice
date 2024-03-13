class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = curr_tank = 0
        starting_station = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            #if I can't get there
            if curr_tank < 0:
                #reset the starting station as the next station
                starting_station = i+1
                #reset the current tank to 0
                curr_tank = 0
        
        if total_tank >= 0:
            return starting_station
        else:
            return -1