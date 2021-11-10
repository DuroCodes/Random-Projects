import json, requests
from os import system
from datetime import datetime
from prettytable import PrettyTable
from pprint import pprint
try:
  secret = open("secret.json")
  tokens = json.load(secret)
  secret.close()

  access_token = tokens["access_token"]
  school_code = tokens["school_code"]

  headers = {"Authorization": f"Bearer {access_token}"}
  canvas_link = f"https://{school_code}.instructure.com/api/v1/courses"
  check_date = datetime(day=datetime.now().day-5, month=datetime.now().month, year=datetime.now().year)

  class c:
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
    print(c.re)
    url = f"{canvas_link}?per_page=100"
    r = requestc.get(url, headers=headers).json()

    t = PrettyTable([f'{c.g}Name{c.re}', f'{c.y}ID{c.re}'])
    t.align[f'{c.g}Name{c.re}'] = "l"
    t.align[f'{c.y}ID{c.re}'] = "l"
    t.sortby = f'{c.y}ID{c.re}'

    for k in r: t.add_row([f'{c.g}{k.get("name",f"{c.r}Not Available")}{c.re}', f'{c.y}{k["id"]}{c.re}']) 
    print(t)

  def CheckAssignments(class_id):
    print(c.re)
    url = f"{canvas_link}/{str(class_id)}/assignments?per_page=100"
    r = requestc.get(url, headers=headers).json()

    t = PrettyTable([f'{c.g}Name{c.re}', f'{c.y}ID{c.re}', f'{c.b}Due Date{c.re}'])
    t.align[f'{c.g}Name{c.re}'] = "l"
    t.align[f'{c.y}ID{c.re}'] = "l"
    t.align[f'{c.b}Due Date{c.re}'] = "l"
    t.sortby = f'{c.b}Due Date{c.re}'

    for k in r: 
      due_time = k.get("due_at",f"{c.r}1969-01-01")
      if due_time is None: due_time = f"1969-01-01"
      due_date = datetime.strptime(due_time[:10], "%Y-%m-%d")
      if due_date >= check_date: t.add_row([f'{c.g}{k["name"]}{c.re}', f'{c.y}{k["id"]}{c.re}', f'{c.b}{k.get("due_at",f"{c.r}N/A")[:10]}{c.re}'+c.re])
    print(t)
  def CheckModules(class_id):
    print(c.re)
    url = f"{canvas_link}/{str(class_id)}/modules"
    r = requestc.get(url, headers=headers).json()

    t = PrettyTable([f'{c.g}Name{c.re}', f'{c.y}ID{c.re}', f'{c.b}Items Count{c.re}'])
    t.align[f"{c.g}Name{c.re}"] = "l"
    t.align[f"{c.y}ID{c.re}"] = "l"
    t.align[f"{c.b}Items Count{c.re}"] = "l"
    t.sortby = f"{c.y}ID{c.re}"

    for k in r: t.add_row([f'{c.g}{k["name"]}{c.re}', f'{c.y}{k["id"]}{c.re}', f'{c.b}{k["items_count"]}{c.re}'])
    print(t)

  def CheckModuleItems(class_id, module_id):
    print(c.re)
    url = f"{canvas_link}/{str(class_id)}/modules/{str(module_id)}/items"
    r = requestc.get(url, headers=headers).json()

    module = requestc.get(f"{canvas_link}/{str(class_id)}/modules/{str(module_id)}", headers=headers).json()

    t = PrettyTable([f"{c.g}Title{c.re}", f"{c.m}Type{c.re}", f"{c.y}ID{c.re}"])
    t.title = f'{c.b}{module["name"]}{c.re}'
    t.align[f"{c.g}Title{c.re}"] = "l"
    t.align[f"{c.m}Type{c.re}"] = "l"
    t.align[f"{c.y}ID{c.re}"] = "l"
    t.sortby = f"{c.y}ID{c.re}"

    for k in r: t.add_row([f'{c.g}{k["title"]}{c.re}', f'{c.m}{k["type"]}{c.re}', f'{c.y}{k["id"]}{c.re}'])
    print(t)

  while True:
    system("clear")
    user_input = input(f'{c.m}1.{c.re} Get Courses\n{c.m}2.{c.re} Get Assignments\n{c.m}3.{c.re} Get Modules\n{c.m}4.{c.re} Get Module Data\nInput mode: {c.m}')
    if user_input.lower() in ('1', '2', '3', '4'):
      if user_input.lower() == '1': CheckCourses()
      if user_input.lower() == '2': CheckAssignments(input(f"{c.re}Input Course ID: {c.m}"))
      if user_input.lower() == '3': CheckModules(input(f"{c.re}Input Course ID: {c.m}"))
      if user_input.lower() == '4': CheckModuleItems(input(f"{c.re}Input Course ID: {c.m}"), input(f"{c.re}Input Module ID: {c.m}"))
      break
except: pass