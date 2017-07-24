package np_core;
/**
 * Created by oluwalekefakorede on 23/07/2017.
 */
public class Stack <E>{
    private final int size;
    private int top;
    private E[] elements;

    public Stack(){
        this(0);
    }
    public Stack(int s){
        size = s > 0 ? s : 0;
        top = size - 1;
        elements = (E[]) new Object[size];
    }
    public boolean isEmpty(){
        if(size ==0){
            return true;
        }
        else{
            return false;
        }
    }
    public void push(E value){
        if(top == size -1){
            throw new FullStackException(String.format("This satck is full, cannot push value : ",value));
        }
        else{
            elements[++top] = value;
        }
    }
    public E pop(){
        if(top == -1){
            throw new EmptyStackException("this stack is empty, cannot perform the operation pop");
        }
        else {
            return elements[top--];
        }
    }
}
