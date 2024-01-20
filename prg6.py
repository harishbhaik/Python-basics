def palindrome(a):
    mid=(len(a)-1)//2
    start=0
    last=len(a)-1
    flag=0
    reverse_String=""
    while(start<mid):
        if(a[start]==a[last]):
            start+=1
            last-=1
        else:
            flag=1
            break
    if(flag==0):
        print("the entered string is palindrome")
    else:
        reverse_String=a[::-1]
        print("the reversed string is:")
str=input("Enter a string:")
palindrome(str)
            
