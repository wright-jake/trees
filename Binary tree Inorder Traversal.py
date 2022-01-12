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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create a stack to store our tree
        stack = []
        
        #array where we store our nodes in preorder 
        result = []
        
        #while stack still contains nodes to traverse
        while root is not None or stack:
            
            #check we still have more nodes to traverse in that subtree
            while root is not None:
                
                #add node to our stack
                stack.append(root)
                
                #then change our current node to the left child
                root = root.left
            
            #if no more left children pop off this node
            root = stack.pop()
            
            #add node value to our result array
            result.append(root.val)
            
            #now we deal with the right child
            root = root.right
        
        #return nodes from the inorder traversal
        return result
