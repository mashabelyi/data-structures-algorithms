## Data Strtuctures ##

### Arrays ###

### Linked Lists ###
* Dynamic size - grows and shrinks on demand. Uses MEMORY proportional to size.
* But uses extra memory to store a reference to next node with each item.
* ACCESS O(n) in worst case.

Java has builtin [java.util.LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) implementation

|           |Access|Insertion|Deletion|Search| Space Complexity|
|------|------|------|------|------|------|
|Linked List|O(n)  | O(1)    | O(1)   | O(n) | O(n)            |

|         	|Implementation| Notes|
|-----------|--------------|------|
|java  		| [java.util.LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) | |
|python		| [list](https://docs.python.org/2/tutorial/datastructures.html)  | Efficient **Stack** implementation (LIFO). Use **append()** and pop() |
|python		| [deque](https://docs.python.org/3/library/collections.html#collections.deque)  | Efficient **Queue** implementation (LIFO). Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction. Use **append()**, **popleft()**, **popright()** |

### Doubly Linked Lists ###
* Achieves constant add/delete from tail time
* Requires more memory to keep a reference to the previous Node

### Stack ###
* Last-in-first-out (LIFO)
* Interface:
```
void 	push(key)	
Object 	pop()		
Boolean is_empty()		
```

|                         |Access|Insertion|Deletion|Search| Space Complexity|
|-------------------------|------|---------|--------|------|-----------------|
|LinkedList Implementation|O(n)  | O(1)    | O(1)   | O(n) | O(n), uses extra space for LinkedList Node pointers            |
|Array Implementation     |O(n)  | O(1)  - with fixed capacity   | O(1)   | O(n) | O(n), Either use a fixed capacity queue, or update the Array size dynamically |

|         	|Implementation| Notes|
|-----------|--------------|------|
|java       |[java.util.Deque](https://docs.oracle.com/javase/7/docs/api/java/util/Deque.html)|A linear collection that supports element insertion and removal at both ends. Preferred interface for both Queue and Stack applications.|
|python     | | |

### Queue ###
* First-in-first-out (FIFO)
* Interface:
```
void 	enqueue(key)	
Object 	dequeue()		
Boolean is_empty()		
```

|                         |Access|Insertion|Deletion|Search| Space Complexity|
|-------------------------|------|---------|--------|------|-----------------|
|LinkedList Implementation|O(n)  | O(1)    | O(1)   | O(n) | O(n), uses extra space for LinekdList Node pointers            |
|Array Implementation     |O(n)  | O(1)    | O(1)   | O(n) | O(n), MUST be a fixed capacity queue            |

|         	|Implementation| Notes|
|-----------|--------------|------|
|java       |[java.util.Deque](https://docs.oracle.com/javase/7/docs/api/java/util/Deque.html)|A linear collection that supports element insertion and removal at both ends. Preferred interface for both Queue and Stack applications.|
|python     | | |

## Algorithms ##

### Sort ###

|         	|Implementation| Notes|
|-----------|--------------|------|
|java  		| .sort()  | implements Quicksort |
|python		| .sort()  | Python uses an algorithm called Timsort: Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data.|