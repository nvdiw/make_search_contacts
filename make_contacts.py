import names
import random
import csv
import json

n = 10

# returns 'n' numbers id
def random_id(n) :
    lst_id = []
    for i in range(n) :
        id = random.randint(10000 , 20000)
        if id not in lst_id :
            lst_id.append(id)
    return lst_id

# returns 'n' numbers first name
def random_first_name(n) :
    lst_first_name = []
    for i in range(n):
        first_name = names.get_first_name()
        lst_first_name.append(first_name)
    return lst_first_name

# returns 'n' numbers last name
def random_last_name(n) :
    lst_last_name = []
    for i in range(n):
        last_name = names.get_last_name()
        lst_last_name.append(last_name)
    return lst_last_name

# returns 'n' numbers numbers
def random_number(n) :
    lst_first_numbers = [ 912, 919, 921, 930, 936, 911, 922, 900, 991, 990, 935, 937, 913 ]
    lst_numbers = []
    for i in range(n) :
        first_number = str(random.choice(lst_first_numbers))
        second_number = str(random.randint(1000000 , 9999999))
        main_number = '0' + first_number + second_number
        lst_numbers.append(main_number)
    return lst_numbers

# returns merge {'id' 'first_name' 'last_name' 'phone_number'}
def make_random_contacts(id , f_name , l_name , lst_number) :
    d_c = {}
    d_contacts = []
    for i in range(n) :
        d_c = {'id' : id[i] , 'f_name' : f_name[i] , 'l_name' : l_name[i] , 'number' : lst_number[i]}
        d_contacts.append(d_c)
    return d_contacts

def main() :
    id = random_id(n)
    f_name = random_first_name(n)
    l_name = random_last_name(n)
    lst_number = random_number(n)
    make_random_contacts(id , f_name , l_name , lst_number)

main()

# x = make_random_contacts(random_id(n) , random_first_name(n) , random_last_name(n) , random_number(n))
# for i in x :
#     print(i)