package DataStructures;
import java.util.Iterator;

/**
 * 
 * LinkedList Implementation with O(1) insertion and deletion from front (optimized for LIFO Stack)
 *
 * @param <Type>
 */
public class LinkedList<Type> implements Iterable{
	
	private Node<Type> head;
	private int size = 0;
	
	private static class Node<Type>
	{
		private Type data;
		private Node next;
		public Node(Type data, Node<Type> next)
		{
			this.data = data;
			this.next = next;
		}
	}
	
	public LinkedList()
	{
		this.head = null;
	}
	
	/*
	 * Iterable implementation
	 * @see java.lang.Iterable#iterator()
	 */
	public Iterator iterator() {
		return new LinkedListIterator();
	}
	
	private class LinkedListIterator implements Iterator<Type>
	{
		private Node<Type> current = head;
		
		public boolean hasNext() {
			return current != null;
		}
		
		public Type next() {
			Type item = current.data;
			current = current.next;
			return item;
		}
		
	}
	
	public void insertHead(Type item)
	{
		/*
		 * Add to the front of the list 
		 * O(1)
		 */
		Node oldhead = this.head;
		this.head = new Node(item, oldhead);
		size ++;
	}
	
	public Node deleteHead(Type item)
	{
		/*
		 * Remove from front of the list
		 * O(1)
		 */
		if(head==null) throw new IndexOutOfBoundsException("List is empty"); 
		Node first = this.head;
		this.head = this.head.next;
		size--;
		return first;
	}
	
	public void insertTail(Type item)
	{
		/*
		 * Add to the end of the list. Have to traverse to the end starting from head
		 * O(n)
		 */
		if(head==null){
			insertHead(item);
			return;
		}
		
		Node tmp = head;
		while(tmp.next != null) tmp = tmp.next;
		tmp.next = new Node(item, null);
		size++;
	}
	
	public Node deleteTail(Type item)
	{
		/*
		 * Remove from the end of the list
		 * O(n)
		 */
		if(head==null) throw new IndexOutOfBoundsException("List is empty");
		
		Node tmp = head;
		Node prev = null;
		while(tmp.next != null) 
		{
			prev = tmp;
			tmp = tmp.next;
		}
		head = prev;
		size--;
		return tmp;
	}
	
	public int size()
	{
		return this.size;
	}
	
	public static void main(String[] args)
	{
		LinkedList<Integer> list = new LinkedList<Integer>();
		// populate list
		int i=0;
		while (i < 20)
		{
			list.insertTail(i);
			i++;
		}
		
		Iterator<String> iter = list.iterator();
		while(iter.hasNext())
		{
			System.out.println(String.valueOf(iter.next()));
		}
	}
	
}



