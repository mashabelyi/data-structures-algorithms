package DataStructures;

public class BinarySearchTree {
	
	public Node root;
	
	private static class Node {
		public int data;
		private Node left;
		private Node right;
		public Node(int data, Node left, Node right) {
			this.data = data;
			this.left = left;
			this.right = right;
		}
	}
	
	public BinarySearchTree() {
		this.root = null;
	}
	
	/**
	 * insert()
	 * O(log(n))
	 * 
	 * @param data - value to insert
	 */
	public void insert(int data) {
		root = insert(root, data);
	}
	
	public Node insert(Node n, int data) {
		if (n == null){
			n = new Node(data, null, null);
		}
		else {
			if (n.data > data) {
				n.left = insert(n.left, data);
			}
			else {
				n.right = insert(n.right, data);
			}
		}
		return n;
		
	}
	
	public void delete(int data) {
		
	}
	
	/**
	 * min(Node)
	 * Find smallest child node
	 * @param n
	 * @return
	 */
	public Node min(Node n) {
		if (n.left == null) return n;
		else return min(n.left);
	}
	
	/**
	 * max(Node)
	 * Find smallest child node
	 * @param n
	 * @return
	 */
	public Node max(Node n) {
		if (n.right == null) return n;
		else return max(n.left);
	}
	
	public void inOrder(Node n){
		if (n != null){
			inOrder(n.left);
			System.out.print(n.data + " ");
			inOrder(n.right);
		}
	}
	
	public void preOrder(Node n){
		if (n != null){
			System.out.print(n.data + " ");
			preOrder(n.left);
			preOrder(n.right);
		}
	}
	
	public void postOrder(Node n){
		if (n != null){
			postOrder(n.left);
			postOrder(n.right);
			System.out.print(n.data + " ");
		}
	}
	
	public static void main (String[] args) {
		BinarySearchTree bst = new BinarySearchTree();
		bst.insert(4);
		bst.insert(9);
		bst.insert(1);
		bst.insert(2);
		bst.insert(5);
		bst.insert(7);
		bst.insert(8);
		
		System.out.println("In-Order:");
		bst.inOrder(bst.root);
		System.out.println("\nPre-Order:");
		bst.preOrder(bst.root);
		System.out.println("\nPost-Order:");
		bst.postOrder(bst.root);
	}
}
