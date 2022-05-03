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

**Methods:** `append()`, delete.

## Hash Table

Implementation: **Dictionary**

```py
my_dict = {'key1': 'value1', 'key2': 'value2'}
# accessing values
my_dict['key2'] # value2
```

**Methods:** insert, `get()`, delete.

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

**Methods:** `prepend()`, `delete()`.

**Uses:** In Stacks & Queues, as they only need fast operations on the ends.

## Stack

Implementation: **Stack**

```py
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __repr__(self):
        return repr(self.items)
```

**Methods:** `push()`, `pop()`, `peek()`.

**Uses:** Call Stack (tracks function calls), DFS (Depth First Search).

## Queue

Implementation: **Queue**

```py
from collections import deque


class Queue():
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def peek(self):
        return self.items[0]

    def __repr__(self):
        return repr(self.items)
```

**Methods:** `enqueue()`, `dequeue()`, `peek()`.

**Uses:** BFS (Breadth First Search), Printers (prints in order).

## Insertion Sort

```py
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr
```

**Uses:** Used for small lists. Time complexity of O(n^2).

## Merge Sort

```py
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half, right_half = arr[:mid], arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    if left_index < len(left):
        result.extend(left[left_index:])
    if right_index < len(right):
        result.extend(right[right_index:])
    return result
```

**Uses:** Used for large lists. Time complexity of O(n log n).


## Quick Sort

```py
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
```

**Uses**: Very fast for small lists. Low memory cost.