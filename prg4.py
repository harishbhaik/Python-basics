names=["josh","peter","tim"]
print("Current names list is:",names)
new_name=input("please enter a names:\n")
names.append(new_name)
print("Updated name list is:", names)

list1=[10,20,30,40,50]
print("Current numbers:",names)
el=list1.insert(3,77)
print("the new list is:",list)
n=int(input("enter a number to add to list:\n"))
index=int(input("enter the index to add the number :\n"))
list1.insert(index,n)
print("updated numbers list:",list1)

list1=[10,20,30]
list1.extend(["52.10","43.12"])
print(list1)
list1.extend((40,30))
print(list1)
list1.extend("aplle")
print(list1)
      
