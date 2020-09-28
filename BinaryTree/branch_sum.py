class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

class BT(BinaryTreeNode):
    def traverse_tree(self, root):
        if root is None:
            return
        self.traverse_tree(root.left)
        self.traverse_tree(root.right)
        print("{}->".format(root.value), end="")

    def insert(self, values, i=0):
        # this insert nodes one by one to create a Binary tree, not BST

        # example: when we have BT(1).insert([2, 3])
        # first we insert [2] with i=0 (values[0]), insert 2 to 1's left since it's none
        # then [3] with i=1 (values[1]), insert 3 to 1's right since it's none
        # when we try to insert values[2] which is none, then i== len(values), we stop insert

        # q is always [1] in the beginning
        # first q is [1] only, q.pop(0) is 1, so insert 2 to 1's left, break, call insert (3, 1)
        # now q is [1] again, q.pop(0) is 1
        # so next insert 3 to 1's right, break, call insert (4, 2)

        # now when we go to insert 4, and q is reset to [1] again
        # we pop q[0]==1, since its left and right are not none, we call q.append(cur.left), then q becomes [2]
        # then q.append(cur.right), then q = [2,3]
        # Then call insert(5,3)
        # now q is reset to [1] again
        # then q.pop(0) == 1, we find 1's left and right are not none, so append 2&3 to q, so q=[2,3]
        # then q.pop(0) == 2, we find 2's left is not none, append 4 to q, so q=[3,4], 
        # then find 2's right is None, so insert 5 to 2's right, break 
        if i >= len(values):
            return

        # here q is always [1], because everytime we are here, we call the function recursively
        # so we always re-enter the function, and q starts with [1]
        # q is updated within the while loop
        q = [self]
        print("q begins".center(20, "="))
        for x in q:
            print(x.value)
        print("..............")
        print('q[0] value {}'.format(q[0].value))
        while len(q) > 0:
            cur = q.pop(0) # pop the node from leftest
            print('cur node value = {}'.format(cur.value))
            if cur.left is None:
                print("insert {} to {}'s left".format(values[i], cur.value))
                cur.left = BinaryTreeNode(values[i])
                break
            print("append cur.left {} to q".format(cur.left.value))
            q.append(cur.left)
            print("q".center(10, "-"))
            for x in q:
                print(x.value)
            if cur.right is None:
                print("insert {} to {}'s right".format(values[i], cur.value))
                cur.right = BinaryTreeNode(values[i])
                break
            print("append cur.right {} to q".format(cur.right.value))
            q.append(cur.right)
            print("q".center(10, "*"))
            for x in q:
                print(x.value)
        print("call insert recursively")
        self.insert(values, i+1)
        return self
    def printSelf(self):
        print(self.value)
        print(self.left)
        print(self.right)

    def bst_insert(self, value):
        # this insert nodes as a BST: left < cur < right
        # 1
        #  2
        #   4
        #  3 5
        if value < self.value:
            if self.left is None:
                self.left = BT(value)
            else:
                self.left.bst_insert(value)
        else:
            if self.right is None:
                self.right = BT(value)
            else:
                self.right.bst_insert(value)
        return self


class Solution(object):
    def print_branch_sum(self, tree):
        sum_out = []
        self.print_bs(tree, 0, sum_out)
        print(sum_out)

    def print_bs(self, tree, runningSum, sum_out):
        # have two returns to break the recursion
        # sum_out is updated during the call, so only return is enough, no need to return a value
        # first is, if tree i None
        if tree is None:
            return


        # first add current node's value to runningSum
        runningSum = runningSum + tree.node


class Solution(object):
    def print_branch_sum(self, tree):
        sum_out = []
        self.print_bs(tree, 0, sum_out)
        print(sum_out)

    def print_bs(self, tree, runningSum, sum_out):
        # have two returns to break the recursion
        # sum_out is updated during the call, so only return is enough, no need to return a value
        # first is, if tree i None
        if tree is None:
            return


        # first add current node's value to runningSum
        runningSum = runningSum + tree.value

        # the recursive call can be put here, or after checking if the tree is leaf
        # but must be after runningSum update
        self.print_bs(tree.left, runningSum, sum_out)
        self.print_bs(tree.right, runningSum, sum_out)

        # if we go to the leaf node, then it's time to append the runningSum to the output
        if tree.left is None and tree.right is None:
            sum_out.append(runningSum)
            # second 
            return



tree = BT(1).insert([2, 3, 4, 5, 6])
# tree = BT(1).bst_insert(2).bst_insert(4).bst_insert(3).bst_insert(5)
# tree = BT(100).bst_insert(5).bst_insert(15).bst_insert(2).bst_insert(1).bst_insert(5)
tree.traverse_tree(tree)

sol = Solution()
sol.print_branch_sum(tree)



