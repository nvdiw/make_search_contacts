import csv

file = 'contacts.csv'
dataFrame = csv.reader(open(file , 'r'))
x = 1

# Function to compare 2 words
def is_alphabetically_smaller(str1, str2):
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
def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    arr3 = []
 
    i = 0
    j = 0
    while i < m and j < n:
        if is_alphabetically_smaller(arr1[i], arr2[j]):
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
def merge_sort(arr, lo, hi):
    if lo == hi:
        return [arr[lo]]
    mid = lo + (hi - lo) // 2
    arr1 = merge_sort(arr, lo, mid)
    arr2 = merge_sort(arr, mid + 1, hi)
 
    arr3 = merge(arr1, arr2)
    return arr3

# Driver code
def sort_by_merge(dataFrame) :
    arr = []
    for i in dataFrame :
        arr.append(i)
    n = len(arr)
    a = merge_sort(arr, 1, n - 1)
    for i in range(n - 1) :
        print(a[i])

sort_by_merge(dataFrame)