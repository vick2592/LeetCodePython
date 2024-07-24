class Solution:
    def countHighestScoreNodes(parents):
        from collections import defaultdict
        
        # Step 1: Build the tree as a graph
        children = defaultdict(list)
        for i, p in enumerate(parents):
            if p != -1:  # Skip the root's parent
                children[p].append(i)
        
        # Helper function to calculate subtree sizes
        def dfs(node):
            size = 1  # Count the current node
            for child in children[node]:
                size += dfs(child)
            subtree_sizes[node] = size
            return size
        
        # Step 2: Calculate subtree sizes
        n = len(parents)
        subtree_sizes = [0] * n
        dfs(0)  # Start DFS from the root
        
        # Step 3: Calculate scores and find the max score
        max_score = 0
        count = 0
        for node in range(n):
            score = 1
            total_size = n
            
            for child in children[node]:
                score *= subtree_sizes[child]
                total_size -= subtree_sizes[child]
            
            if node != 0:  # If not the root, include the "remaining tree" size
                score *= (total_size - 1)
            print("Node and size: ", node, score)
            
            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1
        
        return count

# Example usage
parents = [-1,2,0,2,0]
answer = Solution.countHighestScoreNodes(parents)
print(answer)  # Expected output: 3
