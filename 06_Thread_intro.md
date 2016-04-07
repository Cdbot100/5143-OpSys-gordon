Scott Gordon
M10226092
Thursday April 7th,

##Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.
Their is a global counter, called "sharedCounter" which is initially set to zero.(See line 10) The counter is updated inside of both threads every time a count is  by 10,000. (See lines 19-21 and 31-33 respectively) 

##After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?
Yes it does fix the problem of corrupted output by removing the race condition. The "downside" is that the code does not execute as quickly. 

##Comment out the join statements at the bottom of the program and describe what happens.
The main program ends during the beginning of the thread A & B 's lifecycle. It is several seconds of output after the main program is no longer executing and the threads still are. This is likely not what the programmer wanted from this program. 

##What happens if you try to Ctrl-C out of the program before it terminates?
The threads continue to run not releasing the IOstream. Because the main program has already terminated, control C is powerless. My shell is practially rendered useless

##Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.
for example when between the execution of line 21 and the separate execution of line 22 Thread A is getting interrupted so thread B can continue to run line 36. Therefore at the time of execution of line 22, the global sharedNumber == 2! thread A and B always print "that was weird" because they are constantly being interrupted by the other thread. Because there is no lock to protect the shared variable, its value is unknown at any given time during execution of the main program. 

##Does uncommenting the lock operations clear up the problem in question 5?
Yes, but the program itself doesn't do anything lol. 

