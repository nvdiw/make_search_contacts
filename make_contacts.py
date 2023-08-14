import names
import random
import csv
import pandas as pd

n = 100

# returns 'n' numbers id
def random_id(n) :
    lst_id = []
    c = 10000
    for i in range(n) :
        c += 1
        id = c
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
        main_number = first_number + second_number
        lst_numbers.append(main_number)
    return lst_numbers

# returns merge {'id' 'first_name' 'last_name' 'phone_number'}
def make_random_contacts(id , f_name , l_name , lst_number) :
    lst_c = {}
    lst_contacts = []
    for i in range(n) :
        lst_c = [ id[i] , f_name[i] , l_name[i] , lst_number[i] ]
        lst_contacts.append(lst_c)
    return lst_contacts

# import to file.csv CSV
def import_contacts_file(title , persons) :
    with open ('contacts.csv' , 'w') as f :
        w = csv.writer(f ,lineterminator='\n' )
        w.writerow(title)
        w.writerows(persons)

# import sorted file as f_name
def sort_contacts_f_name(file) :
    # DataFrame to read our input CS file
    dataFrame = pd.read_csv(file)
    # sorting according to Car column
    dataFrame.sort_values("first_name", axis=0, ascending=True,inplace=True, na_position='first')
    dataFrame.to_csv('contacts_sorted_fname.csv', index=False)

def main() :
    id = random_id(n)
    f_name = random_first_name(n)
    l_name = random_last_name(n)
    numbers = random_number(n)
    title = ['id' , 'first_name' , 'last_name' , 'numbers']
    import_contacts_file(title , make_random_contacts(id , f_name , l_name , numbers))
    sort_contacts_f_name("contacts.csv")

main()

# x = make_random_contacts(random_id(n) , random_first_name(n) , random_last_name(n) , random_number(n))
# for i in x :
#     print(i)