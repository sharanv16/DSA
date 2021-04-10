class Node:
     def __init__(self,data_val):
         self.data_val=data_val
         self.next=None



class LinkedList:
    def __init__(self):
        self.head=None

    def insertStart(self,data_val):
        new_node = Node(data_val)
        if self.head is None:
            head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertEnd(self,data_val):
        new_node = Node(data_val)
        if self.head is None:
            head = new_node
        else:
            temp = self.head
            while temp.next:
                temp=temp.next

            temp.next=new_node

    def insertAfter(self,target,data_val):
        new_node=Node(data_val)
        temp=self.head
        while temp.data_val != target:
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node







    def printList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data_val)
                temp=temp.next


if __name__=="__main__":
    l=LinkedList()
    l.head=Node(4)
    first=Node(5)
    second=Node(6)
    l.head.next=first
    first.next=second
    l.printList()

    l.insertAfter(5,10)
    print("\n")
    l.printList()

