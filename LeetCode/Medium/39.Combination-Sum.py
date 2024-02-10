class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def recursiveDFS(leftover, lst, start):
            if leftover < 0:
                return
            elif leftover == 0:
                result.append(list(lst))
                return 
            #이미 확인한 숫자는 확인할 필요가 없기 때문에 range를 계속 조절 해줘야함
            for i in range(start, len(candidates)):
                #the following line doesn't work since I have INFINITE supply of each number and I need to give it "another chance" rather than moving on
                #recursiveDFS(lst.append(candidate), leftover-candidate)
                lst.append(candidates[i])
                recursiveDFS(leftover-candidates[i], lst, i)
                lst.pop()
            return
        
        recursiveDFS(target, [], 0)
        return result