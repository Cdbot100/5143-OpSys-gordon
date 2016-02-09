#!/bin/bash
#Scott Gordon 5143 Advanced Operating System Concepts
#This script takes a filename as its first argument and creates a dated copy of the file. 

day=$(date +'%Y-%m-%d')
#formatted day value
name=$(basename $1)
#basename of file without pathname
cp $1 ./$day$name
#copy from source to this directory, append date to the front of the file name
echo "Filename is:./"$day$name
#report name of file
