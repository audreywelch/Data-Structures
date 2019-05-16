class Heap:
  def __init__(self):
    self.storage = []

  # Adds the input value into the heap, ensuring that the inserted value is in the correct spot in the heap
  def insert(self, value):
    # Insert the value into the last place in the array
    self.storage.append(value)
    length = self.get_size()

    # Call bubble_up() to check if it's parent is larger and then swapping if so
    self.bubble_up(length - 1)

  # Removes and returns the 'topmost' value from the heap, ensuring that the heap property is maintained after the topmost element has been removed
  def delete(self):
    pass

  # Returns the maximum value in the heap in constant time
  def get_max(self):
    return self.storage[0]

  # Returns the number of elements stored in the heap
  def get_size(self):

    length = 0

    for _ in self.storage:
      length += 1

    return length

  # Moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
  def bubble_up(self, index):
    
    while index > 0:
      # get the parent element of this index
      parent = (index - 1) // 2

      # check if the current index element is higher priority (larger) than its parent element
      if self.storage[index] > self.storage[parent]:
        # If yes, swap
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

        # "Move up" by setting the new index to what was the parent
        index = parent
      else:
        break

  # Grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent
  def _sift_down(self, index):
    pass

new_heap = Heap()
new_heap.insert(6)
new_heap.insert(8)
new_heap.insert(10)
new_heap.insert(9)
new_heap.insert(1)
new_heap.insert(9)
new_heap.insert(9)
new_heap.insert(5) 
print(new_heap)