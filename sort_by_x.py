import csv

file = 'contacts.csv'
dataFrame = csv.reader(open(file , 'r'))
numbers = [str(i) for i in range(10)]
# input_q = input('searching for : ').lower()

# returns sorted contact list by " if :x = '1 = fn' , if: '2 = ln' , if: '3 = number'"
def sort_by_x(dataFrame , x) :
    persons = [person for person in dataFrame]
    p = 0
    d_fn = {}
    for person in persons[1:] :
        d = {p : person[x]}
        d_fn.update(d)
        p += 1
    a = sorted(d_fn.items(), key=lambda x: x[1])
    sorted_persons = []
    for i in a :
        num = i[0]
        sorted_persons.append(persons[num+1])
    return sorted_persons




# persons = [person for person in dataFrame]
# x = []
# for i in persons[1:] :
#     x.append(i[1])
# print(x)

# sort_by_x(dataFrame , 1)
for i in sort_by_x(dataFrame , 1) :
    print(i)