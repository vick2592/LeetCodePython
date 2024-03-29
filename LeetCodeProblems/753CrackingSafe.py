class Solution:
    def crackSafe(n, k):
        if n == 1:
            return ''.join(map(str, range(k)))
        seen = set()
        result = []
        def dfs(node, k, seen, result):
            for i in range(k):
                edge = node + str(i)

                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:], k, seen, result)
                    result.append(str(i))

        start_node = "0" * (n - 1)
        print("The start node is: ",start_node)
        dfs(start_node, k, seen, result)
        print(seen)
        return "".join(result) + start_node


n = 2
k = 2

ans = Solution.crackSafe(n, k)
print(ans)  # Output: "00110"
