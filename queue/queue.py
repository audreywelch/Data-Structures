from linked_list import LinkedList

class Queue:
  def __init__(self):
    # counter to keep track of the number of elements in our queue
    self.size = 0

    # what data structure should we
    # use to store queue elements? -> LinkedList implementation
    self.storage = LinkedList()

    # or
    # self.storage = []

  def enqueue(self, item):
    # add the item to the linked_list
    self.storage.add_to_tail(item)

    # increment our counter
    self.size += 1

    # or: self.storage.append(item)
  
  def dequeue(self):

    # Decrement our size counter
    if self.size > 0:
      self.size -= 1

    # Remove the head of the linked list and return it
    return self.storage.remove_head()

    # # If the queue is empty
    # if not self.storage:
    #   return None

    # removed_item = self.storage[0]

    # self.storage.remove(self.storage[0])

    # return removed_item

  def len(self):

    return self.size

    # length = 0

    # for each_element in self.storage:
    #   length += 1

    # return length
