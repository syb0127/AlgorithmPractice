class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memoization = [False for i in range(len(s)+1)]
        memoization[-1] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i+len(w) <= len(s):
                    if s[i:i+len(w)] == w:
                        memoization[i] = memoization[i+len(w)]
                if memoization[i]:
                    break
        return memoization[0]