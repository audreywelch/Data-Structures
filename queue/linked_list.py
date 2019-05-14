class Node:
    def __init__(self, value = None, next_node = None):
        # the value at this linked list Node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    # in adventure room we had methods on the rooms, on the nodes, and on the game itself
    # Method on the node would be like the room's method to view the items
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next_node):
        self.next_node = new_next_node

# Make a new class for the linked list
class LinkedList:
    def __init__(self):
        # Linked list has
        # Reference to the head of the list
        self.head = None
        # Reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # initialize a node with a value of value
        new_node = Node(value, None) # tail doesn't have a next_node, so it's going to be None

        # Check if there is no head(i.e. the list is empty)
        # if not self.head
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # We have a non-empty list, add the new node to the tail
        else:
            # Set current tail's next reference to the new node that we passed in, because we are adding to that tail
            self.tail.set_next(new_node)

            # The head's already pointing to the appropriate node, because we add it to the tail
            # Now we set the tail's current Next to that
            # The linked lists's tail itself needs to point to the new_node
            # Each node has a next, and the LIST has a tail
            # So we set it twice. Here we are saying, the linked list's tail
            self.tail = new_node

    # Remove the head
    def remove_head(self):

        # What if it's empty?
        # What if it has one thing?
        # What if it has two things or more?

        # If the linked list is empty, return none
        if not self.head:
            return None

        # If the linked list has only one value
        # How would we know? and what would we do about it?
        # if self.head == self.tail: # Wouldn't work if multiples of same values
        # OR
        if not self.head.get_next(): # this would point to None, meaning the head doesn't have a tail
            
            # get a reference to the head
            head = self.head
            
            # if the head has no next, then we havea  single element in our list
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None

            # return the value
            return head.get_value()

        # If the list has more than one element
        else:
            # return the value of the head that we just removed
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    def contains(self, value):
        # If the linked list is empty, return False
        if not self.head:
            return False
        else:
            current = self.head
            while current:
                # Travel throughout the linked list while checking if the value of the current node you're at, is the value that you're looking for
                if value == current.get_value():
                    return True
                else:
                    # update current to be whatever the next is
                    current = current.get_next()

            return False

    def add_to_head(self, value):
        # Initialize a node with a value of value
        new_node = Node(value, None)

        # If the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node

        # If the list has one item
        elif not self.head.get_next():
            new_node.set_next = self.head
            self.head = new_node

        # If th list has 2 or more items
        else:
            prev_head = self.head
            self.head = new_node
            self.head.set_next(prev_head)