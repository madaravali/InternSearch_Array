arr=[int(x) for x in input().split()]
arr.sort()
diff=int(input())
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[j]-arr[i]==diff):
            print("pair found")
            print(arr[i])
            print(arr[j])
            diff=0
if(diff!=0):print("not found")    
