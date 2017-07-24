package np_core;

public class FullStackException extends RuntimeException{
    public FullStackException(){
        this("Stack is full");
    }

    public FullStackException(String message){
        super(message);
    }

}
