# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


class TreeNode:
    
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    
       
class Solution:
    def __init__(self) -> None:
        pass
    
    def create_tree(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode (6)       
        
        root.right = TreeNode (15)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode (18)

        return root

    def create_tree_bad(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        # root.right = TreeNode (2)
        return root

    prev = None
    def in_order_validate(self, root):        
        if root:
            if not self.in_order_validate(root.left):
                return False
            if self.prev and self.prev >= root.val:
                return False
            
            self.prev = root.val

            return (self.in_order_validate(root.right))
        return True


    
    def in_order(self,root):
        if root:
            self.in_order(root.left)
            print(root.val)
            self.in_order(root.right)


if __name__ == "__main__":
    solution = Solution()
    tree = solution.create_tree()
    print("*** Print the tree in order: [Left-Node-Right] ***")
    solution.in_order(tree)
    print("*** Check if the binary search tree is valid ***")
    result = solution.in_order_validate(tree)   
    if result:
        print("The binary tree is a BTS")
    else:
        print("The binary tree is not a BTS")


