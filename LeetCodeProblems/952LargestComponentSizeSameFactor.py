class Solution:
    def largestComponentSize(nums):
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                size[rootY] += size[rootX]
                return size[rootY]
            return size[rootX]

        def primeFactors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, int(n ** 0.5) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 2:
                factors.add(n)
            return factors

        parent = {}
        size = {}

        # Initialize parent and size for each number and its factors
        for num in nums:
            for factor in primeFactors(num):
                if factor not in parent:
                    parent[factor] = factor
                    size[factor] = 1
                if num not in parent:
                    parent[num] = num
                    size[num] = 1
                union(num, factor)

        # Find the size of the largest component
        component_size = {}
        for num in nums:
            root = find(num)
            if root not in component_size:
                component_size[root] = 0
            component_size[root] += 1

        print(parent,size, component_size)

        return max(component_size.values())

nums = [2, 3, 6, 7, 4, 12, 21, 39]
# nums = [20,50,9,63]
answer = Solution.largestComponentSize(nums)
print(answer)  # Expected output: 8