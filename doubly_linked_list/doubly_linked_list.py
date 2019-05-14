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
    new_node = ListNode(value, None, None)

    # If the list is empty
    if self.tail is None:
      self.head = new_node
      self.tail = new_node

    # If the list has one item
    elif not self.tail.prev:

      # set the current tail's next to the new node
      self.tail.next = new_node

      # set the list's tail as the new tail
      self.tail = new_node

    # If the list has 2 or more items
    else:
      prev_tail = self.tail
      self.tail = new_node
      self.tail.prev = prev_tail

  # Removes the tail node and returns the value stored in it
  def remove_from_tail(self):
    # If the list is empty
    if not self.tail:
      return None

    # If the list has one item
    elif not self.tail.prev:

      # get a reference to the tail
      tail = self.tail

      # delete the list's head reference
      self.head = None
      # delete the list's tail reference
      self.tail = None

      # return the value
      return tail.value

    # If the list has 2 or more items
    else:
      # get a reference to the tail
      value = self.tail.value

      # set the tail to be what was previously before the tail
      self.tail = self.tail.prev

      # return the value
      return value

  # Takes a reference to a node in the list & moves it to the front
  # of the list, shifting all other nodes down
  def move_to_front(self, node):
    
    # If the list is empty or has only one item, use the add_to_head() method
    if not self.head or not self.head.next:
      self.add_to_head(node)

    # Loop through each node in the list, checking if the value of current node is what I'm looking for
    # current = self.head
    # while current:
    #   if node == current.value:
    #     self.add_to_head(node)
    #   else:
    #     # update the current to be whatever the next is
    #     current = current.next

  # Takes a reference to a node in the list and moves it to the end of the list,
  # shifting all other nodes up
  def move_to_end(self, node):
    
    # If the list is empty or has only one item, use the add_to_tail() method
    if not self.tail or not self.tail.prev:
      self.add_to_tail(node)

    # Loop through each node in the list, checking if the value of the current node is what I'm looking for
    # current = self.head
    # while current:
    #   if node == current.value:
    #     self.add_to_tail(node)
    #   else:
    #     # update the current to be whatever the next is
    #     current = current.next

  # Takes a reference to a node in the list and removes it from the list.
  # The deleted node's `previous` and `next` pointers should point to each afterwards.
  def delete(self, node):
    
    # If the list is empty
    if not self.head:
      return

    # If the list has one or more items
    else:
      current = self.head
      while current:
        if node == current.value:
          self.delete(node)
        else:
          current = current.next
  
  # Returns the maximum value in the list
  def get_max(self):
    
    # If the list is empty
    if not self.head:
      return 0

    # If the list has one or more items
    else:
      max = self.head.value
      current = self.head
      while current:
        if current.value > max:
          max = current.value
        else:
          current = current.next
      
      return max
