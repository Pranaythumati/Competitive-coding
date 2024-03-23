class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def show(self):
        t=self.head
        while t:
            print(t.val,end="->")
            t=t.next
    def reverse(self,head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        self.head = prev
        return prev

    
obj=LinkedList() # object creation
obj.head=node(1)
obj.head.next=node(2)
obj.head.next.next=node(3)
obj.head.next.next.next=node(4)
obj.head.next.next.next.next=node(5)
obj.show()
obj.reverse(obj.head)
print("\n reversed string")
obj.show()
