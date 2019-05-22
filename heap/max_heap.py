class Heap:
  def __init__(self):
    self.storage = []

  # Adds the input value into the heap, ensuring that the inserted value is in the correct spot in the heap - Insert with bubbling up is a time complexity of: O(log n) b/c splitting everything in half and only working along one half
  def insert(self, value):
    # Insert the value into the last place in the array
    self.storage.append(value)
    length = self.get_size()

    # Call bubble_up() to check if it's parent is larger and then swapping if so
    self._bubble_up(length - 1)

  # Removes and returns the 'topmost' value from the heap, ensuring that the heap property is maintained after the topmost element has been removed
  def delete(self):
    # Save the value that was at the top in order to return it
    top_value = self.storage[0]

    # Remove the top value
    #self.storage.remove(top_value)
    self.storage[0] = 0

    # Get the length of the array in order to use it to refer to the last element
    length = self.get_size()

    # Put the last element in the array at the top / Replace root with the last leaf
    self.storage[0] = self.storage[length - 1]
    del(self.storage[-1]) # Remove the last element

    # Call sift_down() to check if either of its children nodes are larger, and swapping if so
    self._sift_down(0)

    return top_value

  # Returns the maximum value in the heap in constant time
  def get_max(self):
    return self.storage[0]

  # Returns the number of elements stored in the heap
  def get_size(self):

    # length = 0

    # for _ in self.storage:
    #   length += 1

    return len(self.storage)

  # Moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
  def _bubble_up(self, index):
    
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
    
    # Determine the end of the array
    end = self.get_size() - 1
    left_child_index = (index * 2) + 1

    # while child nodes exist - the index is less than the length of the array
    # if left is less than length
    while left_child_index <= end:

      # get the other child node of this index
      right_child_index = left_child_index + 1
      largest_child_index = left_child_index

      # determine largest of the children
      if right_child_index <= end and self.storage[right_child_index] > self.storage[left_child_index]:
        largest_child_index = right_child_index
      else:
        largest_child_index = left_child_index

      # check if the largest of the children is bigger than the array[index]
      if self.storage[largest_child_index] > self.storage[index]:
        # swap
        self.storage[largest_child_index], self.storage[index] = self.storage[index], self.storage[largest_child_index]

        # index becomes the child that was swapped with
        index = largest_child_index

        # Reset the left_child_index to accommodate for the new index 
        left_child_index = 2 * index + 1
      else:
        break



new_heap = Heap()
new_heap.insert(6)
new_heap.insert(8)
new_heap.insert(10)
new_heap.insert(9)
new_heap.insert(5)
new_heap.delete()
print(new_heap)
