#!/usr/bin/env python3
def main():
    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList():
        def __init__(self):
            self.head = None

        def insert_front(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        
        def insert_back(self, data):
            new_node = Node(data)
            if not self.head: # Empty list
                self.head = new_node
                return
            # Traverse list until the end
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        def insert_index(self, data, index):
            new_node = Node(data)
            # Just do insert_front if first index
            if index == 0:
                new_node.next = self.head
                self.head = new_node
                return
            current_node = self.head
            # This is still O(n) complexity I believe
            for _ in range(index):
                if current_node is None:
                    break
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

        def traverse(self) -> list:
            current = self.head
            items = []
            while current:
                items.append(current.data)
                current = current.next
            return items

    ll = LinkedList()
    ll.insert_back('item 1')
    ll.insert_back('item 2')
    ll.insert_back('item 3')
    print("List: ", ll.traverse())


if __name__ == "__main__":
    main()

    def delete(self, key):
        """Delete the first node with the specified value."""
        current = self.head
        prev = None

        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def search(self, key):
        """Search for a node by value."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse(self):
        """Print all values in the list."""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements