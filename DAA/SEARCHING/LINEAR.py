# Linear Search with user input

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))
key = int(input("Enter element to search: "))
found = False
for i in range(n):
    if arr[i] == key:
        print("Element found at index:", i)
        found = True
        break
if not found:
    print("Element not found")