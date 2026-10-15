
# Linked List: All 4 Operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List (Append)
    def append(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    # 2. Traverse and Print Node Values
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert Node at a Specific Position
    def insert(self, data, pos):
        new = Node(data)

        if pos == 0:
            new.next = self.head
            self.head = new
            return

        temp = self.head

        for i in range(pos - 1):
            temp = temp.next

        new.next = temp.next
        temp.next = new

    # 4. Delete Alternate Nodes
    def deleteAlternate(self):
        temp = self.head

        while temp and temp.next:
            temp.next = temp.next.next
            temp = temp.next


# Create Linked List
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Original Linked List:")
ll.display()

# Insert 15 at position 1
ll.insert(15, 1)
print("After Insertion:")
ll.display()

# Delete Alternate Nodes
ll.deleteAlternate()
print("After Deleting Alternate Nodes:")
ll.display()
