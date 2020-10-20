x,y,a=map(int,input().split())
if x%a==0:
    i=x//a
else:
    i=(x//a)+1
 
if y%a==0:
    j=y//a
else:
    j=(y//a)+1
 
tiles=i*j
print(tiles)