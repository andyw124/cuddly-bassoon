integer = int(input("Input: "))


def method(n):
    b=[]
    for i in range(n):
       b.append(i+1)
    return b

def fizzBuzz(n:list):
    for i in range(len(n)):
        if (i+1)%3==0:
            n[i]="Fizz"
        elif  (i+1)%5==0:
            n[i]="Buzz"
        else:
            n[i]=str(i+1)
    return n

print(fizzBuzz(method(integer)))
