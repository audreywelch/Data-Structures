class Heap:
  def __init__(self):
    self.storage = []

  # Adds the input value into the heap, ensuring that the inserted value is in the correct spot in the heap
  def insert(self, value):
    pass

  # Removes and returns the 'topmost' value from the heap, ensuring that the heap property is maintained after the topmost element has been removed
  def delete(self):
    pass

  # Returns the maximum value in the heap in constant time
  def get_max(self):
    return self.storage[0]

  # Returns the number of elements stored in the heap
  def get_size(self):

    count = 0

    for each_element in self.storage:
      count += 1

    return count

  # Moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
  def _bubble_up(self, index):
    pass

  # Grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent
  def _sift_down(self, index):
    pass

new_heap = Heap()