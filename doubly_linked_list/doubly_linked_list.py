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
    pass

  # Removes the head node and returns the value stored in it
  def remove_from_head(self):
    pass

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
