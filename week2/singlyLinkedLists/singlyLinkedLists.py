class SLink():
    def __init__(self):
        self.head=None

    def add_to_front(self, val):
        newnode=SNode(val)
        newnode.next= self.head
        self.head=newnode
        return self

    def add_to_back(self, val):
        newnode=SNode(val)
        if self.checkListEmpty(False):
            self.head=newnode
        else:
            pointer=self.head
            while(pointer.next != None):
                pointer=pointer.next
            pointer.next=newnode
        return self

    def printValue(self):
        if not self.checkListEmpty(True):
            pointer=self.head
            print(self.head, pointer, pointer.next)
            while (pointer != None):
                print(pointer.value)
                pointer=pointer.next
        return self

    def remove_from_front(self):
        if not self.checkListEmpty(True):
            self.head=self.head.next
        return self

    def remove_from_back(self):
        if not self.checkListEmpty(True):
            pointer = self.head
            while (pointer.next.next != None):
                pointer=pointer.next
            pointer.next=None
        return self

    def remove_val(self, val):
        if not self.checkListEmpty(True):
            previous = self
            pointer=self.head
            while (pointer.value != val):
                previous = pointer
                if (pointer.next != None):
                    pointer = pointer.next
                else:
                    print("Unable to find Value")
                    return self
            if previous == self:
                self.head = None
            else:
                previous.next = pointer.next
        return self

    def insert_at(self, behind, val):
        if not self.checkListEmpty(False):
            newnode=SNode(val)
            pointer=self.head
            while (pointer.value != behind):
                if (pointer.next != None):
                    pointer = pointer.next
                else:
                    print("Unable to find Value")
                    return self
        newnode.next = pointer.next
        pointer.next = newnode
        return self

    def printValue(self):
        if not self.checkListEmpty(True):
            pointer=self.head
            while (pointer != None):
                print(pointer.value)
                pointer=pointer.next
        return self

    def checkListEmpty(self, printToConsole):
        if self.head == None:
            if printToConsole:
                print("List is empty")
            return True
        else:
            return False

class SNode():
    def __init__(self, val):
        self.value=val
        self.next=None

newlink=SLink()
newlink.printValue()
newlink.add_to_front("is").add_to_front("This").add_to_back("an").add_to_back("awesome").add_to_back("test").printValue()
newlink.remove_from_front().remove_from_back().printValue()
newlink.remove_val('awesome').printValue()
newlink.remove_val('aw').printValue()
newlink.insert_at('an', 'excellent').printValue()
