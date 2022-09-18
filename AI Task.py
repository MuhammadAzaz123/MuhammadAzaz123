#   Activity 1
for i in range(20):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print("Bingo !!")
        print("-----")
    else:
        pass

#   Activity 2
inp = input("Enter a Number to check if it is Even or Odd       :")
if int(inp) % 2 == 0:
    print("The Number  "+inp+"  is Even Number")
else:
    print("The Number  "+inp+"  is Odd Number")

#   Activity 3
sum= 0
n = int(input("Enter Any Integer    :"))

while n !=0:
    n = int(input("Enter Any Integer    :"))
    sum=sum+n

print("Sum of the Integers Is    :", sum)

#   Activity 4

isPrime = True
i = 2
n = int(input("Enter a Number   :"))
while i<n:
    rem = n%i
    if rem == 0:
        isPrime = False
        break
    else:
        i = i+1
if isPrime:
    print(n, " is a prime Number   ")
else:
    print(n, " is not a prime Number   ")




sum = 0
i = 1
while i<=5:
    s= int(input("Enter a  Number       :"))
    sum=sum+s
    i=i+1

print("Sum Of the Integers is  :", sum)


sum = 0
i =1
while i<=10:
    print(i)
    sum=sum+i
    i=i+1

print("--------")
print("Sum is ", sum)




#   Task 1
n = int(input("Enter the integer number: "))    
revs_number = 0  

while (n > 0):  
     
    remainder = n % 10  
    revs_number = (revs_number * 10) + remainder  
    n = n // 10  
  
  
print("The reverse number is : {}".format(revs_number))


#   Task 2
n=int(input("enter the values : "))
even=0
odd=0

for num in range(1,n+1):
    if(num%2==0):
        even=even+num
    else:
        odd=odd+num

print("sum of even numbers=",even)
print("sum of odd numbers=",odd)
    

#   Task 3      
n=int(input("enter the terms :"))
fe=0
se=1
if n<0:
    print("enter positive values")
else:
    print(fe,se,end="")
for x in range(2,n):
    next=fe+se
    print(next,end="")
    fe=se
    se=next


#   Task 4
marks=int(input("enter your marks="))
if marks<50:
    print("fail ")
elif marks>=50 and marks<=60:
    print("your grade is E")
elif marks>=61 and marks<=70:
    print("your grade is D")
elif marks>=71 and marks<=80:
    print("your grade is c")
elif marks>=81 and marks<=90:
    print("your grade is B")
elif marks>=91 and marks<=100:
    print("your grade is A")
else:
    print("invalid input")


#   Task 5
n=int(input("entr a number="))
fact=1
if n<0:
    print("please enter positive number")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial is=",fact)
          
      
            








