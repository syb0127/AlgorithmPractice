from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        longest = 0
        distinct = defaultdict()

        l, r = 0, 0
        while r < len(s):
            #we add the right value and since we are using a hashmap, it already checks if s[r] is already in the hashmap and updates it
            #all keys in dictionary must be unique in Python
            distinct[s[r]] = r

            if len(distinct) == 3:
                #find the leftmost element out of the three
                leftmost = min(distinct.values())
                #this works since s[leftmost] will find the index of the first(leftmost) occurrence of leftmost element
                del distinct[s[leftmost]]
                #with the prev 2 lines, we only need l for calculating the length of the longest substring so far
                l = leftmost+1
            longest = max(longest, (r - l + 1))
            r += 1

        return longest