import java.util.NoSuchElementException;

public interface ListInterface<E> {
    public void addFirst(E item);
    // public void addAfter(Node<E> curr, E data);
    // public void addLast(E data);
    public E removeFirst();
    // public E removeAfter(Node<E> curr);
    // public E removeLast();
    public int size();
    // public boolean contains(E item);
    public void print();
    // public boolean isEmpty();
    // public Node<E> getHead();
    // public Node<E> getFirst();
}
