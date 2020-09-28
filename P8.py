a=[int(x) for x in input().split()]
a.sort()
n=len(a)
m=int(input())
diff=a[-1]
i=0
while(i<n-(m-1)):
    if(a[i+m-1]-a[i]<diff):
        diff=a[i+m-1]-a[i]
    else:
        diff=diff
        i=i+1
print(diff)    
