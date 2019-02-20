print("STACK IMPLEMENTATION")
stack=[]
while True:


    print("what you want to perform?\n 1.INSERT 2.DELETE 3.SIZE 4.EMPTINESS 5.EXIT")


    a=int(input())
    if a==1:
        print("enter the element you want to insert")
        l=input()
        stack.append(l)
        print("the elements in the stack are",stack)
    elif a==2:
        if stack==[]:
            print("the stack is empty")
        else:
            stack.pop()
            print("the elements in the stack are",stack)
    elif a==3:
        print("size of the stack is",len(stack))
        
    elif a==4:
        if stack==[]:
            print("empty")
        else:
            print("you have",len(stack),"elements in your stack")
    elif a==5:
        print("exit")
        break
    
