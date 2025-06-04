class ListNode:
    def __init__(self, val):
        self.val = val
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_element(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next= new_node
        
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" → ")
            current = current.next
        print("End")
            
my_list = LinkedList()
my_list.add_element(10)
my_list.add_element(20)
my_list.add_element(30)

my_list.print_list()
