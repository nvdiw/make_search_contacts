import csv

file = 'contacts_sorted_fname.csv'
dataFrame = csv.reader(open(file , 'r'))
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
input_q = input('searching for : ').lower()

# if number return number if letter return letter
def number_letter_comparison(input_q) :
    for i in input_q :
        if i in numbers :
            search_for = 'number'
        else :
            search_for = 'letter'
            break
    return search_for

# print lists
def print_lst(lst) :
    for i in lst :
        print(i)

# returns list of searched numbers
def search_number(input_q) :
    lst_answers = []
    for lst in dataFrame :
        if lst[1] == 'first_name' :
            continue
        lst_answer = lst
        lst = lst[3]
        c = 0
        x = 0
        for my_letter in input_q :
            if my_letter != lst[c] :
                break
            elif my_letter == lst[c] :
                x += 1
                if len(input_q) == x :
                    lst_answers.append(lst_answer)
            c += 1
    return lst_answers

# returns list of searched names
def search_name(input_q) :
    lst_answers = []
    for lst in dataFrame :
        if lst[1] == 'first_name' :
            continue
        lst_answer = lst
        lsts = [lst[1].lower() , lst[2].lower()]
        for lst in lsts :
            c = 0
            x = 0
            for my_letter in input_q :
                if my_letter != lst[c] :
                    break
                elif my_letter == lst[c] :
                    x += 1
                    if len(input_q) == x :
                        lst_answers.append(lst_answer)
                if c + 1 < len(input_q) :
                    c += 1
    return lst_answers



def main() :
    if number_letter_comparison(input_q) == 'number' :
        print_lst(search_number(input_q))
    if number_letter_comparison(input_q) == 'letter' :
        print_lst(search_name(input_q))

main()