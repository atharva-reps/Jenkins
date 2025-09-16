class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        print(f"Pushed {element} into the stack")

    def pop(self):
        if not self.isempty():
            element = self.stack.pop()
            print(f"Popped {element} from the stack")
            return element
        else:
            print(f"Stack is empty")
            return None

    def peek(self):
        return len(self.stack)

    def isempty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack elements: ", self.stack)

stack = Stack()
stack.push(14)
stack.push(25)
stack.push(53)
stack.display()
print("Top element is ", stack.peek())
stack.pop()
stack.display()
print("Stack size is ", stack.size())
