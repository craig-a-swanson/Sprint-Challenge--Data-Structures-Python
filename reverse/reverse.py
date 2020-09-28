class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Itereate through the list and set each node to the head
        # set the node's set_next() to the previous node
        if self.head is None:
            return None
        if self.head.get_next() is None:
            return node.get_value()
        # change the direction of the pointers
        # the prev next should now be this node's next
        # this node's next will change to the prev node
        while node is not None:
            next_node = node.get_next()
            node.set_next(prev)
            node = next_node
        
            

