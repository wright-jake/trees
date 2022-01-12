#example input
root = [1,null,3,2,4,null,5,6]

#solution
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
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
            stack.extend(node.children[::-1])
        
        return output
