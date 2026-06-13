# Time Complexity Practice


# O(1) - Constant Time
arr = [10, 20, 30, 40]

print("O(1) Example:")
print(arr[0])


# O(n) - Linear Time
print("\nO(n) Example:")

for i in arr:
    print(i)


# O(n^2) - Quadratic Time
print("\nO(n^2) Example:")

for i in arr:
    for j in arr:
        print(i, j)


# O(log n) - Logarithmic Time
print("\nO(log n) Example:")

number = 16

while number > 1:
    print(number)
    number = number // 2


# O(n log n) - Linearithmic Time
print("\nO(n log n) Example:")

n = 4

for i in range(n):
    j = n

    while j > 1:
        print(i, j)
        j = j // 2