import threading
import time
import random
import os
    
def fun():
    print threading.currentThread().getName(),'Starting'
    time.sleep(random.randint(0,10))
    print threading.currentThread().getName(),'Exiting'
            
class threadManager(threading.Thread):
    
    def __init__(self):
        self.threads = [];
#- Method to **run all** threads being managed (that have not been run yet).  
#- Each thread will run the same function for ease of implementation right now.
    def runall(self):
        for th in self.threads:
            self.runthread(th.name)
#- Method to **run** a thread based on name, or id (once run, remove it from the class).
#- Each thread will run the same function for ease of implementation right now.
    def runthread(self, name):
        for th in self.threads:
            if name is th.name:
                th.start()
                #self.threads.remove(th)
#- Method to **add** a thread which will give it a name and id (then don't run it until explicitly invoked using name or id)
#- Each thread will run the same function for ease of implementation right now
    def addthread(self,th):
        self.threads.append(threading.Thread(target=fun, name=int(th)))

    @staticmethod
    def enumerate():
        return threading.enumerate()
        
if __name__ == '__main__':
    t = threadManager()
    for i in range (1,4):
        t.addthread(i)
    t.runall()
    
