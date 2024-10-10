class Solution:
    def findProductsOfElements(queries):
        def get_binary_representation_values(num):
            binary_rep = bin(num)[2:]  # Get binary representation and remove '0b' prefix
            values = []
            #print(binary_rep)
            for i, bit in enumerate(reversed(binary_rep)):
                if bit == '1':
                    values.append(2 ** i)
            return values

        print(get_binary_representation_values(9))
    # Construct big_nums
        big_nums = []
        i = 1
        while len(big_nums) < 1000:  # Arbitrary large number to ensure we cover all queries
            big_nums.extend(get_binary_representation_values(i))
            i += 1

        # Process queries
        ans = []
        for q in queries:
            fromi, toi, modi = q
            product = 1
            for i in range(fromi, toi + 1):
                product *= big_nums[i]
                product %= modi  # Take modulo at each step to avoid overflow
            ans.append(product)

        return ans


queries = [[2,5,3],[7,7,4]]

answer = Solution.findProductsOfElements(queries)
print(answer)