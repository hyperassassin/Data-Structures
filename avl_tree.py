class treenode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class avl_tree(object):
    def insert(self,root,key):
        if not root:
            return treenode(key)
        elif key < root.val:
            root.left = self.insert(root.left , key)
        else:
            root.right = self.insert(root.right , key)
        root.height = 1 + max(self.getheight(root.left),self.getheight(root.right))
        balance = self.getbalance(root)
        if balance > 1 and key < root.left.val:
            return self.rightrotate(root)
        if balance < -1 and key > root.right.val:
            return self.leftrotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)
        return root
    
    def leftrotate(self,z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))
        return y
    
    def rightrotate(self,z):
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3
        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))
        return y
    
    def getheight(self,root):
        if not root:
            return 0
        return root.height

    def getbalance(self,root):
        if not root:
            return 0
        return self.getheight(root.left) - self.getheight(root.right)
    
    def preorder(self,root):
        if not root:
            return
        print("{0} ".format(root.val),end = "")
        self.preorder(root.left)
        self.preorder(root.right)

tree = avl_tree()
root = None

root = tree.insert(root , 10)
root = tree.insert(root , 20)
root = tree.insert(root , 30)
root = tree.insert(root , 40)
root = tree.insert(root , 50)
root = tree.insert(root , 25)

"""The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50 """

print("Preorder traversal of the AVL tree is")
tree.preorder(root)
print()
