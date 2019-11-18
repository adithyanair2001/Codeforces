a=str(input())
t=0
zero=0
one=0

for i in range(len(a)-1):
    if a[i]=="1":
        one=one+1
        

    else:
        zero=zero+1
        

    if(one>=7 or zero>=7):
        t=1
        break

if t==1:
    print("YES")

else:
    print("NO")
