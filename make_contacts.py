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

# return 'n' numbers first name
def random_first_name(n) :
    lst_first_name = []
    for i in range(n):
        first_name = names.get_first_name()
        lst_first_name.append(first_name)
    return lst_first_name

# return 'n' numbers last name
def random_last_name(n) :
    lst_last_name = []
    for i in range(n):
        last_name = names.get_last_name()
        lst_last_name.append(last_name)
    return lst_last_name

# returns merge {'id' 'first_name' 'last_name' 'phone_number'}
def make_random_list(id , f_name , l_name) :
    d_c = {}
    d_contacts = []
    for i in range(n) :
        d_c = {'id' : id[i] , 'f_name' : f_name[i] , 'l_name' : l_name[i]}
        d_contacts.append(d_c)
    return d_contacts

def main() :
    id = random_id(n)
    f_name = random_first_name(n)
    l_name = random_last_name(n)
    make_random_list(id , f_name , l_name)

main()