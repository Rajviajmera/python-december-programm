# Python Array
a = [1, "Hello", [3.14, "world"]]
a.append(2)  # Add an integer to the end
print("first list :",a)
print()

#import array
import array
b = array.array('i', [1, 2, 3, 1, 2, 5])
print("second list :",b)
print()
print("--------second list elements------")

# index of 1st occurrence of 2
print(b.index(2))

# index of 1st occurrence of 1
print(b.index(1))

# update item at index 2
b[2] = 6
print(b)

# update item at index 4
b[4] = 8
print(b)