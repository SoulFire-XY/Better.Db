from os.path import exists

def action_path(act_path):
    status = exists(act_path)
    locsa = open('locs.txt', 'a+')
    locsw = open('locs.txt', 'w+')

    if status == False:
        print("File not Found: " + act_path + "\n Do you want to create a file with the same name as given in the path?")
        print("Either go to the module setting on handler.py and change file path or Create new db files")
        a = input()

        if a == "yes":
            file = open(f'dbs\\{act_path}', 'x')
            locsw.write(f'dbs\\{act_path} \n')
            file.close()
            bin = 'dbs\\' + act_path[:-4] + '.dat'
            file2 = open(bin, 'x')
            locsa.write(bin)
            file2.close()
            print("Creation Complete!")
        elif a == "no":
            n = input('Enter the path of the File (.txt): ')
            txt = f'dbs\\{n}'
            file = open(txt, 'x')
            locsw.write(f"{n} \n")
            file.close()
            n = input('Enter the path of the File(.dat): ')
            dat = f'dbs\\{n}'
            file = open(dat, 'x')
            locsa.write(dat)
            file.close()
            print("Creation Complete!")
        
    else:
        pass
