class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare it to the value we want to insert
        
        # new value < self.value
            # if self.left is already taken by a node
                # make that node call insert
            # set the left child to the new node with the new value
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        
        # if the new value >= self.value
            # if self.right is already taken by a node
                # make that node call insert
            # set the right child to the new node with new value
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        if self.value < target:
            if self.right is None:
                return False
            return self.right.contains(target)

        if self.value >= target:
            #check the left subtree
            if self.left is None:
                return False
            return self.left.contains(target)