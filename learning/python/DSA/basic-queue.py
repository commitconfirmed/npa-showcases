#!/usr/bin/env python3
# deque can also be used for stacks, but we get O(1) speed with deque for front popping
from collections import deque
import time
import random

def main():
    class Queue():
        def __init__(self) -> None:
            self.queue = deque()
        
        def push(self, element: any) -> None:
            self.queue.append(element)

        def pop(self) -> list:
            if self.is_empty():
                raise IndexError("Queue is Empty")
            return self.queue.popleft()
        
        def peek(self) -> list:
            if self.is_empty():
                raise IndexError("queue is Empty")
            return self.queue[0]
        
        def is_empty(self) -> bool:
            return len(self.queue) == 0
        
        def length(self) -> int:
            return len(self.queue)
        
    myQueue = Queue()
    myQueue.push('A')
    myQueue.push('B')
    myQueue.push('C')
    print("queue: ", myQueue.queue)
    print("Pop: ", myQueue.pop())
    print("queue after Pop: ", myQueue.queue)
    print("Peek: ", myQueue.peek())
    print("isEmpty: ", myQueue.is_empty())
    print("Size: ", myQueue.length())

    # Let's see the speed difference
    bigStack = [random.randint(1, 10000000) for _ in range(1000000)]
    bigQueue = deque(random.randint(1, 10000000) for _ in range(1000000))
    stackStart = time.time()
    for _ in range(1000):
        bigStack.pop(0)
    stackEnd = time.time()
    print("Stack time taken:", stackEnd - stackStart)
    queueStart = time.time()
    for _ in range(1000):
        bigQueue.popleft()
    queueEnd = time.time()
    print("Queue time taken:", queueEnd - queueStart)


if __name__ == "__main__":
    main()

