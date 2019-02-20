print("QUEUE IMPLEMENTATION")
queue=[]
while True:


    print("what you want to perform?\n 1.ENQUEUE 2.DEQUEUE 3.SIZE 4.EMPTINESS 5.EXIT")


    a=int(input())
    if a==1:
        print("enter the element you want to insert")
        l=input()
        queue.append(l)
        print("the elements in the queue are",queue)
    elif a==2:
        if queue==[]:
            print("the queue is empty")
        else:
            queue.pop(0)
            print("the elements in the queue are",queue)
    elif a==3:
        print("size of the queue is",len(queue))
        
    elif a==4:
        if queue==[]:
            print("empty")
        else:
            print("you have",len(queue),"elements in your queue")
    elif a==5:
        print("exit")
        break
