import csv

file = 'contacts.csv'
dataFrame = csv.reader(open(file , 'r'))

# sorts items[x] about lst
def quick_sort(items , x=1):
    if len(items) > 1:
        p = items[0]
        pivot = items[0][x]
        left = [i for i in items[1:] if i[x] < pivot]
        right = [i for i in items[1:] if i[x] >= pivot]
        return quick_sort(left, x) + [p] + quick_sort(right, x)
    else:
        return items

arr = []
for i in dataFrame :
    arr.append(i)
arr.remove(arr[0])

for i in quick_sort(arr , 1):
    print(i)

