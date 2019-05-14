class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
  
  def dequeue(self):
    # If the queue is empty
    if not self.storage:
      return None

    removed_item = self.storage[0]

    self.storage.remove(self.storage[0])

    return removed_item

  def len(self):

    length = 0

    for each_element in self.storage:
      length += 1

    return length
