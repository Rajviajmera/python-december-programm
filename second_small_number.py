def find_second_smallest_unique(arr):
    # Convert to a set to remove duplicates, then sort
    unique_sorted_arr = sorted(list(set(arr)))
    
    # Check if there are at least two unique elements
    if len(unique_sorted_arr) < 2:
        return "Array must have at least two unique elements"
    else:
        return unique_sorted_arr[1]

# Example usage:
arr1 = [0, 5, 8, 2, 1, 9, 2]
print(f"The second smallest unique element is: {find_second_smallest_unique(arr1)}") 
# Output: The second smallest unique element is: 2
