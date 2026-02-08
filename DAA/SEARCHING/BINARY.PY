# STEP 1: Take a sorted list as input
a = list(map(int, input("Enter sorted numbers: ").split()))  # a → sorted list

# STEP 2: Take the element to be searched
x = int(input("Enter element to search: "))                  # x → target value

# STEP 3: Initialize left and right pointers
l, r = 0, len(a) - 1     # l → left index, r → right index

# STEP 4: Repeat until the search space is valid
while l <= r:
    m = (l + r) // 2    # STEP 5: Find middle index
    
    # STEP 6: Compare middle element with target
    if a[m] == x:
        print("Element found at index", m)
        break
    elif a[m] < x:      # STEP 7: Target is in right half
        l = m + 1
    else:               # STEP 8: Target is in left half
        r = m - 1
else:
    # STEP 9: Element not found after complete search
    print("Element not found")
    