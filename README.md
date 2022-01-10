# trees
A collection of LeetCode solutions for tree questions

A binary tree is a rooted tree in which each node has no more than 2 children, if a tree is a rooted tree in which each node has no more than N children - it is called an N-ary tree

There are four traversal methods for trees:

Preorder Traversal - visit the root node, then traverse each subtree from left to right

Inorder Traversal - start from the base of the left subtree, cover each level of that subtree then move up, visit root node, then work from base up on the remaining subtrees (left to right)

Postorder Traversal - cover all subtrees from base up and then left to right, finally, visit the root node

Levelorder Traveral - traverse the tree by level, left to right

For traversal's we will either use a queue for breadth-first search or a stack for depth-first search
