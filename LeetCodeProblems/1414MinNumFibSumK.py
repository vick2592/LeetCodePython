class Solution:
    def findMinFibonacciNumbers(k):
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        print(fib)
        ans = 0
        while k > 0:
            if k >= fib[-1]:
                k -= fib[-1]
                ans += 1
            fib.pop()
        return ans
    
k = 1900
answer = Solution.findMinFibonacciNumbers(k)

print(answer)
