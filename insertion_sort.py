# lst = [['c','u'], ['d','t'], ['a','l'], ['b','m'], ['g','n'], ['e','o'], ['f','q'], ['j','p'], ['h','r'], ['i','s']]
import csv

file = 'contacts.csv'
dataFrame = csv.reader(open(file , 'r'))

# returns sorted list 'insertion_sort'
def insertion_sort(items , x = 1):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j-1][x] > items[j][x]:
            items[j-1], items[j] = items[j], items[j-1]
            j -= 1
    return items

# runs into main function
def main() :
    lst = []
    for i in dataFrame :
        lst.append(i)
    lst.remove(lst[0])

    for i in insertion_sort(lst, x = 1) :
        print(i)

main()