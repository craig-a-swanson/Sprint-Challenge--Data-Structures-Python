class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.buffer_list = []
        self.head = 0
        self.tail = 0

    def append(self, item):
        # appends the element to the tail
        # if the list isn't full, it adds the new tail and leaves the head alone
        # if the list is full:
            # it replaces the head with the value
            # the head moves "up" one
            # the tail becomes the new value
        if self.head == self.tail:
            self.buffer_list.append(item)
            self.tail = (self.tail + 1) % self.capacity
        elif len(self.buffer_list) < self.capacity:
            self.buffer_list.append(item)
            self.tail = (self.tail + 1) % self.capacity
            if self.tail == self.head:
                self.head += 1
        else:
            self.head = (self.head + 1) % self.capacity
            self.tail = (self.tail + 1) % self.capacity
            self.buffer_list[self.tail] = item

    def get(self):
        pass