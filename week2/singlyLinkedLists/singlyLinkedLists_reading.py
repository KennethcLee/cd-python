class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SNode(val)
        current_head=self.head
        self.head=new_node
        new_node.next=current_head
        return self

    def print_values(self):
        if self.head != None:
            pointer=self.head
            while (pointer != None):
                print(pointer.value)
                pointer=pointer.next
        else:
            print("Linked list empty")
        return self

    def add_to_back(self,val):
        new_node=SNode(val)
        if self.head != None:
            pointer=self.head
            while (pointer.next != None):
                pointer=pointer.next
            pointer.next=new_node
        else:
            self.head=new_node
        return self

class SNode:
    def __init__(self, val):
        self.value=val
        self.next=None

my_list=SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
