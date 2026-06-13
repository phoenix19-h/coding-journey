# Question 1
name= input("Enter Name :")
print(name)

# Question 2
num1= int(input(" Enter number 1:"))
num2= int(input(" Enter number 2:"))
choose=input("operator:")
if choose=='+':
    print(num1+num2)
if choose=='*':
    print(num1*num2)
if choose=='/':
    print(num1/num2)
if choose=='-':
    print(num1-num2)
    
# Question 3
numbers = [10,45,3,99,12]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print("The greatest number is", largest)
        