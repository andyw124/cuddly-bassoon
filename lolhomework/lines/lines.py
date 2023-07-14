import sys

filess=list(sys.argv)

if(len(filess)<2):
    print("Too few command-line arguments")
    sys.exit(sys.exit)
elif(len(filess)>2):
    print("Too many command-line arguments")
    sys.exit(sys.exit)

try:
    with open(filess[1],"r") as file:
        if(filess[1].split(".")[-1]!="py"):
            print("Not a Python file")
            exit(sys.exit)
        else:
            textt=file.readlines()
            countt=0
            for i in textt:
                if len(i.lstrip())!=0 and i.lstrip()[0]!="#" and i.lstrip()[0]!="\"\"\"" and i.lstrip()[0]!="\'\'\'":
                    countt+=1
            print(countt)
            exit(0)
except FileNotFoundError:
    print("File does not exist")
    sys.exit(sys.exit)