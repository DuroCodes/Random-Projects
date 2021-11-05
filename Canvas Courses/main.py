from requests import get

url = "https://canvas.instructure.com/api/v1/courses"
headers = {"Authorization": "Bearer 11631~M36BGoMGtgtRoxrjThHE8OlWGaCaUiZPjWAxdimHp7x9Pl7eh8OZJmAN3bBgB78f"}

r = requests.get(url, headers=headers)
print(r)