from collections import Counter
from re import S

class Solution:
    def minStickers(stickers, target):
        
        sticker_counts = [Counter(sticker) for sticker in stickers]
        dp = {}
        def dfs(target_str):
            if not target_str:
                return 0
            if target_str in dp:
                return dp[target_str]
            ans = float('inf')
            target_count = Counter(target_str)
            for sticker in sticker_counts:
                if target_str[0] not in sticker:
                    continue
                #When subtracting to container objects that have a collection of elements and frequency, you will get a new dictoinary with remaining elements
                #that will have more than 0 frequency or an empty dictionary. 
                remaining_char = target_count - sticker
                letters = [char * count for char, count in remaining_char.items()]
                ans = min(ans, dfs(''.join(letters)) + 1)
                
            dp[target_str] = ans
            return ans
        
        res = dfs(target)
        return res if res != float('inf') else -1
                    
stickers = ["with","example","science"]
target = "thehat"

# stickers = ["notice","possible"]
# target = "basicbasic"

answer = Solution.minStickers(stickers, target)
print(answer)  # Expected output: 3