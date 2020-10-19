n,s=input().split()
n,s=int(n),int(s)
k=s//n
q=s%n
if q!=0:
    c=k+1
else:
    c=k
print(c)
