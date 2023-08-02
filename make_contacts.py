import names
import random
import csv
import json

n = 10

# returns 'n' numbers id
def make_id(n) :
    lst_id = []
    for i in range(n) :
        id = random.randint(10000 , 20000)
        if id not in lst_id :
            lst_id.append(id)
    return lst_id

# return 'n' numbers first name
def make_first_name(n) :
    lst_first_name = []
    for i in range(n):
        first_name = names.get_first_name()
        lst_first_name.append(first_name)
    return lst_first_name

# return 'n' numbers last name
def make_last_name(n) :
    lst_last_name = []
    for i in range(n):
        last_name = names.get_last_name()
        lst_last_name.append(last_name)
    return lst_last_name


def main() :
    print(make_id(n))
    print(make_first_name(n))
    print(make_last_name(n))
    
main()