def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements larger than key to the right
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
# --- Interactive Part ---
# Get input from user, split by spaces, and convert to integers
user_input = input("Enter numbers separated by spaces: ")
data = [int(x) for x in user_input.split()]
insertion_sort(data)
print("Sorted Result:", data)