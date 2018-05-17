from timeit import Timer
from DataStructures import LinkedList, DoublyLinkedList

def LinkedListHead(n):
	LL = LinkedList()
	for i in range(0,n):
		LL.insert_head(i)

def LinkedListTail(n):
	LL = LinkedList()
	for i in range(0,n):
		LL.insert_tail(i)

def DoublyLinkedListHead(n):
	LL = DoublyLinkedList()
	for i in range(0,n):
		LL.insert_head(i)

def DoublyLinkedListTail(n):
	LL = DoublyLinkedList()
	for i in range(0,n):
		LL.insert_tail(i)

if __name__ == "__main__":
	print("Singly Linked List Head:")
	t = Timer("LinkedListHead(20)", "from __main__ import LinkedListHead")
	print('n=20: {}'.format(t.timeit(1000)))

	t = Timer("LinkedListHead(1000)", "from __main__ import LinkedListHead")
	print('n=100: {}'.format(t.timeit(1000)))

	print("Singly Linked List Tail:")
	t = Timer("LinkedListTail(20)", "from __main__ import LinkedListTail")
	print('n=20: {}'.format(t.timeit(1000)))

	t = Timer("LinkedListTail(1000)", "from __main__ import LinkedListTail")
	print('n=100: {}'.format(t.timeit(1000)))

	print("Doubly Linked List Head:")
	t = Timer("DoublyLinkedListHead(20)", "from __main__ import DoublyLinkedListHead")
	print('n=20: {}'.format(t.timeit(1000)))

	t = Timer("DoublyLinkedListHead(1000)", "from __main__ import DoublyLinkedListHead")
	print('n=100: {}'.format(t.timeit(1000)))

	print("Doubly Linked List Tail:")
	t = Timer("DoublyLinkedListTail(20)", "from __main__ import DoublyLinkedListTail")
	print('n=20: {}'.format(t.timeit(1000)))

	t = Timer("DoublyLinkedListTail(1000)", "from __main__ import DoublyLinkedListTail")
	print('n=100: {}'.format(t.timeit(1000)))