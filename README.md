# trees
A collection of LeetCode solutions for tree questions

A tree is a frequently-used data structure to stimulate a hierachical tree structure, each node of the tree will have a root value and a list of references to other nodes (which we call child nodes)

A binary tree is a rooted tree in which each node has no more than 2 children, if a tree is a rooted tree in which each node has no more than N children - it is called an N-ary tree

There are four traversal methods for trees:

Preorder Traversal - visit the root node, then traverse each subtree from left to right

Inorder Traversal - start from the base of the left subtree, cover each level of that subtree then move up, visit root node, then work from base up on the remaining subtrees (left to right)

Postorder Traversal - cover all subtrees from base up and then left to right, finally, visit the root node

Levelorder Traveral - traverse the tree by level, left to right

There are two general strategies for traversing trees:

Breadth First Search (BFS), using a queue data structure, we scan through the tree level by level, following the order of height from top to bottom, we normally use this for levelorder traversal

Depth First Search (DFS), using a stack data structure, we adopt depth as the priority, starting at the root and reaching all the way down to a certain leaf, then back to the root to reach another branch, we normally use this for preorder, inorder and postorder traversal
