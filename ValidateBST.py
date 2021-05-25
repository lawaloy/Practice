class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lower = float("-inf")
        higher = float("inf")
        stack = []
        node = root
        stack.append([lower, node, higher])
        while len(stack) > 0:
            left, curNode, right = stack.pop()
            #if curNode is None:
            #    continue
            if left >= curNode.val or curNode.val >= right:
                return False
            if curNode.left:
                stack.append([left, curNode.left, curNode.val])
            if curNode.right:
                stack.append([curNode.val, curNode.right, right])
            
        return True
