
arr=[10,20,30,45,7,3,4,59]

#1 Find maximum element in array
max=arr[0]
for i in arr:
    if i>max:
        max=i
print("The greatest number is",max)

#2Find minimum element
min=arr[0]
for j in arr:
    if j<min:
        min=j
print("The lowest number is",min)

#3 Reverse an array
reversed_arr=[]

for k in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[k])

print("Reversed array:", reversed_arr)

#4 Find sum of elements
total=0

for l in arr:
    total=total+l
print("Sum of elements:", total)