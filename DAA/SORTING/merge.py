def merge_sort(a, s, e):          # sort array from index s to e
    if s < e:                    # run only if more than 1 element
        m = (s+e)//2             # find middle index
        merge_sort(a, s, m)      # sort left part
        merge_sort(a, m+1, e)    # sort right part
        merge(a, s, m, e)        # merge both parts

def merge(a, s, m, e):
    L = a[s:m+1]                 # copy left half
    R = a[m+1:e+1]               # copy right half
    i = j = 0                   # pointers for L and R
    k = s                       # pointer for main array
    while i < len(L) and j < len(R):   # compare both halves
        if L[i] <= R[j]:         # pick smaller value
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1                  # move main pointer
    a[k:e+1] = L[i:] + R[j:]     # add remaining values  
    
# Take input from user
a = list(map(int, input("Enter numbers: ").split()))
# Apply merge sort
merge_sort(a, 0, len(a)-1)
# Print result
print("Sorted:", a)