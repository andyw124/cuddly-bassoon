def loltwosearch(num,target):
    for i in range(len(num)):
        for j in range(1,len(num)):
            if (num[i]+num[j]<target):
                if(num[i]<=num[j] and i<len(num)-2):
                    i+=1
                elif(j<len(num)-2):
                    j+=1
                else:
                    break
            elif(num[i]+num[j]>target):
                if(num[i]<=num[j] and j<len(num)-2):
                    j+=1
                elif(i<len(num)-2):
                    i+=1
                else:
                    break
            elif(num[i]+num[j]==target and num[i]!=num[j]):
                return [i,j]
    return []

def threesearch(listtt):
    answer=[]
    for i in range(len(listtt)):
        temp=0-listtt[i]
        print(listtt[i])
        print(temp)
        list2=listtt.copy()
        list2.remove(listtt[i])
        templi=loltwosearch(list2,temp)
        print(templi)

        if(len(templi)==0):
            pass
        else:
            tempnw=[listtt[templi[0]],listtt[templi[1]]]
            temppp=[listtt[i]]
            temppp.extend(tempnw)
            answer.append(temppp)
    return answer

print(threesearch([-1,0,1,2,-1,-4]))