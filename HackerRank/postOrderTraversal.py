def postOrder(root):
    if root is None:
        return None
    postOrder(root.left)
    postOrder(root.right)
    print(root.info, end=' ')