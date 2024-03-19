class Solution:
    def reverseWords(self, s: str) -> str:
        d = deque()
        left, right = 0, len(s)-1
        
        #remove spaces on the left
        while left <= right and s[left] == ' ':
            left += 1
        #remove spaces on the right
        while left <= right and s[right] == ' ':
            right -= 1
            
        curr_word = []
        while left <= right:
            if s[left] == ' ' and curr_word:
                d.appendleft(''.join(curr_word))
                curr_word = []
            elif s[left] != ' ':
                curr_word.append(s[left])
            left += 1
        d.appendleft(''.join(curr_word))
        
        return ' '.join(d)