# lst = [['c','u'], ['d','t'], ['a','l'], ['b','m'], ['g','n'], ['e','o'], ['f','q'], ['j','p'], ['h','r'], ['i','s']]
import csv

file = 'contacts.csv'
dataFrame = csv.reader(open(file , 'r'))

# returns sorted list 'bubble_sort'
def bubble_sort(lst , x = 0) :
    for i in range(len(lst)) :
        for j in range(len(lst)-1-i) :
            if lst[j][x] > lst[j+1][x] :
                lst[j][x], lst[j+1][x] = lst[j+1][x], lst[j][x]
    return lst

# runs into main function
def main() :
    lst = []
    for i in dataFrame :
        lst.append(i)
    lst.remove(lst[0])

    for i in bubble_sort(lst , 1) :
        print(i)

main()