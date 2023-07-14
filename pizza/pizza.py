import sys
from tabulate import tabulate as tb

filess=list(sys.argv)
if(len(filess)<2):
    print("Too few command-line arguments")
    sys.exit(sys.exit)
elif(len(filess)>2):
    print("Too many command-line arguments")
    sys.exit(sys.exit)
try:
    with open(filess[1],"r") as file:
        if(filess[1].split(".")[-1]!="csv"):
            print("Not a CSV file")
            exit(sys.exit)
        else:
            hallgp=[]
            for i in file:
                hallgp.append(i.lstrip().rstrip().split(","))
            print(tb(hallgp[1:], headers=hallgp[0], tablefmt="grid"))
            #asciart(hallgp)

except FileNotFoundError:
    print("File does not exist")
    sys.exit(sys.exit)

