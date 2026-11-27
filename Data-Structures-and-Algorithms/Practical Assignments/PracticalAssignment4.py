class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert node
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            temp = self.root

            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = Node(data)
                        break
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = Node(data)
                        break
                    temp = temp.right

    # Display in ascending order
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Find minimum
    def minimum(self):
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.data

    # Find maximum
    def maximum(self):
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp.data

    # Count scores above 50
    def count(self, root):
        if root is None:
            return 0

        return ((1 if root.data > 50 else 0)
                + self.count(root.left)
                + self.count(root.right))

    # Search score
    def search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # Calculate total
    def total(self, root):
        if root is None:
            return 0
        return (root.data + self.total(root.left)
                + self.total(root.right))


# Main program
bst = BST()

scores = [45, 78, 32, 89, 56, 92,
          67, 34, 85, 73, 61, 98]

for x in scores:
    bst.insert(x)

print("Ascending Order:")
bst.inorder(bst.root)

print("\nLowest:", bst.minimum())
print("Highest:", bst.maximum())
print("Above 50:", bst.count(bst.root))

key = int(input("Enter score to search: "))

if bst.search(bst.root, key):
    print("Score Found")
else:
    print("Score Not Found")

print("Average:", bst.total(bst.root) / len(scores))