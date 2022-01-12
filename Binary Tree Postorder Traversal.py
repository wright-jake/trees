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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create a stack to store our tree
        stack = [root]
        
        #array where we store our nodes in postorder
        result = []
        
        #while stack still contains nodes to traverse
        while stack:
            
            #pop top node off the stack
            node = stack.pop()
            
            #if node is valid/exists
            if node:
                
                #add the value of the node to our result array
                result.append(node.val)
                
                #add the children of this node to the stack
                stack.append(node.left)
                stack.append(node.right)
                
        #postorder so we want it in reverse       
        return result[::-1]
