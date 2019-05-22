## Each node IS a binary search tree. It has a left, a right, and a value.

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  ## Adds the input value to the BST
  def insert(self, value):

    # If new value is less than current value ( root )
    if value < self.value:
      # if there is no node on the left / an insertion point has been found
      if not self.left:
        # Create a new binary search tree with the value
        self.left = BinarySearchTree(value)
      # If there's already a node in that place
      else:
        # recursively call itself (insert) until it finds an empty leaf space/a spot to instantiate a new binary search tree
        self.left.insert(value)

    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  ## Searches the BST for the input value, returning a boolean indicating whether the value exists in the tree or not
  def contains(self, target):

    # If the current value doesn't exist, return False
    if self.value is None:
      return False

    # If the current value is equal to the target
    if self.value == target:
      print("True")
      return True

    # If target is less than the current value, move to the left
    elif target < self.value:

      # If the value is the target, return True
      if self.value == target:
        return True

      if self.left is None:
        return False
      
      # "Move" to the left, if there is a node there, by calling this function again, but this time calling it on the left node
      elif self.left is not None:
        # Search, comparing the target with the current value again -- recursion
        return self.left.contains(target)
      elif self.left is None:
        # If you can't move further left, return False
        return False

    # If target is greater than or equal to the current value, move to the right
    elif target >= self.value:

      # If the value is the target, return True
      if self.value == target:
        return True

      if self.right is None:
        return False

      # "Move" to the right, if there is a node there, by calling this function again, but this time, calling it on the right node
      elif self.right is not None:
        return self.right.contains(target)
      elif self.right is None:
        return False


  ## Returns the maximum value in the binary search tree
  def get_max(self):
    # # If current value is null, return None
    # if self.value is None:
    #   return None

    # If there is an element to the right
    if self.right:
      # go right and get_max
      self.right.get_max()

    # If you can't go right, you are at the largest element
    else:
      return self.value

  ## Performs a traversal of *every* node in the tree, executing the passed-in callback function on each tree node value.
  def for_each(self, cb):
    pass


newTree = BinarySearchTree(2)
newTree.insert(3)
newTree.insert(7)
newTree.contains(7)
newTree.contains(8)