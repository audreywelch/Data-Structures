"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  # Replaces the head of the list with the new value that is passed in
  def add_to_head(self, value):
    # Initialize a node with a value of the value passed in
    new_node = ListNode(value)

    # If the list is empty
    if not self.head and not self.tail: # if self.length == 0
      self.head = new_node
      self.tail = new_node

    # If the list has 2 or more items
    else:
      prev_head = self.head
      self.head = new_node
      self.head.next = prev_head

    # Increment our length
    self.length += 1

  # Removes the head node and returns the value stored in it
  def remove_from_head(self):
    # If the list is empty
    if not self.head and not self.tail: # self.length == 0
      return None

    # Increment the length
    self.length -= 1

    # If the list has one item
    if self.head == self.tail: # not self.head.next:
      # get a reference to the head
      current_head = self.head

      # delete the list head's reference & the tail's reference
      self.head = None
      self.tail = None

      # return the value
      return current_head.value

    # If the list has 2 or more items
    else:
      # get a reference to the head
      current_head = self.head

      # set the head to be what was previously next to the head
      self.head = self.head.next

      # set what was previously before the head to none
      self.head.prev = None

      # return the value
      return current_head.value

  # Replaces the tail of the list with a new value that is passed in
  def add_to_tail(self, value):
    # Initialize a node with a value of the value passed in
    new_node = ListNode(value)

    self.length += 1

    # If the list is empty
    if not self.tail and not self.head:
      self.head = new_node
      self.tail = new_node

    # If the list has 2 or more items
    else:
      prev_tail = self.tail
      self.tail = new_node
      self.tail.prev = prev_tail

  # Removes the tail node and returns the value stored in it
  def remove_from_tail(self):
    # If the list is empty
    if not self.head and not self.tail:
      return None

    self.length -= 1

    # If the list has one item
    if self.tail == self.tail:
      # get a reference to the tail
      current_tail = self.tail

      # delete the list's head reference
      self.head = None
      # delete the list's tail reference
      self.tail = None

      # return the value
      return current_tail.value

    # If the list has 2 or more items
    else:
      # get a reference to the tail
      current_tail = self.tail.value

      # set the tail to be what was previously before the tail
      self.tail = self.tail.prev

      # set what was previously next to the tail to None
      self.tail.next = None

      # return the value
      return current_tail.value

  # Takes a reference to a node in the list & moves it to the front
  # of the list, shifting all other nodes down
  def move_to_front(self, node):

    # If the node is already in the front
    if node is self.head:
      return

    node_value = node.value

    # If the node is currently the tail
    if node is self.tail:
      self.remove_from_tail()
    
    else:
      node.delete()
      self.length -= 1
    
    self.add_to_head(node_value)

  # Takes a reference to a node in the list and moves it to the end of the list,
  # shifting all other nodes up
  def move_to_end(self, node):

    # If the node is already at the end
    if node is self.tail:
      return

    value = node.value

    # If the node is currently the head
    if node is self.head:
      self.remove_from_head()
      self.add_to_tail(value)

    else:
      node.delete()
      self.length -= 1
      self.add_to_tail(value)

  # Takes a reference to a node in the list and removes it from the list.
  # The deleted node's `previous` and `next` pointers should point to each afterwards.
  def delete(self, node):
    
    self.length -= 1

    # If the list is empty
    if not self.head and not self.tail:
      return

    if self.head == self.tail:
      self.head = None
      self.tail = None
    
    elif self.head == node:
      self.head = node.next
      node.delete()

    elif self.tail == node:
      self.tail = node.prev
      node.delete()
    
    else:
      node.delete()
  
  # Returns the maximum value in the list
  def get_max(self):
    
    # If the list is empty
    if not self.head:
      return None

    max_val = self.head.value
    current = self.head

    # If the list has one or more items
    while current:
      if current.value > max_val:
        max_val = current.value
      current = current.next
      
    return max_val
