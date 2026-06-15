# Day 2 - Arrays Basics


# Creating an array
numbers = [10, 20, 30, 40, 50]


# Accessing elements
print("First element:")
print(numbers[0])

print("Third element:")
print(numbers[2])


# Traversing an array
print("\nArray elements:")

for value in numbers:
    print(value)


# Length of array
print("\nLength:")
print(len(numbers))


# Updating value
numbers[1] = 100

print("\nAfter update:")
print(numbers)


# Adding element
numbers.append(60)

print("\nAfter adding:")
print(numbers)


# Removing element
numbers.remove(30)

print("\nAfter removing:")
print(numbers)
