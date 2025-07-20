#!/usr/bin/env python3
def main():
    class Stack():
        def __init__(self) -> None:
            self.stack = []
        
        def push(self, element: any) -> None:
            self.stack.append(element)

        def pop(self) -> list:
            if self.is_empty():
                raise IndexError("Stack is Empty")
            return self.stack.pop()
        
        def peek(self) -> list:
            if self.is_empty():
                raise IndexError("Stack is Empty")
            return self.stack[-1]
        
        def is_empty(self) -> bool:
            return len(self.stack) == 0
        
        def length(self) -> int:
            return len(self.stack)
        
    myStack = Stack()
    myStack.push('A')
    myStack.push('B')
    myStack.push('C')
    print("Stack: ", myStack.stack)
    print("Pop: ", myStack.pop())
    print("Stack after Pop: ", myStack.stack)
    print("Peek: ", myStack.peek())
    print("isEmpty: ", myStack.is_empty())
    print("Size: ", myStack.length())

if __name__ == "__main__":
    main()

