class Solution:
    def reformatNumber(number):
        nums = []
        for n in number:
            if n == " " or n == "-":
                continue
            else:
                nums.append(n)
                
        ans = ""
        for i in range(len(nums)):
            if len(nums) - i == 4:
                ans += nums[i] + nums[i+1] + "-"
                ans += nums[i+2] + nums[i+3]
                break
            if i % 3 == 0 and i != 0:
                ans += "-"
            ans += nums[i]
                
        print(nums)
        return ans
number = "123 4-5678"
answer = Solution.reformatNumber(number)
print(answer)
