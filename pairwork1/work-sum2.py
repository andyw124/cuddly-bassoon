
words=input("num: ")
targettt=input("target: ")
def reader(wordsss):
    return [int(a) for a in words if (a!="[" and a!="]" and a!="," and a!=" ")]

def loltwosearch(num,target):
    for i in range(len(num)):
        for j in range(1,len(num)):
            if (num[i]+num[j]<target):
                if(num[i]<=num[j]):
                    i+=1
                else:
                    j+=1
            elif(num[i]+num[j]>target):
                if(num[i]<=num[j]):
                    j+=1
                else:
                    i+=1
            else:
                return [i,j]

print(loltwosearch(reader(words),int(targettt)))
