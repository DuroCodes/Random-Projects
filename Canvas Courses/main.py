import requests
from termcolor import colored as c
from prettytable import PrettyTable

url = "https://clevelandschools.instructure.com/api/v1/courses"
headers = {"Authorization": "Bearer 11631~M36BGoMGtgtRoxrjThHE8OlWGaCaUiZPjWAxdimHp7x9Pl7eh8OZJmAN3bBgB78f"}

r = requests.get(url, headers=headers).json()
t = PrettyTable(['Name', 'ID'])
t.align['Name'] = "l"
t.align['ID'] = "l"

for k in r: t.add_row([k.get("name","\033[91mNot Available\033[0m"), k["id"]])
print(t)