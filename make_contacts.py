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

def main() :
    print(make_id(n))

main()