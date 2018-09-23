### LINKED LIST IMPLEMENTATION IN PYTHON 3.7###
#__________________________________

### CLASSES ###

# NODE #
class Node():
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
  
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node


# LINKED LIST #
class LinkedList():
  def __init__(self, value=None):
    self.head_node = Node(value)
    
  def get_head_node(self):
    return self.head_node
    
  def insert_beginning(self, new_value):
    #instantiate new node
    new_node = Node(new_value)
    #use set_next_node link it to the current head
    new_node.set_next_node(self.head_node)
    #set head_node to this new node that is now the head
    self.head_node = new_node
    
  def stringify_list(self):
    outputString = ""
    while True:
      outputString += str(self.head_node.get_value())
      outputString +=  "\n"
      if self.head_node.get_next_node() == None:
        break
        return outputString
      else:
        nextNode = self.head_node.get_next_node()
        outputString += str(nextNode.get_value())
        outputString +=  "\n"
      return outputString
      break
      
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.next_node = next_node.get_next_node()
          current_node = None
        else:
          current_node = next_node
          
# Instantiate a Node. #
#my_node = Node(44)

# Print a Node's value. #
#print(my_node.get_value())

# Instatiate multiple Nodes #
#yacko = Node("likes to yak")

#wacko = Node("has a penchant for hoarding snacks")

#dot = Node("enjoys spending time in movie lots")

#Link yacko -> dot
#yacko.set_link_node(dot)

#Link dot -> wacko
#dot.set_link_node(wacko)

# Return dot's data using yacko. #
### Yacko's get_link_node returns dot. #
###### Converts to dot.get_value() which returns dots value. #
#dots_data = yacko.get_link_node().get_value()
#wackos_data = dot.get_link_node().get_value()

# Print out both. #
#print(dots_data)
#print(wackos_data)


# Test your code by uncommenting the statements below - did your list print to the terminal?
#testLL = LinkedList(5)
#testLL.insert_beginning(70)
#testLL.insert_beginning(5675)
#testLL.insert_beginning(90)
#print(ll.stringify_list())