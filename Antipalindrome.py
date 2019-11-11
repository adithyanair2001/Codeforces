a=input()
new=a
n=len(a)
flag=0
pp=0
for i in range(0, len(a)//2):
    if a[i] != a[len(a)-i-1]:
       flag=1
       break

string=a.replace(a[n-1],'',1)

for j in range(0, len(string)//2):
    if(string[j] != string[len(string)-j-1]):
        pp=2
        break

if(flag==1):
    print(len(a))
elif(pp==2):
    print(len(string))
else:
    if(flag!=1):
        print(0)



