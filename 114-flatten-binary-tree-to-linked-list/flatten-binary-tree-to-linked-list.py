# class Solution:
#     def flatten(self, root: TreeNode | None) -> None:

#         self.prev = None

#         def dfs(node):
#             if not node:
#                 return

#             dfs(node.right)
#             dfs(node.left)

#             node.right = self.prev
#             node.left = None

#             self.prev = node

#         dfs(root)

class Solution:
    def flatten(self, root: TreeNode | None) -> None:

        curr = root

        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree
                prev = curr.left

                while prev.right:
                    prev = prev.right

                # Connect the original right subtree
                # to the rightmost node
                prev.right = curr.right

                # Move left subtree to the right
                curr.right = curr.left
                curr.left = None

            curr = curr.right