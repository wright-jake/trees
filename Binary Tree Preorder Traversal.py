#example input
root = [1,null,2,3]

#solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #recursive solution
        
        #if tree is empty then we cannot traverse anything
        if root is None:
            return []
        
        #preorder traversal: root, left, right
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
        
        #iterative solution
        
        #if tree is empty then we cannot traverse anything
        if root is None:
            return []
        
        #create a stack to store our tree
        stack = [root]
        
        #array where we store our nodes in preorder 
        result = []
        
        #while stack still contains nodes to traverse
        while stack:
            
            #pop top node off the stack
            root = stack.pop()
            
            #add the value of the node to our result array
            result.append(root.val)
            
            #stacks use LIFO so we want to add the right subtree first and then the left
            if root.right is not None:
                stack.append(root.right)   
            if root.left is not None:
                stack.append(root.left)
                
        return result
                
