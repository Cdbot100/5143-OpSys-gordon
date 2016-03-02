# Chapter 3 Review Questions
Name: Scott Gordon
Course: 5143 Operating Systems
Date: 01 Mar, 2016

##3.4 What does it mean to preempt a process? 
is a process where the Operating system temporarily interrupts a running task, or moves it from a Running state to a Ready state in order to allow a task with a higher priority to execute. 


##3.5 What is swapping and what is its purpose? 
involves moving part or all of a process from main memory to disk. Because memory holds many running processes and I/O is much slower then computation, the CPU could potentially end up sitting idle. So, when none of the processes in main memory are in the ready state, the OS swaps one of the blocked processes out to disk. And brings in either a new process from the suspended queue or a new-process request.  


##3.9 List three general categories of information in a process control block. 
Process Identification: like the process ID, or the ID of parent processes (if any), also an identifier for the user. 

Processor State information: like control and status registers, the program counter, any condition codes, any status information, as well as Pointers for the stack

Process Control information: information needed by the OS for scheduling, like the current state of the process, its priority, any events the process may be waiting on, also any linking information for other processes, any handlers for interprocess communication, the privilege information pointers for memory management, also information about process ownership and a history of utilization 

##3.10 Why are two modes (user and kernel) needed? 
Mostly for security purposes. it prevents a user from interfering with other programs, it also allows software to take complete control of the processor and all of its instructions, registers, and memory. A typical user process does not need this type of control over the processor and for safety the OS handles this. 

##3.12 What is the difference between an interrupt and a trap? 
Both change the state of a process but; In a trap, an exception of error is raised and the OS attempts do determine if it is fatal for the execution of the process. If it is, the currently running process is moved to the exit state, or some recovery or procedure may be called. Unlike interrupts where processes are moved back to the ready state. 



##3.13 Give three examples of an interrupt. 

Hardware interrupt where a device requests the processor for example I/O devices, software interrupts which occur normally during execution, traps/exceptions also known as internal interrupts such as a divide by zero, or unknown opcode.  


##3.14 What is the difference between a mode switch and a process switch?
A process switch is when the processor switches from one thread/process to another; it could happen because of preemption. However a mode switch is when the cpu changes privilege levels. for example to execute kernel code which typically would be off limits to a user process. 
