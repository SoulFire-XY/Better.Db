import handler
def mode(path_saved):
    l = ["1","2","3","4","5","6"]
    print("Select the mode you want =>")
    print("1: read")
    print("2: read binary")
    print("3: write")
    print("4: write binary")
    print("5: append")
    print("6: append binary")
    n = input("Mode (no.): ")
    if  n in l:
        path_saved.write((n))
    else:
        print("invalid!")
        mode(handler.savedr)