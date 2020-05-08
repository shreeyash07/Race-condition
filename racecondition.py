import threading 
  
x = 0
  
def increment(): 

    global x 
    x += 1
  
def thread_task(): 

    for _ in range(100000): 
        increment() 
  
def main_task(): 
    global x 
    x = 0
  
    thread1 = threading.Thread(target=thread_task) 
    thread2 = threading.Thread(target=thread_task) 
  
    thread1.start() 
    thread2.start() 
  
    thread1.join() 
    thread2.join() 
  
if __name__ == "__main__": 
    for i in range(10): 
        main_task() 
        print("Iteration {0}: x = {1}".format(i,x)) 
