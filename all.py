#data type
"""
name="akash"
roll=25
marks=41.3
print("type",type(name))
print("type",type(roll))
print("type",type(marks))

# if 
no=int(input("enter the number:"))
if no>0:
	print("number is positve")
if no<0:
	print("Number is negitive:")
if no==0:
	print("number is zero")
	""


#if else:
n=int(input("enter a number:"))
if n>=10:
	print("number is 11 to unlimited")
else:
	print("number up to 9")
	""

# nested if

a=int(input("enter the number:"))
b=int(input("enter the second number:"))
c=int(input("Enter the third number:"))
if a>b:
	if a>c:
		print("largest",a)

if b>a:
	if b>c:
		print("largest",b)

if c>a:
	if c>b:
		print("largest",c)

""
#if else lader
a=int(input("Enter a number:"))
b=int(input("Enter two number:"))
c=int(input("Enter third number:"))
if ((a>b) and (a<c)):
	print("largest",a)
elif((b>c) and (b>c)):
	print("largest",b)
elif((c>a) and (c>b)):
	print("largest",c)
	""

  # DATA SCIENCE
import numpy as np

import matplot.pyplot as plt 
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.title("sine wave from")
plt.plot(x,y)
plt.show()
"""
# n=int//input("enter your name:")
# print(n)

#FOR
for x in range(1,11)
print(x)