class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        #dictionary that maps number to Roman numerals
        romanToInt = [(1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40,"XL"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")]
        ind = 0
        while num > 0:
            while romanToInt[ind][0] <= num:
                print(num)
                num -= romanToInt[ind][0]
                roman += romanToInt[ind][1]
            ind += 1
        return roman