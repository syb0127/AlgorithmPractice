class Solution:
    def numDecodings(self, s: str) -> int:
        #처음 table 만들때 default value가 뭔지 잘 생각해야함
        dp = [0] * (len(s)+1)
        # An empty string can only be decoded as an empty string.
        dp[0] = 1
        # 길이가 1인 string을 decode하는 방법은 A(1), B(2), C(3) 등등 밖에 없음. 한가지 방법이니 1로 설정.
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        
        for i in range(2, len(s)+1):
            #여기서 두가지 케이스로 나뉘는데 알파벳은 26개이므로 하나의 digit이나 두개의 digit으로 grouping하는 방법이 있음. Coin change 같이 inner for loop을 돌릴 필요는 없고 이 두가지 케이스를 각자 테스트 해보면 됨.
            
            #1 digit grouping 확인
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            
            #2 digit grouping이 가능
            if i != (len(s) + 1):
                #i-1,i-2가 subproblem
                two_digit = int(s[i-2:i])
                if two_digit <= 26 and  two_digit >= 10:
                    dp[i] += dp[i-2]
                    
        return dp[len(s)]