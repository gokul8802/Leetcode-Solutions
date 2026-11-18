class Solution:
    def postorder(self, root: Optional[TreeNode], result: List[int]) -> None:
        if root is None:
            return

        self.postorder(root.left, result)
        self.postorder(root.right, result)

        result.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.postorder(root, ans)

        return ans