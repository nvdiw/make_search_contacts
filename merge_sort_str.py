import csv

file = 'contacts.csv'
dataFrame = csv.reader(open(file , 'r'))

# Function to compare 2 words
def is_alphabetically_smaller(str1, str2, x):
    if type(str1) == list :
        str1 = str1[x]
    if type(str2) == list :
        str2 = str2[x]
        
    str1 = str1.upper()
    str2 = str2.upper()
    if str1 < str2:
        return True
    return False

# merge arrays
def merge(arr1, arr2, x):
    m = len(arr1)
    n = len(arr2)
    arr3 = []
 
    i = 0
    j = 0
    while i < m and j < n:
        if is_alphabetically_smaller(arr1[i], arr2[j], x):
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    while i < m:
        arr3.append(arr1[i])
        i += 1
    while j < n:
        arr3.append(arr2[j])
        j += 1
    return arr3

# Function to mergeSort 2 arrays
def merge_sort(arr, lo, hi, x):
    if lo == hi:
        return [arr[lo]]
    mid = lo + (hi - lo) // 2
    arr1 = merge_sort(arr, lo, mid, x)
    arr2 = merge_sort(arr, mid + 1, hi, x)
 
    arr3 = merge(arr1, arr2, x)
    return arr3

# Driver code
def sort_by_merge(dataFrame , x) :
    arr = []
    for i in dataFrame :
        arr.append(i)
    n = len(arr)
    lst = merge_sort(arr, 1, n - 1, x)
    for i in range(n - 1) :
        print(lst[i])

sort_by_merge(dataFrame , 2)