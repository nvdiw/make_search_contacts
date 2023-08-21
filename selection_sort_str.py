import csv

file = 'contacts.csv'
dataFrame = csv.reader(open(file , 'r'))

def selection_sort(items , x=1):
    for i in range(len(items)):
        min_idx = i
        for j in range(i+1, len(items)):
            if items[min_idx][x] > items[j][x]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
    return items

arr = []
for i in dataFrame :
    arr.append(i)
arr.remove(arr[0])

selection_sort(arr , 2)

for i in arr :
    print(i)
