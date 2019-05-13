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
    new_node = ListNode(value, None, None)

    # If the list is empty
    if not self.head:
      self.head = new_node
      self.tail = new_node

    # If the list has one item - the head does not have a next
    elif not self.head.next:
      new_node.next = self.head
      self.head = new_node

    # If the list has 2 or more items
    else:
      prev_head = self.head
      self.head = new_node
      self.head.next = prev_head

  # Removes the head node and returns the value stored in it
  def remove_from_head(self):
    # If the list is empty
    if not self.head:
      return None

    # If the list has one item
    elif not self.head.next:

      # get a reference to the head
      head = self.head

      # delete the list head's reference
      self.head = None

      # delete the tail's reference
      self.tail = None

      # return the value
      return head

    # If the list has 2 or more items
    else:

      # get a reference to the head
      value = self.head

      # set the head to be what was previously next to the head
      self.head = self.head.next

      # return the value
      return value


  # Replaces the tail of the list with a new value that is passed in
  def add_to_tail(self, value):
    pass

  # Removes the tail node and returns the value stored in it
  def remove_from_tail(self):
    pass

  # Takes a reference to a node in the list & moves it to the front
  # of the list, shifting all other nodes down
  def move_to_front(self, node):
    pass

  # Takes a reference to a node in the list and moves it to the end of the list,
  # shifting all other nodes up
  def move_to_end(self, node):
    pass

  # Takesa  reference to a node in the list and removes it from the list.
  # The deleted node's `previous` and `next` pointers should point to each afterwards.
  def delete(self, node):
    pass
  
  # Returns the maximum value in the list
  def get_max(self):
    pass
