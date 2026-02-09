def partition(arr, start, end):
    pivot = arr[end]      # Take last element as pivot
    sp = start - 1        # Index of smaller elements
    for i in range(start, end):
        # If element is smaller than or equal to pivot
        if arr[i] <= pivot:
            sp += 1
            # Swap
            arr[sp], arr[i] = arr[i], arr[sp]
    # Place pivot at correct position
    arr[sp + 1], arr[end] = arr[end], arr[sp + 1]
    return sp + 1

def quick_sort(arr, start, end):
    if start < end:
        pivot_pos = partition(arr, start, end)
        # Sort left part
        quick_sort(arr, start, pivot_pos - 1)
        # Sort right part
        quick_sort(arr, pivot_pos + 1, end)
        
# -------- MAIN PROGRAM -------- #
arr = list(map(int, input("Enter integer values: ").split()))
print("Before Sorting:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("After Sorting :", arr)