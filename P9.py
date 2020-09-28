a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
n=len(a)
i=0
j=0
count=1
while(i<n-1):
   if(a[i+1]<b[j]):
       count=count+1
       i=i+1
   else:
        i=i+1
        j=j+1
print(count)
