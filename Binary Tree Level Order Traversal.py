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
