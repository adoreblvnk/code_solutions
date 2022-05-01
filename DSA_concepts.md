# Data Structure & Algorithms Cheat Sheet

Popular Data Structures & Algorithms. Useful for LeetCode, Competitive Programming, & understanding its concepts.

prod by blvnk.

Contents:

## Dynamic Arrays

Implementation: **List**

```py
my_list = [1, 2, 3, 4, 5]
# accessing elements
my_list[1] # 2
```

**Methods:** `append`, delete.

## Hash Table

Implementation: **Dictionary**

```py
my_dict = {'key1': 'value1', 'key2': 'value2'}
# accessing values
my_dict['key2'] # value2
```

**Methods:** insert, `get`, delete.

## Linked List

Implementation: **Singly Linked List**

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)


# singly linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        result = ""
        current = self.head
        while current:
            result += f"{str(current.data)} "
            current = current.next
        return result

    def __len__(self):
        return self.size

    def prepend(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, target):
        prev = None
        current = self.head
        while current:
            if current.data == target:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False
```

**Methods:** `prepend`, `delete`.

**Uses:** In Stacks & Queues, as they only need fast operations on the ends.