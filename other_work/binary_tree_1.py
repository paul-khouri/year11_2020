class Node:

    def __init__(self, data):
        
        self.left = None
        self.right =None
        self.data = data

    def add_left(self, data):
        self.left = Node(data)
    def add_right(self, data):
        self.right = Node(data)


    def printTree(self):
        print(self.data)

root = Node(7)
root.add_left(3)

root.left.add_left(1)
root.left.add_right(5)
root.left.left.add_left(0)
root.left.left.add_right(2)
root.left.right.add_left(4)
root.left.right.add_right(6)

root.add_right(11)
root.right.add_left(9)
root.right.add_right(13)
root.right.left.add_left(8)
root.right.left.add_right(10)
root.right.right.add_left(12)
root.right.right.add_right(14)

chosen_item = root
chosen_item.printTree()
run_loop = True
while run_loop == True:
    my_input = input("Choose L or R:  ")
    if my_input == "L":
        chosen_item = chosen_item.left
    if my_input == "R":
        chosen_item = chosen_item.right
        
    chosen_item.printTree()
    
    if chosen_item.left is None:
        print("At the end")
        run_loop = False
print("Out of loop")
        
    
    


