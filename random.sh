#!/bin/bash
#Scott Gordon 5143 Advanced Operating System Consepts
#this script prints a random word. The file containing my words is local to this directory and is named words.txt

#sort --random-sort < ~/5143_Opsys/words.txt | head -n 1
#sort my word file randomly, print the first line
sort --random-sort </usr/share/dict/words | head -n 1
#sort words file randomly, print first line of file 
