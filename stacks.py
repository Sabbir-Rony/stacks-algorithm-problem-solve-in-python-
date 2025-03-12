class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped {popped_item} from the stack.")
            return popped_item
        else:
            print("Stack is empty! Cannot pop an item.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty! No top element.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Top element is {stack.peek()}")
    print(f"Stack size is {stack.size()}")
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
