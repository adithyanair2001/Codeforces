a=input()
s1="aouie"
flag=0
        
for i in range(len(a)-1):
    if(a[i] not in s1 and a[i+1] not in s1 and a[i]!="n"):
        flag =1
        break

if(len(a)==1 and a[0]!="n" and a[0] not in s1):
    flag =1

if(a[len(a)-1] not in s1 and a[len(a)-1]!="n"):
    flag=1

if flag==1:
    print("NO")
else:
    print("YES")
