from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n)  # Create a new node
        if self.size == 0:  # if queue is empty
            self.head = new  # new node is head
            self.tail = new  # new node is tail
        else:  # If queue is not empty, add new after tail and update tail
            self.tail.nxt = new
            self.tail = new
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        if self.size == 0:  # If queue is empty, return  an empty set
            return "{ }"
        else:
            now = self.head
            result = "{ " + str(now.value)
            while now.nxt is not None:
                now = now.nxt
                result += " " + str(now.value)
            result += " }"
            return result

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n)
        if self.size == 0:  # If queue is empty
            self.head = new
            self.tail = new
        else:
            new.nxt = self.head  # add the new node before the head
            self.head = new  # update head
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.size == 0:  # Error message if queue is empty
            print("You can't access an empty queue")
            return None
        else:  # Otherwise return the tail
            return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        else:
            return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        else:
            value = self.head.value
            if self.size == 1:  # If thes size is 1, the queue becomes empty
                # because if we remove the head, the queue will be empty
                self.head = None
                self.tail = None
            else:
                self.head = self.head.nxt  # If we update the head to the
                # next head, the old head will be removed from the queue
            self.size -= 1  # we also delete it from the size
            return value

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        else:
            value = self.tail.value
            # If thes size is 1, the queue becomes empty
            # because if we remove the tail, the queue will be empty
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                now = self.head
                # It will iterate until the now's next element
                # is not the same as the tail
                while now.nxt is not self.tail:
                    now = now.nxt  # update now
                now.nxt = None  # Now is the last-1 element so it
                # will be removed
                self.tail = now  # Update tail
            self.size -= 1  # we also delete it from the size
            return value
