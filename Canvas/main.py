import requests
from prettytable import PrettyTable

# url = "https://clevelandschools.instructure.com/api/v1/courses"
# headers = {"Authorization": "Bearer 11631~M36BGoMGtgtRoxrjThHE8OlWGaCaUiZPjWAxdimHp7x9Pl7eh8OZJmAN3bBgB78f"}

# r = requests.get(url, headers=headers).json()
# t = PrettyTable(['Name', 'ID'])
# t.align['Name'] = "l"
# t.align['ID'] = "l"

# for k in r: t.add_row([k.get("name","\033[91mNot Available\033[0m"), k["id"]])
# print(t)

class_id = input("")
url = f"https://clevelandschools.instructure.com/api/v1/courses/{class_id}/assignments?per_page=100"
headers = {"Authorization": "Bearer 11631~M36BGoMGtgtRoxrjThHE8OlWGaCaUiZPjWAxdimHp7x9Pl7eh8OZJmAN3bBgB78f"}

r = requests.get(url, headers=headers).json()
t = PrettyTable(['Name', 'ID', 'Due Date'])
t.align['Name'] = "l"
t.align['ID'] = "l"
t.align['Due Date'] = "l"
t.sortby = 'Due Date'

for k in r: t.add_row([k.get("name","\033[91mNot Available\033[0m"), k["id"], k.get("due_at","\033[91mN/A\033[0m")[:10]])

print(t)