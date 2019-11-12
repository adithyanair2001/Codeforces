a=list(map(int,input().split()))
c=0

for i in range(len(a)-1):
    if a[i]%2==0:
        c=c+1
        x=i

    else:
        b=b+1
        y=i 

if c==1:
    print(x)

else:
    print(y)   