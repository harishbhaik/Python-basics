d=int(input("Enter number of days:"))
fine=0
if(d<=5):
    fine=d*0.50
    print("fine:",float(fine))
elif(d>5 and d<=10):
     i=d-5
     fine=(i*1)+(5*0.5)
     print("fine:",float(fine))
elif(d>10 and d<=30):
    i=d-10
    fine=(i*5)+(5*0.5)+(5*1)
    print("fine:",float(fine))
else:
    i=d-10
    fine=(i*5)+(5*0.5)+(5*1)
    print("your members is calcelled")
    print("fine:",float(fine))
                
                
