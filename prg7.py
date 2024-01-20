arr=[5,2,8,7,10,23,56,78]
temp=0
print("Elements of original arry")
for i in range(0,len(arr)):
    print(arr[i],'\t',end="")
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("\nElements of array sortd in assending order")
for i in range(0,len(arr)):
    print(arr[i],'\t',end="")
print("\n5th maximum number is:",arr[len(arr)-5])
            
