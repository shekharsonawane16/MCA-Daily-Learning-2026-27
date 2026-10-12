#1. Create a Linked List in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

temp = n1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")


# 2. Traverse and Print the Node Values in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

temp = n1
while temp:
    print(temp.data)
    temp = temp.next


# 3.	Insert node at a specific position

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)

# data = int(input("Enter value: "))
# pos = int(input("Enter position: "))

# new = Node(data)

# if pos == 1:
#     new.next = head
#     head = new
# else:
#     temp = head
#     for i in range(pos - 2):
#         temp = temp.next
#     new.next = temp.next
#     temp.next = new

# temp = head
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")


# 4. Find the Middle Node and Print Its Value in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print("Middle node:", slow.data)


# 5. Delete a Node from a Linked List in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

pos = int(input("Enter position to delete: "))

if pos == 1:
    head = head.next
else:
    temp = head
    for i in range(pos - 2):
        temp = temp.next
    temp.next = temp.next.next

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")


# 6. Reverse a Linked List in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

prev = None
temp = head

while temp:
    next_node = temp.next
    temp.next = prev
    prev = temp
    temp = next_node

head = prev

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")


# 7. Calculate the Sum of Every Two Consecutive Node Values in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

temp = head

while temp and temp.next:
    print(temp.data + temp.next.data)
    temp = temp.next
