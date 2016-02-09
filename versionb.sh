
#!/bin/bash
#Scott Gordon 5143 Advanced Operating System Concepts
#This script takes a filename as its first argument and creates a dated copy of the file. 

day=$(date +'%Y-%m-%d')
#formatted day value
name=$(basename $1)
file="${name%.*}"
ext="${name##*.}"
#basename of file without pathname
cp $1 ./$file$day.$ext
#copy from source to this directory, append date to the rear of the file name
echo "Filename is:./"$file$day.$ext
#report name of file


