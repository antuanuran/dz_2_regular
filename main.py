from create_csv import create_csv
from pprint import pprint
import csv

create_csv()



with open("phonebook_raw.csv") as f:
    rows = csv.reader(f)
    contacts_list = list(rows)
print(contacts_list)




