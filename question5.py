class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self,head=None):
      self.head = head
      self.length = 1

    def append(self, new_element):   
        current = self.head
        if self.head:
            while current.next:
              current = current.next
              self.length += 1
            current.next = new_element
        else:
          self.head = new_element

def question5(ll,m):
    item = ll.head
    ll_length = 1
    while item.next:
        ll_length += 1
        item = item.next
    length = ll_length
    get_item = length - m
    item = ll.head
    if m <= length:
        for i in range(get_item):
            item = item.next
    else:
        return "Provided position is not in the list"
    return item.data

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e4)
ll.append(e3)

print question5(ll,2)
print question5(ll,3)
