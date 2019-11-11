a=list(input())
b=list(input())
tot=a+b
c=list(input())
l=len(tot)

if(len(tot)==len(c)):
    count=0
    for i in c:
        if i in tot:
            count+=1
            tot.remove(i)

    if count == l:
        print("YES")

    else:
        print("NO")

else:
    print("NO")
            



                

    
