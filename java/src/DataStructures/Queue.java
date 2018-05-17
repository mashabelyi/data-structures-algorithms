package DataStructures;

/**
 * Queue - FIFO queue
 * 		 - Linked List implementation
 * 		 - constant time enqueue() and dequeue() methods
 *
 * @param <Type>
 */
public class Queue<Type> {
	
	private Node<Type> head;
	private Node<Type> tail;
	private int size;
	
	private class Node<Type> {
		private Type data;
		private Node next;
		public Node(Type data, Node next) {
			this.data = data;
			this.next = next;
		}
	}
	
	public Queue() {
		head = null;
		tail = null;
		size = 0;
	}
	
	/**
	 * enqueue(data)
	 * Insert item at the end of the list
	 * @param data
	 */
	public void enqueue(Type data) {
		if (isEmpty()) {
			this.head = new Node(data, null);
			this.tail = this.head;
		}
		else {
			Node oldtail = this.tail;
			this.tail = new Node(data, null);
			oldtail.next = tail;
		}
		size ++;
	}
	
	/**
	 * dequeue()
	 * Remove item from the beginning of the list
	 * @return Node
	 */
	public Node dequeue() {
		if(isEmpty()) return null;
		Node oldhead = this.head;
		this.head = oldhead.next;
		if(isEmpty()) this.tail = null;
		size--;
		return oldhead;
	}
	
	/**
	 * isEmpty()
	 * @return
	 */
	public Boolean isEmpty() {
		return head == null;
	}
	
	public String toString() {
		String[] toPrint = new String[size];
		Node tmp = this.head;
		int i = 0;
		while (tmp != null) {
			toPrint[i] = (String) tmp.data;
			tmp = tmp.next;
			i++;
		}
		return String.join(" ", toPrint);
	}
	
	public static void main(String[] args) {
		Queue<String> q = new Queue<String>();
		String input = "a b c d e f g h i j k l m n o p";
		for (String str: input.split(" ")) {
			q.enqueue(str);
		}
		System.out.println(q);
		q.dequeue();
		q.dequeue();
		System.out.println(q);
		
	}
	
}
