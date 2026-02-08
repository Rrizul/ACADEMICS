a = list(map(int, input("Enter sorted numbers: ").split()))  # a → sorted list
x = int(input("Enter element to search: "))                  # x → target value

l, r = 0, len(a) - 1     # l → left index, r → right index

while l <= r:
    m = (l + r) // 2    # m → middle index
    
    if a[m] == x:       # check if middle element is target
        print("Element found at index", m)
        break
    elif a[m] < x:      # target lies in right half
        l = m + 1
    else:               # target lies in left half
        r = m - 1
else:
    print("Element not found")