class Solution:
    def maxTaxiEarnings(self, n, rides):
        # Sort rides by end time
        rides.sort(key=lambda x: x[1])
        print(rides)
        
        # Initialize DP array
        dp = [0] * (n + 1)
        
        ride_index = 0
        for i in range(1, n + 1):
            # Carry forward the previous maximum profit
            dp[i] = dp[i - 1]
            
            # Update DP array for all rides ending at point i
            while ride_index < len(rides) and rides[ride_index][1] == i:
                start, end, tip = rides[ride_index]
                dp[i] = max(dp[i], dp[start] + (end - start + tip))
                ride_index += 1
        
        return dp[n]

n = 20
rides = [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]

answer = Solution()
result = answer.maxTaxiEarnings(n, rides)
print(result)  # Expected output: 20