class Solution:
    def multiply(num1, num2):
        intN1 = int(num1)
        intN2 = int(num2)
        intAnswer = intN1 * intN2
        strAnswer = str(intAnswer)
        return strAnswer

num1 = "123"
num2 = "456"

answer = Solution.multiply(num1, num2)
print(answer)  # Expected output: "56088"