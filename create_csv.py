import csv
import requests
import os


def create_csv():
    url = 'https://raw.githubusercontent.com/netology-code/py-homeworks-advanced/master/5.Regexp/phonebook_raw.csv'
    res = requests.get(url, allow_redirects=True)
    with open('sales_team.csv', 'wb') as file:
        file.write(res.content)


    list_all = []
    with open('sales_team.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            list_all.append(row)


    with open("phonebook_raw.csv", "w") as result:
        temp_write = csv.writer(result)
        temp_write.writerows(list_all)

    os.remove('sales_team.csv')



