# Chapter 2 Review Questions
Name: Scott Gordon
Course: 5143 Operating Systems
Date: 16 Feb 2016 

## What are three objectives of an OS design?
Convenience of use for the user, Efficient control for I/O and program execution, and the ability to evolve with changes in hardware and software. 

## What is the kernel of an OS?
It is the monitor and manages I/O requests, It executes in a privileged mode which has unfettered access to the system. It can access protected areas of memory and can execute privileged instructions which a typical user is not privy to. 

## What is multiprogramming?
Can also be referred to as multitasking. With sufficient memory to hold several programs, a multiprogrammed system can use the monitor to switch the use of the CPU among the different processes. A process may be switched out or into the processor for several reasons, such as I/O, or being interrupted by the OS or another program with a higher priority. Multiprogramming is the central theme of modern operating systems. 

## What is a process?
First defined by Multics users in the 1960's their are many definitions for the term process.
is can be defined as a program in execution or as an entity that can be assigned to and executed on a processor. Also, A unit of activity characterized by a single sequential thread of execution, a current state and an associated set of system resources. It is often used as a more general term of the word "Job"

## How is the execution context of a process used by the OS?


## List and briefly explain five storage management responsibilities of a typical OS.
Process isolation, meaning a program is not allowed to write to another program's memory. Dynamic memory allocation and management, meaning memory can grow and shrink as required by programs; Ideally this should be transparent to programmers and users alike. Support for modular programs or programs written which can grow or shrink dynamically. 

##Explain the distinction between a real address and a virtual address.
Virtual memory allows programs to address memory without knowledge of system resources. It was created to meet requirements of having multiple jobs reside in main memory concurrently, so that they can avoid the wait between secondary store while successive processes are written in and out from secondary storage. 

##Describe the round-robin scheduling technique.

##Explain the difference between a monolithic kernel and a microkernel.
A monolithic kernel provided all of what was considered OS functionality int very large kernels. these monolithic kernels contained scheduling functionality, networking, device drivers, memory management, and more. these monolithic kernels were typically implemented as one process. Today, Microkernel architecture designs have stripped the kernel down to its essentials, such as memory management, scheduling and inter-process communication. other OS services are provided using separate processes known as servers. this decoupled kernel and server development and allows for a high level of customization. 

##What is multithreading?
Is a technique which divides a process into smaller subunits which can be executed concurrently. this allows for much faster execution and also lends itself to use in a multicore environment 


##List the key design issues for an SMP operating system.
an SMP OS must provide all the functionality of a multiprogramming system plus additional features to accommodate simultaneous concurrent processes or threads, scheduling between multiple processors, (any of which may be currently executing or scheduleing) as well as dealing with memory management paging issues caused by multiple processes accessing shared memory, as well as stability requirements such as fault tolerance if their are issues. 