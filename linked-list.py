# 19 SEP 2019 -- Lenny Adams -- Linked List in Python

# Begin by creating a Node class.
class Node:
  
  # Initialize the Node class.
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node
