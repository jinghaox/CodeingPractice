import sys 

class MinHeap_Mine: 
    # my heap data structure has no dummy [0] node with -inf, it starts from [0]  
    # the code from geeksforgeeks has a dummy [0] node, and the heap starts from [1]
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        # heap is saved in an array
        self.Heap = [0]*(self.maxsize + 1) 
        # heap starts from [0]
        self.FRONT = 0
  
    # Function to return the position of parent for the node currently at pos 
    def parent(self, pos): 
        # parent's index is (pos+1)//2-1
        #         0
        #     1       2
        #   3   4    5  6
        # 7  8 9 10
        # e.g. pos = 9, then parent is (9+1)//2-1=4
        #      pos = 10, then parent is (10+1)//2 - 1 = 
        # py2: x/y == x//y (if they are integer)
        # py3: x/y is float
        return (pos+1)//2-1
  
    # Function to return the position of the left child for the node currently at pos 
    def leftChild(self, pos): 
        # left node is 2*pos+1
        # e.g. pos = 4, then left is 4*2+1, right is 4*2+2
        return 2 * pos + 1
  
    # Function to return the position of the right child for the node currently at pos 
    def rightChild(self, pos): 
        # For leftChild, we can determine if it has left child or not by checking
        # if the current node is a leaf or not
        # But for rightChild, we can't use the "node is leaf or not" to indicate it has right child or not
        # so we need another helper function hasRightChild to work with this rightChild function
        return (2 * pos) + 2
    
    def hasRightChild(self, pos):
        # this function is necessary because we are using array for heap
        # so rightChild(pos) may return gabage data for 2*pos+2
        if (2*pos+2) <= self.size-1:
            return True
        return False
  
    # Function that returns true if the passed node is a leaf node 
    def isLeaf(self, pos): 
        # if pos >= size//2, then it's a leaf 
        # check pos <= self.size is kindof redundant
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        # swap first pos and second pos
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
        """Make sure each node's val is less than its children
        Recusion is used
        """
        # If the node is a non-leaf node and greater than any of its child 
        if not self.isLeaf(pos): 
            if self.hasRightChild(pos):
                if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
                self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
    
                    # when node@pos > left or > right
                    # then swap it with the min of (left, right), then recursively call minHeapify(min(left,right))
                    if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                        # Swap with the left child and heapify the left child 
                        self.swap(pos, self.leftChild(pos)) 
                        self.minHeapify(self.leftChild(pos)) 
    
                    else: 
                        # Swap with the right child and heapify the right child 
                        self.swap(pos, self.rightChild(pos)) 
                        self.minHeapify(self.rightChild(pos)) 
            else:
                # if has no right child, and it's not a leaf node, then it must have a left child
                if self.Heap[pos] > self.Heap[self.leftChild(pos)]:
                    if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                        self.swap(pos, self.leftChild(pos)) 
                        self.minHeapify(self.leftChild(pos)) 

  
    # Function to insert a node into the heap 
    def insert(self, element): 
        """Insert a new node to heap
        Append the new node to the very end
        Then check if this node's value < its parent, if so, swap it
        Then set current to the parent node, and repeat
        """
        if self.size >= self.maxsize : 
            return
        # increase size by 1
        self.size+= 1
        # add the new element to the end
        self.Heap[self.size-1] = element 

        # set current as the last element
        current = self.size-1 
        # if current's val < current's parent value, we need to swap it with parent
        # then set current node as its parent node, and repeat
        # e.g 
        #      17                6
        #    /   \      ==>    /   \ 
        #   19    6           19   17 
        #  current=17        current=6
        # then check if 6 < 6's parent, because we don't know the new added element is the min or not
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        """Print heap
        Only print from root to the last non-leaf node
        A node may only have left child
        """
        for i in range(0, (self.size//2)): 
            # my mod: 
            if (2*i+2) <= self.size-1:
                print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                    str(self.Heap[2 * i + 1])+" RIGHT CHILD : "+
                                    str(self.Heap[2 * i + 2])) 
            else:
                print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                    str(self.Heap[2 * i + 1]))
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
        # minimize heap from non-leaf node
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum element from the heap 
    def remove(self): 
        # remove the root node
        # pop the first element, then move the last one to the first, re-heapify
        popped = self.Heap[self.FRONT] 
        print(self.Heap[self.size-1])
        self.Heap[self.FRONT] = self.Heap[self.size-1] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 

# ===========================================================================
class MinHeap: 
    # geeksforgeeks algorithm: https://www.geeksforgeeks.org/min-heap-in-python/
    # this one uses a dummy node saved to [0], so FRONT is set to 1
    # means heap starts from [1]
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize # or self.Heap[0] = float('-inf')
        # set the index of the top to 1 instead of 0
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 
if __name__ == "__main__": 
      
    print('The minHeap is ') 
    # first init heap with max_size=15
    minHeap = MinHeap_Mine(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(4) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    print("------before min heapify ------")
    minHeap.Print() 
    minHeap.minHeap() 
    print("------after min heapify ------")
    minHeap.Print() 
  
    print("The Min val is " + str(minHeap.remove())) 
    minHeap.Print() 
    print("The Min val is " + str(minHeap.remove())) 
    minHeap.Print() 