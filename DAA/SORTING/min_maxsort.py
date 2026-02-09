def max_min_sort(arr):
    n = len(arr)
    for i in range(n):
        # assume current index has minimum value
        min_index = i
        # find the minimum element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap the found minimum with current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
# take input
numbers = list(map(int, input("Enter numbers: ").split()))
# sort using max-min logic
list = max_min_sort(numbers)
print("Sorted list:",list)