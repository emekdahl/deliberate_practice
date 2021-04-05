def maxDepth(self, root: TreeNode) -> int:
    """
    type: TreeNode
    rtype: int

    goal: find maximum depth of binary tree
    """

    if root is None:
        return 0
    else:
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

# time complexity: visit each node once, so O(N) where N is the number of nodes

# space complexity:  in the worst case, the tree is completely unbalanced, e.g. each node has only left child node, the recursion call would occur NN times (the height of the tree), therefore the storage to keep the call stack would be \mathcal{O}(N)O(N). But in the best case (the tree is completely balanced), the height of the tree would be \log(N)log(N). Therefore, the space complexity in this case would be \mathcal{O}(\log(N))O(log(N))
