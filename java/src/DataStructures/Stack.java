package DataStructures;
/**
 * Stack - LIFO queue
 * 		 - Linked List implementation
 * 		 - constant time push() and pop() methods
 * @author mashabelyi
 *
 * @param <Type>
 */

public class Stack<Type> {
	
	private Node head;
	private int size;
	
	/**
	 * Linked List Node implementation
	 *
	 * @param <Type>
	 */
	private static class Node<Type> {
		private Type data;
		private Node<Type> next;
		public Node(Type data, Node next) {
			this.data = data;
			this.next = next;
		}
	}
	
	public Stack() {
		this.size = 0;
		this.head = null;
	}
	
	/**
	 * push()
	 * 
	 * Insert at beginning of list 
	 * O(1)
	 * @param data - value to insert
	 */
	public void push(Type data) {
		if (isEmpty()) {
			this.head = new Node(data, null);
		}
		else {
			Node oldhead = this.head;
			this.head = new Node(data, oldhead);
		}
		size++;
	}
	
	/**
	 * pop()
	 * 
	 * Remove from beginning of list
	 * O(1)
	 * @return - removed Node
	 */
	public Node pop() {
		if (isEmpty()) {
			return null;
		}
		else {
			Node oldhead = this.head;
			this.head = this.head.next;
			size--;
			return oldhead;
		}
		
	}
	
	/**
	 * isEmpty()
	 * 
	 * @return
	 */
	public Boolean isEmpty() {
		return this.head == null;
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
		Stack<String> s = new Stack<String>();
		String input = "a b c d e f g h i j k l m n o p";
		for (String str: input.split(" ")) {
			s.push(str);
		}
		System.out.println(s);
		s.pop();
		s.pop();
		System.out.println(s);
		
	}
}
