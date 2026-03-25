def max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    mid = (low + high) // 2

    max1, min1 = max_min(arr, low, mid)
    max2, min2 = max_min(arr, mid + 1, high)

    return max(max1, max2), min(min1, min2)


# Input (unsorted allowed)
arr = list(map(int, input("Enter elements: ").split()))

maximum, minimum = max_min(arr, 0, len(arr)-1)

print("Maximum value is:", maximum)
print("Minimum value is:", minimum)