#Scott Gordon
#5143 Advanced Operating System Consepts 2016
#written for Python 2.7.10
#this program implements a simple shell
#special thanks to the following webpages
#http://stackoverflow.com/questions/11968976/list-files-in-only-the-current-directory
#https://docs.python.org/2/library/os.path.html

import os
import sys

#handles parsing of the input into pieces
class parserManager(object):
    #init function
    def __init__(self):
        self.parts = []
    
    #parse the line and split into parts
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        #self.findflags()
        return self.parts

    def findflags(self):
        for words in self.parts:
            if '-' in words:
                for letters in words:
                   if letters != '-':
                      self.flags += letters
 
#handles our commands and command history and desides what to run
class commandManager(parserManager):
    
    #init function
    def __init__(self):
        self.command = None
        self.command_history = []
    
    #add to history
    def push_command(self,cmd):
        self.command_history.append(cmd)
     
    #return history
    def get_commands(self):
        return self.command_history
     
    #total number of previous commands returns length of command history
    def number_commands(self):
        return len(self.command_history)
    
    #desides which command to run returns the command string
    def run_command(self,cmd):
        self.command = cmd
        self.flags = []
        self.command = self.parse(self.command)
        self.handler(cmd)        #Handle input
        return self.command
    
    #checks for valid input and handles it. returns nothing
    def handler(self,cmd):
        cmdlist = ["ls", "cat", "chmod", "cd", "history", "mv", "rm", "wc", "exit", "quit", "help"]
        if cmd:
            self.findflags()
            self.push_command(cmd)      #add cmd to history if its not an empty string     
            if self.parts[0] == "ls" :
                currentpath=os.getcwd()
                self.ls(currentpath)

            elif self.parts[0] == "cat":
                if len(self.parts) >1:
                    self.cat(self.parts[1])
                else:
                    print("Command 'cat' requires a file")

            elif self.parts[0] == "chmod":
                if len(self.parts) > 2:
                    self.chmod(self.parts[1],self.parts[2])
                else:
                    print("Command 'chmod' requires two arguments")
                
            elif self.parts[0] == "cd":
                if len(self.parts) >1:
                    self.cd(self.parts[1])
                else:
                    print("Command 'cd' requires a directory")

            elif self.parts[0] == "history":
                self.history()
            
            elif self.parts[0] == "mv":
                if len(self.parts) > 2:
                    self.mv(self.parts[1],self.parts[2])
                else:
                    print("Command 'mv' requires a two arguments")
            
            elif self.parts[0] == "rm":
                if len(self.parts) >1:
                    self.rm(self.parts[1])
                else:
                    print("Command 'rm' requires an argument")

            elif self.parts[0] == "wc":
                if len(self.parts) >1:
                    self.wc(self.parts[1])
                else:
                    print("Command 'wc' requires an argument")

            elif self.parts[0] == "exit":
                self.quit()

            elif self.parts[0] == "quit":
                self.quit()

            elif self.parts[0] == "help":
                print("...no")

            else:
                suggestions = []
                outmsg= "Unknown Command: '" + cmd +"'"
                if self.parts not in cmdlist:
                    for words in cmdlist:
                        for first in words[0]:
                            if self.parts[0][0] == first: 
                                suggestions.append(words)
                if suggestions:
                    outmsg+= "\nMaybe: "
                    for sug in suggestions:
                        outmsg+= str(sug) + " "
                print(outmsg)
        else:
            print "no input recieved!"

   #ls function
    def ls(self,dir):
        flaglist = ["l", "s", "a", "m", "c"]
        if self.flags:
            for letters in self.flags:
                if letters in flaglist:
                    print(letters)
                elif 'l' in self.flags:
                    print ("unknown flag", letters)     
        else:
            files = os.listdir(os.curdir)  #files and directories
            #files = filter(os.path.isfile, os.listdir( os.curdir ) )  # files only
            #files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ] #list comprehension version.        files = os.listdir(os.curdir)
            print(files)
    
    #cat Function
    def cat(self,file):
        try:
            f = open(file,'r')
            print(f.read())
        except IOError:
            outmsg= "Could not open file: '" + file +"'"
            print(outmsg)

    #chmod
    def chmod(self,file,perm):
        try:
            temp= perm.zfill(4)       #add leading 0
            temp= int(temp,8)         #cast to octal
        except ValueError:
            print("invalid octal value")
        try:
            os.chmod(file,temp)
            print("changed file permissions to " , perm) 
        except OSError:
            outmsg= "Could not change file: '" + file +"'"
            print(outmsg)
        
    #cd
    def cd(self,path):
        try:
            os.chdir(path)
        except OSError:
            outmsg= "No such file or directory: '" + path + "'"
            print(outmsg)

    #history
    def history(self):
        commandlist = self.get_commands()
        print(commandlist)

    #mv
    def mv(self,path1, path2):
        try:
            os.rename(path1, path2)
        except OSError:
            outmsg= "Problem moving file: '" + path1 + "' to '" + path2 + "'" + "\nPlease make sure your path is correct and your file doesn't already exist"
            print(outmsg)

    #rm
    def rm(self,file):
        try:
            os.remove(file)
        except OSError:
            outmsg= "Error removing file '" + file + "'"
            print(outmsg)
            return
        print("File removed")

    #wc
    def wc(self,file):
        os.system("wc -l " +file)    #fix this lol

    #print the exit message and quit, return nothing
    def quit(self):
        print ("Thanks for using YOshell v 0.1")
        sys.exit()

#driver module puts everything together
class driver(object):
    def __init__(self):
        self.commands = commandManager()

#basic looping structure of the CMD line
    def runShell(self):
        while True:
            try:
                currentpath = os.getcwd() + "/>"
                self.input = raw_input(currentpath)         # get command
                parts = self.commands.run_command(self.input)
            except KeyboardInterrupt:
                print("/n")
                self.commands.quit()

#main
if __name__=="__main__":
    d = driver()                                                #instance of our driver
    d.runShell()                                                #run
