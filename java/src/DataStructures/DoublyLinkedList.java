package DataStructures;

/**
 * DoublyLinkedList
 * 		- achieves constant insertion/deletion from both ends of the list
 * 		- requires extra memory for "next" and "prev" Node pointers, 
 * as well as pointers to head and tail of the list
 *
 * @param <Type>
 */
public class DoublyLinkedList<Type> {
	
	private Node<Type> head;
	private Node<Type> tail;
	private int size = 0;
	
	private static class Node<Type>
	{
		private Type data;
		private Node next;
		private Node prev;
		public Node(Type data, Node<Type> next, Node<Type> prev)
		{
			this.data = data;
			this.next = next;
			this.prev = prev;
		}
	}
	
	public DoublyLinkedList(){
		head = null;
		tail = null;
	}
	
	public void insertHead(Type item)
	{
		/**
		 * Add to the front of the list 
		 * O(1)
		 */
		Node oldhead = this.head;
		this.head = new Node(item, oldhead, null);
		if(this.tail == null) this.tail = this.head;
		size ++;
	}
	
	public Node deleteHead(Type item)
	{
		/**
		 * Remove from front of the list
		 * O(1)
		 */
		if(head==null) throw new IndexOutOfBoundsException("List is empty"); 
		Node first = this.head;
		this.head = this.head.next;
		if(this.head == null)
			this.tail = null;
		else
			this.head.prev = null;
		
		size--;
		return first;
	}
	
	public void insertTail(Type item)
	{
		/**
		 * Add to the end of the list. Use tail pointer
		 * O(1)
		 */
		if(head==null){
			insertHead(item);
		}else{
			Node oldtail = this.tail;
			this.tail = new Node(item, null, oldtail);
			oldtail.next = this.tail;
			size++;
		}

	}
	
	public Node deleteTail(Type item)
	{
		/**
		 * Remove from the end of the list
		 * O(1)
		 */
		if(head==null) throw new IndexOutOfBoundsException("List is empty");
		
		Node last = this.tail;
		this.tail = last.prev;
		if(this.tail == null) 
			this.head = null;
		else 
			this.tail.next = null;
		size--;
		return last;
		
	}
	
	public int size()
	{
		return this.size;
	}
}
