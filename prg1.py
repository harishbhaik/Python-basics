#import comples math equation
import cmath
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
#calculate the discriminant
dis=(b**2)-(4*a*c)
if dis>0:
    print("the roots are real")
#find two results
else:
    print("the roots are img")
ans1=(b-cmath.sqrt(dis))/(2*a)
ans2=(b+cmath.sqrt(dis))/(2*a)
#print the results
print("the root are")
print(ans1)
print(ans2)
