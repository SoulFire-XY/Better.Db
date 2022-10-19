import linecache
import os
import options
import path
savedr = 'saved.txt'
def main():
    savedr = 'saved.txt'

    opt = open("saved.txt", 'r+')

    if os.stat(savedr).st_size == 0:

        saved = open("saved.txt", 'w+')
        options.mode(saved)

    else:
        read = opt.readlines()
        loc = open('locs.txt', 'r+')
        line = loc.readline()
        path.action_path(linecache.getline(r'locs.txt', 1))
        

        if read[0] == "1":
            os.startfile("options\\read.py")
        
        elif  read[0] == "2":
            os.startfile("options\\readbinary.py")
    
        elif  read[0] == "3":
            os.startfile("options\\write.py")

        elif  read[0] == "4":
            os.startfile("options\\writebinary.py")
    
        elif  read[0] == "5":
            os.startfile("options\\append.py")

        elif  read[0] == "6":
            os.startfile("options\\appendbinary.py")

        opt.write(" ")
        opt.close()