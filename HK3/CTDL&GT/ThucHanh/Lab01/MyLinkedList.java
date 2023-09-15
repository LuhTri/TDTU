import java.util.NoSuchElementException;

public class MyLinkedList<E> implements ListInterface<E> {
    private Node<E> head;
    private int numNode;

    public MyLinkedList() {}

    public Node<E> getHead() {
        return this.head;
    }

    public int getNumNode() {
        return this.numNode;
    }

    public void setHead(Node<E> head) {
        this.head = head;
    }    

    public int size() {
        return this.numNode;
    }

    // public boolean contains(E item) {
    //     Node<E> tmp = head;
    //     while(tmp != null) {
    //         if (tmp.getData().equals(item)) {
    //             return true;
    //         }
    //         tmp.getNext();
    //     }

    //     return false;
    // }
    
    public void addFirst(E item) {
        head = new Node<E>(item, head);
        numNode++;
    }

    public void addAfter(Node<E> current, E item) throws NoSuchElementException {
        if (head == null) {
            throw new NoSuchElementException("Cannot add after");
        }

        Node<E> curr = head;

        for (Node<E> n = head.getNext(); n != null; n.getNext()) {
            if (curr.getData().equals(current.getData())) {
                curr.setNext(new Node<E>(item, curr.getNext()));

            }
            curr = n;

        }
    }
    
    public E removeFirst() throws NoSuchElementException {
        if (head == null) {
            throw new NoSuchElementException("List is empty!");
        }
        E tmp = head.getNext().getData();
        head = head.getNext();
        numNode--;
        return tmp;        
    }

    public void print() throws NoSuchElementException {
        if (head == null) {
            throw new NoSuchElementException("List is empty");
        }

        Node<E> n = head;
        System.out.print(n.getData());
        
        for (n = n.getNext(); n != null; n = n.getNext()) {
            System.out.print(" -> " + n.getData());
        }
        System.out.println();
    }

    
}