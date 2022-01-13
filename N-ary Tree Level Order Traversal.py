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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        #recursive solution
        
        #check to see if tree has any nodes
        if root is None:
            return []
        
        #levelorder traversal: level by level (top - bottom)
        result = []
        
        #create recursive function
        def solve(node, level):
            
            #start the current level
            if len(result) == level:
                result.append([])
            
            #add the current node in that level
            result[level].append(node.val)
            
            #then run function again but for the next level
            for child in node.children:
                solve(child, level + 1)
        
        #start from the root (level 0)
        solve(root, 0)
        
        #return nodes in levelorder
        return result
        
        
        #iterative solution
        
        #check to see if tree has any nodes
        if root is None:
            return []
        
        #where we will store our traversed nodes in level order
        result = []
        
        #create a double ended queue where we will store the nodes of the tree
        queue = deque([root])
        
        #while there are still nodes in the queue
        while queue:
            
            #where we store the nodes for that level
            level = []
            
            #iterate through all the nodes
            for _ in range(len(queue)):
                
                #pop the nodes out adding them to that specific level of the tree
                node = queue.popleft()
                level.append(node.val)
                
                #add children of node to queue
                queue.extend(node.children)
            
            #add our nodes in level order to our result array 
            result.append(level)
        
        #return the nodes in level order
        return result
