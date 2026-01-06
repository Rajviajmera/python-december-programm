def are_equal_identity(a, b):
    # This checks if a and b are the exact same object in memory.
    return a is b

# Example Usage with Singletons (recommended use case for 'is'):
val1 = int(input("enter any value:"))
val2 = int(input("enter any value:"))
val3 = 10
val4 = 10 # Small integers are often cached, so 'is' works for them too in CPython

print(f"None and None are the same object: {are_equal_identity(val1, val2)}")
print(f"{val3} and {val4} are the same object: {are_equal_identity(val3, val4)}")

# Example with non-singletons (where 'is' might not work as expected):
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# They have the same value (list1 == list2 is True)
# but are different objects in memory.
print(f"list1 and list2 are the same object:{are_equal_identity(list1, list2)}")
