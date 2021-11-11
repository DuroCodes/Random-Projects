import json, requests
from os import system
from datetime import datetime
from prettytable import PrettyTable

try:
  secret = open("secret.json")
  tokens = json.load(secret)
  secret.close()

  access_token = tokens["access_token"]
  school_code = tokens["school_code"]

  headers = {"Authorization": f"Bearer {access_token}"}
  canvas_link = f"https://{school_code}.instructure.com/api/v1/courses"
  check_date = datetime(day=datetime.now().day-5, month=datetime.now().month, year=datetime.now().year)

  class s:
    bl = '\033[30m'
    r = '\033[31m'
    g = '\033[32m'
    y = '\033[33m'
    b = '\033[34m'
    m = '\033[35m'
    c = '\033[36m'
    w = '\033[37m'
    u = '\033[4m'
    re = '\033[0m'

  def CheckCourses():
    print(s.re)
    url = f"{canvas_link}?per_page=100"
    r = requests.get(url, headers=headers).json()

    t = PrettyTable([f'{s.g}Name{s.re}', f'{s.y}ID{s.re}'])
    t.align = "l"
    t.sortby = f'{s.y}ID{s.re}'

    for k in r: t.add_row([f'{s.g}{k.get("name",f"{s.r}Not Available")}{s.re}', f'{s.y}{k["id"]}{s.re}']) 
    print(t)

  def CheckAssignments(class_id):
    print(s.re)
    url = f"{canvas_link}/{str(class_id)}/assignments?per_page=100"
    r = requests.get(url, headers=headers).json()

    t = PrettyTable([f'{s.g}Name{s.re}', f'{s.y}ID{s.re}', f'{s.b}Due Date{s.re}'])
    t.align = "l"
    t.sortby = f'{s.b}Due Date{s.re}'

    for k in r: 
      due_time = k.get("due_at",f"{s.r}1969-01-01")
      if due_time is None: due_time = f"1969-01-01"
      due_date = datetime.strptime(due_time[:10], "%Y-%m-%d")
      if due_date >= check_date: t.add_row([f'{s.g}{k["name"]}{s.re}', f'{s.y}{k["id"]}{s.re}', f'{s.b}{k.get("due_at",f"{s.r}N/A")[:10]}{s.re}'+s.re])
    print(t)
  def CheckModules(class_id):
    print(s.re)
    url = f"{canvas_link}/{str(class_id)}/modules"
    r = requests.get(url, headers=headers).json()

    t = PrettyTable([f'{s.g}Name{s.re}', f'{s.y}ID{s.re}', f'{s.b}Items Count{s.re}'])
    t.align = "l"
    t.sortby = f"{s.y}ID{s.re}"

    for k in r: t.add_row([f'{s.g}{k["name"]}{s.re}', f'{s.y}{k["id"]}{s.re}', f'{s.b}{k["items_count"]}{s.re}'])
    print(t)

  def CheckModuleItems(class_id, module_id):
    print(s.re)
    url = f"{canvas_link}/{str(class_id)}/modules/{str(module_id)}/items"
    r = requests.get(url, headers=headers).json()

    module = requests.get(f"{canvas_link}/{str(class_id)}/modules/{str(module_id)}", headers=headers).json()

    t = PrettyTable([f"{s.g}Title{s.re}", f"{s.m}Type{s.re}", f"{s.y}ID{s.re}"])
    t.title = f'{s.b}{module["name"]}{s.re}'
    t.align = "l"
    t.sortby = f"{s.y}ID{s.re}"

    for k in r: t.add_row([f'{s.g}{k["title"]}{s.re}', f'{s.m}{k["type"]}{s.re}', f'{s.y}{k["id"]}{s.re}'])
    print(t)

  while True:
    system("clear")
    user_input = input(f'{s.m}1.{s.re} Get Courses\n{s.m}2.{s.re} Get Assignments\n{s.m}3.{s.re} Get Modules\n{s.m}4.{s.re} Get Module Data\nInput mode: {s.m}')
    if user_input.lower() in ('1', '2', '3', '4'):
      if user_input.lower() == '1': CheckCourses()
      if user_input.lower() == '2': CheckAssignments(input(f"{s.re}Input Course ID: {s.m}"))
      if user_input.lower() == '3': CheckModules(input(f"{s.re}Input Course ID: {s.m}"))
      if user_input.lower() == '4': CheckModuleItems(input(f"{s.re}Input Course ID: {s.m}"), input(f"{s.re}Input Module ID: {s.m}"))
      break
except: pass