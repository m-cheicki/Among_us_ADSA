import sys


def AVLfromPlayers(listPlayers, AVLTree):
    ''' Return an AVL Tree from a list of Player '''
    root = None
    for _ in listPlayers:
        root = AVLTree.insert_node(root, _)
    return root


# Create a tree node
class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# Create the AVL Tree
class AVLTree(object):
    # Function to insert a node
    def insert_node(self, root, key):
        # Find the correct location and insert the node
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key >= root.left.key:
                root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balanceFactor < -1:
            if key <= root.right.key:
                root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) < 0:
                root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) > 0:
                root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        if y is None:
            return z
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation

    def rightRotate(self, z):
        y = z.left
        if y is None:
            return z
        T3 = y.right
        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        return root.height if root else 0

    # Get balance factore of the node
    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right) if root else 0

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print("{0} ".format(root.key), end="")
        self.inOrder(root.right)

    def getInOrder(self, root):
        return (
            self.getInOrder(root.left) + [root.key] + self.getInOrder(root.right)
            if root
            else []
        )

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)
