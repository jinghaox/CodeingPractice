class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# note:
# for BST, we can always focus on one subtree, either left or right, so we can do it easily in recursion
# but for BT, we don't have that constraints, so we can't focus on one subtree
# to insert a new node, it can be inserted to left subtree, or parent's right (siblings) subtree
class BinaryTree(Node):

    def insert_node(self, arr):
        # this is a method of BT class
        # this one assumes BT's root has been created with a dummy node already
        # we use a helper function for recursion
        # the return of the helper function is the new created node with its left&right children
        def recur(root, arr, i, n):
            print(i)
            if i>=n:
                return
            root = Node(arr[i])
            root.left = recur(root.left, arr, 2*i+1, n)
            root.right = recur(root.right, arr, 2*i+2, n)
            return root

        return recur(self, arr, 0, len(arr))

def insert_recursion(arr, root):
    # this is an external function using recursion
    def insert(arr, root, i, n): 
        # Function to insert nodes in level order  
        # Base case for recursion  
        print(i)
        if i >= n: 
            return

        # first set the root
        # for every insert, the arr[i] will be the root, and we insert 2*i+1 and 2*i+2 to its left and right
        if root is None:
            root = Node(arr[i])  
        else:
            # actually, if root is not None, then we don't need to reassign Node(arr[i]) to root, insert its left/right again, we can just return
            return

        # insert left child  
        root.left = insert(arr, root.left, 2*i+1, n)  

        # insert right child  
        root.right = insert(arr, root.right, 2*i+2, n) 
        return root 

    return insert(arr, root, 0, len(arr))

def insert_iteration(arr, root, i, n):
    # this version is non-recursive version, insert nodes with interation 

    # special case for first node
    if root is None: 
        root = Node(arr[0])

    # use a queue to remember what nodes need to insert
    queue = [root]
    while len(queue):
        cur = queue.pop(0)
        if cur.left is None:
            if 2*i+1 < n:
                cur.left = Node(arr[2*i+1])
            else:
                break
        queue.append(cur.left)
        if cur.right is None:
            if 2*i+2 < n:
                cur.right = Node(arr[2*i+2])
            else:
                break
        queue.append(cur.right)
        i += 1
    return root


def traverse_in_order(root):
    if root is None:
        return
    else:
        traverse_in_order(root.left)
        print("{} ->".format(root.val), end="")
        traverse_in_order(root.right)

def invertBinaryTree(tree):
    if tree is None:
        return
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    tree.left, tree.right = tree.right, tree.left

def invert_BT(root):
    # this is my function, which invx will return the root
    # so invx(root.right) will use the root.right as the root, and return it after it's inverted
    # so first set root.left to temp(t)
    # then invert root.right, and assign the inverted right subtree to root.left
    # then invert temp(t), and assign the inverted left subtree to root.right
    # after it's done, return root
    if root is None:
        return
    t = root.left
    root.left = invert_BT(root.right)
    root.right = invert_BT(t)

    # below is the symetric inversion
    # t = root.right
    # root.right = invx(root.left)
    # root.left = invx(t)
    return root

arr = [1,2,3,4,5,6,7,8]

bt = insert_recusion(arr, None)
# bt = insert_iteration(arr, None, 0, len(arr))

traverse_in_order(bt)

print("\n============\n")

# create a dummy node 0
bt = BinaryTree(0) 
# here's the trick, not bt.insert_node only, need bt = bt.insert_node
# it's like we start from a dummy or None node, 
# and after the insertion, need to assign the output of bt.insert_node to bt
bt = bt.insert_node(arr)
traverse_in_order(bt)
print("\n============\n")
invert_BT(bt)
traverse_in_order(bt)

