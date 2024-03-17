class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #1.Initialize an empty stack.
        #2.Add numbers until I see an operator.
        #3.When I run into an operator, pop 2 numbers and do math.
        #4.Add the result of the operation back to the stack. 
        #5.Theoretically, when I reach the end of the array, I should only have 1 element left.
        #6.Pop and return.
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operators = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                if tokens[i] == "+":
                    result = first_num+second_num
                elif tokens[i] == "-":
                    result = first_num-second_num
                elif tokens[i] == "*":
                    result = first_num*second_num
                else:
                    result = int(first_num/second_num)
                stack.append(result)
        return stack.pop()
                