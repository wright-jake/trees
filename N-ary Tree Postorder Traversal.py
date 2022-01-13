#example input
root = [1,null,3,2,4,null,5,6]

#solution
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        #recursive solution
        
        #if there is no tree then we cannot traverse
        if root is None:
            return []
        
        #postorder travel: left -> right -> root
        result = []
        
        #create recursive function
        def solve(root):
            
            #for loop ensures we reach every child
            for child in root.children:
                
                #search for children first 
                solve(child)
                
                #then add parent node
                result.append(child.val)
        
        #call recursive function to start traversal
        solve(root)
        
        #add root node last
        result.append(root.val)
        
        #return nodes in postorder
        return result
        
        #iterative solution
        
        #if there is no tree then we cannot traverse
        if root is None:
            return []
        
        #we will use the stack to store our tree
        stack = [root]
        
        #we will store our traversal-ordered nodes here
        output = []
        
        #while stack still has nodes to traverse
        while stack:
            
            #we will take the top node from the stack
            node = stack.pop()
            
            #add the value of the node to the output
            output.append(node.val)
            
            #we will then add the children of that node into the stack in reverse order - so that we read the nodes left to right
            stack.extend(node.children)
        
        #we want to visit the root node last
        return output[::-1]
