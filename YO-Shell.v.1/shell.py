#Scott Gordon
#5143 Advanced Operating System Consepts 2016
#written for Python 2.7.10
#this program implements a simple shell capable of a few commands 
#special thanks to the following webpages
#http://stackoverflow.com/questions/11968976/list-files-in-only-the-current-directory
#https://docs.python.org/2/library/os.path.html
#http://stackoverflow.com/questions/2953828/accessing-relative-path-in-python

import os
import sys

#handles parsing of the input into pieces
class parserManager(object):
    #init function
    def __init__(self):
        self.parts = []                             #init parts as an empty list 
    
    #parse the line and split into parts
    def parse(self,cmd):                
        self.parts = cmd.split(" ")                 #split on spaces 
        return self.parts                           #return split list 

    def findflags(self):                            
        for words in self.parts:                    #check each word 
            if '-' in words:                        #if - exists in some word 
                for letters in words:               #for each letter in given word 
                   if letters != '-':               #excluding the hyphen 
                      self.flags += letters         #push letters into flag list 
 
#handles our commands and command history and desides what to run
class commandManager(parserManager):
    
    #init function
    def __init__(self):
        self.command = None                         #create instance of command
        self.command_history = []                   #init history list to empty 
    
    #add to history
    def push_command(self,cmd):                     
        self.command_history.append(cmd)            #add to history list 
     
    #return history
    def get_commands(self):
        return self.command_history                 #return history list 
     
    #total number of previous commands returns length of command history
    def number_commands(self):
        return len(self.command_history)            #return count of history 
    
    #desides which command to run returns the command string
    def run_command(self,cmd):
        self.command = cmd                          #the command = the user string
        self.flags = []                             #init flag list to empty every time 
        self.command = self.parse(self.command)     #parse the command 
        self.handler(cmd)                           #Handle input
        return self.command                         #return command string 
    
    #checks for valid input and handles it. returns nothing
    def handler(self,cmd):
        cmdlist = ["ls", "cat", "chmod", "cp", "cd", "history", "mv", "rm", "wc", "exit", "quit", "help"]
        if cmd:                                     #if cmd exists 
            self.findflags()                        #check for flags 
            self.push_command(cmd)                  #add cmd to history if its not an empty string     
            
            if self.parts[0] == "ls" :              #handler for ls  
                currentpath=os.getcwd()             #get current working directory's path 
                self.ls(currentpath)                #call ls with cwd 

            elif self.parts[0] == "cat":            #handler for cat 
                if len(self.parts) >1:              #if more then one argument 
                    self.cat(self.parts[1])         #try to cat 
                else:                               #handler for error 
                    print("Command 'cat' requires a file")

            elif self.parts[0] == "cp":             #handler for cp 
                if len(self.parts) > 2:             #if more then two arguments 
                    self.cp(self.parts[1], self.parts[2]) #try to cp 
                else:                               #handler for error 
                    print("Command 'cp' requires two arguments")

            elif self.parts[0] == "chmod":          #handler for chmod
                if len(self.parts) > 2:             #if more then two arguments 
                    self.chmod(self.parts[1],self.parts[2]) #try to chmod 
                else:                               #handler for error 
                    print("Command 'chmod' requires two arguments")
                
            elif self.parts[0] == "cd":             #handler for cd 
                if len(self.parts) >1:              #if more then one argument 
                    self.cd(self.parts[1])          #try to cd 
                else:                               #handler for error 
                    print("Command 'cd' requires a directory")

            elif self.parts[0] == "history":        #handler for history
                self.history()                      #call history 
            
            elif self.parts[0] == "mv":             #handler for mv 
                if len(self.parts) > 2:             #if more then two arguments 
                    self.mv(self.parts[1],self.parts[2])#try to mv 
                else:                               #handler for error 
                    print("Command 'mv' requires a two arguments")
            
            elif self.parts[0] == "rm":             #handler for rm
                if len(self.parts) >1:              #if more then one argument 
                    self.rm(self.parts[1])          #try to rm 
                else:                               #handler for error 
                    print("Command 'rm' requires an argument")

            elif self.parts[0] == "wc":             #handler for wc 
                if len(self.parts) >1:              #if more then one argument 
                    self.wc(self.parts[1])          #try to wc 
                else:                               #handler for error 
                    print("Command 'wc' requires an argument")

            elif self.parts[0] == "exit":           #exit handler 
                self.quit()

            elif self.parts[0] == "quit":           #quit handler 
                self.quit()

            elif self.parts[0] == "help":           #help handler 
                print("...no")

            else:                                   #unknown command, so 
                suggestions = []                    #suggestion list is blanked 
                outmsg= "Unknown Command: '" + cmd +"'"#let them know 
                if self.parts not in cmdlist:       
                    for words in cmdlist:           #for each word in command list 
                        for first in words[0]:      #check each first letter 
                            if self.parts[0][0] == first: #if it matches 
                                suggestions.append(words)   #add to list of suggestions 
                if suggestions:                     #if suggestions exist 
                    outmsg+= "\nMaybe: "            
                    for sug in suggestions:         #print each suggestion 
                        outmsg+= str(sug) + " "
                print(outmsg)
        else:
            print "no input recieved!"              #if no input, let them know! 

   #ls function
    def ls(self,dir):
        flaglist = ["l", "s", "a", "m", "c"]
        if self.flags:
            for letters in self.flags:
                if letters in flaglist:
                    print(letters)
                else: 
                    print ("unknown flag", letters)     
        else:
            files = os.listdir(os.curdir)  #files and directories
            #files = filter(os.path.isfile, os.listdir( os.curdir ) )  #only files 
            print(files)
    
    #cat Function
    def cat(self,file): 
        try:        
            f = open(file,'r')                      #attempt to open file 
            print(f.read())                         #dump contents to screen 
        except IOError:                             #handler for errors 
            outmsg= "Could not open file: '" + file +"'"#let them know it didnt work 
            print(outmsg)

    #chmod
    def chmod(self,perm,file):
        try:
            temp= perm.zfill(4)                     #add leading 0
            temp= int(temp,8)                       #cast to octal
        except ValueError:
            print("invalid octal value")
        try:
            os.chmod(file,temp)                     #chmod to correct octal value 
            print("changed file permissions to " , perm) #let them know it worked 
        except OSError:
            outmsg= "Could not change file: '" + file +"'"#let them know it didn't 
            print(outmsg)
        
    #cd
    def cd(self,path):
        if path[0] is '~':                          #check for '~' 
            try:
                os.chdir(os.path.expanduser(path))  #attempt to open correct directory beyond the home dir 
            except OSError:                         #handler for errors 
                outmsg= "No such file or directory: '" + path + "'"
                print(outmsg)                       #couldnt find file at /path/ 
        else:
            try:                                    
                os.chdir(path)                      #attempt to open correct directory     
            except OSError:                         #handler for errors 
                outmsg= "No such file or directory: '" + path + "'"
                print(outmsg)                       #couldnt find directory 

    #history
    def history(self):                              
        commandlist = self.get_commands()
        print(commandlist)
    
    #cp 
    def cp(self,file1,file2):
        return
    
    #mv
    def mv(self,path1, path2):
        try:                                        #attempt to rename file 
            os.rename(path1, path2)
        except OSError:                             #handler for problems 
            outmsg= "Problem moving file: '" + path1 + "' to '" + path2 + "'" + "\nPlease make sure your path is correct and your file doesn't already exist"
            print(outmsg)                           #print outmsg 
            return                                  #dont tell them file was renamed 
        outmsg= "file renamed"
        print(outmsg)                               #do tell them file was renamed 

    #rm
    def rm(self,file):
        try:
            os.remove(file)                         #attempt to remove file 
        except OSError:                             #handler for error 
            outmsg= "Error removing file '" + file + "'"
            print(outmsg)                           #print outmsg 
            return                                  #dont tell them the file was removed 
        print("File removed")                       #do tell them file was removed 

    #wc
    def wc(self,file):
        lines = 0                                   #set initial counts 
        count = 0
        chars = 0 
        flaglist = ["l"]                            #not many flags 
        try:
            with open(file, 'r') as f:              #open the file
                for line in f:                      #count by line
                    words = line.split()            #split based on ' '
                    lines+=1                        #counter for lines 
                    count += len(words)             #add the current line 
                    chars += len(line)              #add the number of chars in the line 
        except IOError:                             #Handler for errors 
            outmsg="No such file or directory: '" + file + "'"
            print(outmsg)
            return                                  #dont attmpt to count words in case of error
        if self.flags:
            for letters in self.flags:              
                if letters in flaglist:             #check for known flag 
                   outmsg = "Word count for file '" + file + "' is " + str(count) 
                   outmsg += "\nLine count is: " + str(lines)  #if -l print line count 
                else:                               
                    print ("unknown flag", letters) #handler for strange flag 
        else:  
            outmsg = "Word count for file '" + file + "' is " + str(count)
        print(outmsg)                               #print correct outmsg 
                    
    #print the exit message and quit, return nothing
    def quit(self):
        print ("Thanks for using YOshell v 0.1")   #friendly goodbye 
        sys.exit()                                 #stable exit 

#driver module puts everything together
class driver(object):                           
    def __init__(self):                                   
        self.commands = commandManager()            #create instace of commandManager 

#basic looping structure of the CMD line
    def runShell(self):         
        while True:                                 #always loop 
            try:
                currentpath = os.getcwd() + "/>"    #print current working directory folowed by an '>'
                self.input = raw_input(currentpath) # get command
                parts = self.commands.run_command(self.input)#attempt to run command
            except KeyboardInterrupt:               #handler for ^C 
                print("/n")                             
                self.commands.quit()                #call quit handler 

#main
if __name__=="__main__":
    d = driver()                                    #instance of our driver
    d.runShell()                                    #run
