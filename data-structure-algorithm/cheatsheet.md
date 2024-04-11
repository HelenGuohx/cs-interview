## Array

- clarify if there are duplicates in the array, how this would affect the answer

Brute force, iterate the elements in the list multiple times using for ... loops

Optimized way

Two pointers (sliding window). 
    Both two pointers starting from left. 
    One pointer starts from left, the other one starts from right

Binary search if the list is sorted or it can be sorted. Usually when interviewers ask about O(logn) time complexity. 

Precomputation if the quesitons involves summarization or multiplication 

## String

similar to array

counting charaters. create a hashmap to store the characters and its occurances. or using an arrya with length of 26


## Hash table

It is the most common optimization approach for any lookup that takes O(n)


## Recursion

Many algorithms adopt Recursion during implementation such as DFS, tree traversal, binary search, backtracking

code template
```
def recursion():
    # define a base case to stop recursion

    # call recursion on sub problems

```

Recursion implicitly uses stack. In other word, recurion can be rewritten in stack iteratively


Time complexity 
- Depends on the number of recursive calls 
- The work on each calls

For the Fibonacci problem, it takes O(2^n) 

Space Complexity

O(h), h is the height of the recursion tree, or the maximum depth of the stack

### Optimization

Memorization, using a list or a hash table to track the visited values. This will reduce the time complexity to be O(n)


## Stack
Stack follows "First in Last out". Some applications of stacks are recursion, DFS, browser history. 

Implementation 
```
# Method1: list, O(n) time complexity to append() and pop()
stack = []


stack.append(value) # add value
stack.pop() # pop the rightmost value in stack
len(stack)  # get stack size
stack[-1]   # get the rightmost value in stack 

#Method 2: deque, python built-in library, O(1) time complexity to append() and pop(). it is more efficient than List approach

from collections import deque

stack = deque()
stack.append(value)
stack.pop()
stack[-1] #get the last topmost value in the stack
```

**deque**: `deque` (pronouced as "deck") stands for double-ended queuem which designed for fast way to append and pop items from both end of the underlying data structure. Under the hood, it is implemented as a doubly linked list, which holds a pointer to the next and previous item in the sequence. The append and pop items takes O(1) in deque. However, accessing random values in deque takes O(n) time complexity. In this case, it would be better to use `list` instead of `deque` this in case. See [reference](https://realpython.com/python-deque/#popping-and-appending-items-efficiently)

## Queue
Queue follows "First in First out". Some applications of queue are Task scheduling, data transfer in network communication, BFS

Implementation
```
# Method 1: list,
queue = []
queue.append(value)
queue.pop(0)     # pop the leftmost value from queue
len(queue)       # get size of queue
queue[0]         # get leftmost value(first in) in queue


# method 2: deque

queue = deque()

queue.append(value)
queue.popleft()
len(queue)
queue[0]

# method 3: Queue
from queue import Queue
TBD
```


## Heap
Heap is a complete binary tree structure with specific ordering property. Heap is also an efficient way to implement PriorityQueue (priority matters in the queue). Common leetcode questions are finding the k largest/smallest values

**min-heap**: Every parent node has a value less than or equal to its children. The minimum value resides at the root, ideal for retrieving the smallest value O(1)

**max-heap**: Every parent node has a value greater than or equal to its children. The maximum value resides at the root, ideal for getting the largest value O(1)

Implementation

Sifting Up (for insertion): Starting from the inserted node, swap its position with its parent if the heap property is violated (e.g., for a min-heap, if the child is greater than the parent). This process continues until the heap property is satisfied.

Sifting Down (for removal): After removing the root element (which has the highest/lowest priority), replace it with the last element and then potentially swap it with its children (depending on the heap type) to restore the heap property.

```
# Method 1: binary tree


# Method2: heapq, Python built-in library
import heapq

# minheap
min_heap = []
heapq.heappush(min_heap, value) # insert value to heap
heapq.heappop(min_heap)         # remove topmost value from heap
len(min_heap)                   # check the size of heap


max_heap = []
heapq.heappush(max_heap, -value) # insert negative value to heap
-heapq.heappop(max_heap)         # remove topmost value from heap, don't forget to inverse the sign again 
len(max_heap)                    # check the size of heap
```


Note
complete binary tree: all level except the last level are fully filled with 2 children. Last level should have all nodes filled as far left as possible

BFS or DFS

if depth is limited, using DFS (implmented using recursion or stack iteratively)

if width is limited or looking for shorted path in a graph or tree, then BFS

