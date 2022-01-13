#example input
root = [3,9,20,null,null,15,7]

#solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #recursive solution
     
        #array to store each level
        levels = []
        
        #if no tree then we cannot traverse any nodes
        if root is None:
            return levels
        
        def helper(node, level):
            
            #start the current level
            if len(levels) == level:
                levels.append([])
            
            #add the current node in to that level
            levels[level].append(node.val)
            
            #then run function again for child nodes (next level)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        
        #start from the top of the tree (level 0)
        helper(root, 0)
        
        #return nodes in level order
        return levels
    
        
        
        #iterative solution
        
        #if no tree then we cannot traverse any nodes
        if root is None:
            return []
        
        #create a queue to store the tree
        queue = deque([root])
        
        #array to store our nodes in level order
        result = []
        
        #while there are still nodes in the queue
        while queue:
            
            #where we store the nodes for that level
            level = []
            
            #iterate through tree
            for _ in range(len(queue)):
                
                #BFS uses FIFO so we will pop the node out to the left
                node = queue.popleft()
                
                #if node exists
                if node:
                    
                    #add to next level
                    level.append(node.val)
                    
                    #add the nodes children into the queue from left to right
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if level:
                result.append(level)
                
                
        return result
