import csv

file = 'contacts_sorted_fname.csv'

dataFrame = csv.reader(open(file , 'r'))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
q = input('searching for : ').lower()

for i in q :
    if i in numbers :
        search_for = 'number'
    else :
        search_for = 'letter'
        break

lst_answers = []
for lst in dataFrame :
    if lst[1] == 'first_name' :
        continue
    lst_answer = lst
    c = 0
    x = 0

    if search_for == 'number' :
        lst = lst[3].lower()
        for my_letter in q :
            if my_letter != lst[c] :
                break
            elif my_letter == lst[c] :
                x += 1
                if x == len(q) :
                    lst_answers.append(lst_answer)
            c += 1
    

    elif search_for == 'letter' :
        lst = lst[1].lower()
        for my_letter in q :
            if len(q) > len(lst) :
                break
            elif my_letter != lst[c] :
                break
            elif my_letter == lst[c] :
                x += 1
                if x == len(q) :
                    lst_answers.append(lst_answer)
            c += 1

for i in lst_answers :
    print(i)