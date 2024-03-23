from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    key: Any = None         # node's position (it's unique)
    value: Any = None       # key-value pair
    left: Any = None
    right: Any = None

    # to make sure every Node is created with a key and value,
    # and with no left or right children
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    # Adds a key-value pair to the map, using the logic
    # left nodes are smaller, right nodes are larger
    def put(self, key, value):
        if key < self.key:
            # If there is no left child, create a new node
            if self.left is None:
                self.left = Node(key, value)
            else:
                # If there is, move to the left child and def put() again
                self.left.put(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.put(key, value)
        else:
            # Update value if it already exists to not have duplicates
            self.value = value

    # string representation of the BST, in-order traversal
    def to_string(self):
        striing = ""  # store
        # travel to the left substree and add to the string
        if self.left is not None:
            striing += self.left.to_string()
        striing += f"({self.key}, {self.value}), "  # current node
        # travel to the right substree and add to the string
        if self.right is not None:
            striing += self.right.to_string()
        return striing

    # total number of nodes
    def count(self):
        count = 1  # Because of the current node
        # travel to the left substree and count
        if self.left is not None:
            count += self.left.count()
        # travel to the right substree and count
        if self.right is not None:
            count += self.right.count()
        return count

    # it should return a value for a given key, or None if the key
    # doesn't exist
    def get(self, key):
        if key < self.key:
            if self.left is not None:
                return self.left.get(key)
            else:
                return None
        elif key > self.key:
            if self.right is not None:
                return self.right.get(key)
            else:
                return None
        else:
            # If key matches the current node's key return value
            return self.value

    # Longest root to leaf path
    def max_depth(self):
        if self is None:
            return 0

        # Depth of the left subtree
        if self.left is None:
            left_depth = 0
        else:
            left_depth = self.left.max_depth()

        # Depth of the right subtree
        if self.right is None:
            right_depth = 0
        else:
            right_depth = self.right.max_depth()

        return 1 + max(left_depth, right_depth)

    # (=nodes with at least one child)
    def count_internal_nodes(self):
        count = 0
        # See if the current node has at least one child + 1
        if self.left is not None or self.right is not None:
            count += 1
        # Travel to the left subtree and count internal nodes
        if self.left is not None:
            count += self.left.count_internal_nodes()
        # Travel to the right subtree and count internal nodes
        if self.right is not None:
            count += self.right.count_internal_nodes()
        return count

    # We do an in-order traversal of the tree to retrieve the key-value pairs
    # as a list, sorted by keys(words)
    def as_list(self, lst):
        if self.left is not None:
            self.left.as_list(lst)
        lst.append((self.key, self.value))
        if self.right is not None:
            self.right.as_list(lst)
        return lst


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
@dataclass
class BstMap:
    root: Node = None  # Bascially creates an empty tree

    # Adds a key-value pair to the map
    def put(self, key, value):
        # if empty create a new node
        if self.root is None:
            self.root = Node(key, value)
        else:
            # if it's not, call the put() func. from Node class
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:  # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns an internal node count. That is, the number of nodes
    # that has aleast one child (i.e. not leafs)
    def count_internal_nodes(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_internal_nodes()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
