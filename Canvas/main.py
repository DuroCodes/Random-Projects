import json 
import requests
from os import system
from datetime import datetime
from prettytable import PrettyTable

secret = open("secret.json")
tokens = json.load(secret)
secret.close()

access_token = tokens["access_token"]
school_code = tokens["school_code"]

headers = {"Authorization": f"Bearer {access_token}"}
canvas_link = f"https://{school_code}.instructure.com/api/v1/courses"
check_date = datetime(day=datetime.now().day-1, month=datetime.now().month, year=datetime.now().year)

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
  url = f"{canvas_link}"
  r = requests.get(url, headers=headers).json()

  t = PrettyTable([f'{s.g}Name{s.re}', f'{s.y}ID{s.re}'])
  t.align[f'{s.g}Name{s.re}'] = "l"
  t.align[f'{s.y}ID{s.re}'] = "l"
  t.sortby = f'{s.y}ID{s.re}'

  for k in r: t.add_row([f'{s.g}{k.get("name",f"{s.r}Not Available")}{s.re}', f'{s.y}{k["id"]}{s.re}']) 
  print(t)
def CheckAssignments(class_id):
  print(s.re)
  url = f"{canvas_link}/{str(class_id)}/assignments?per_page=100"
  r = requests.get(url, headers=headers).json()

  t = PrettyTable([f'{s.g}Name{s.re}', f'{s.y}ID{s.re}', f'{s.b}Due Date{s.re}'])
  t.align[f'{s.g}Name{s.re}'] = "l"
  t.align[f'{s.y}ID{s.re}'] = "l"
  t.align[f'{s.b}Due Date{s.re}'] = "l"
  t.sortby = f'{s.b}Due Date{s.re}'

  for k in r: 
    due_time = k.get("due_at",f"{s.r}1969-01-01")
    if due_time is None: due_time = f"1969-01-01"
    due_date = datetime.strptime(due_time[:10], "%Y-%m-%d")
    if due_date >= check_date: t.add_row([f'{s.g}{k["name"]}{s.re}', f'{s.y}{k["id"]}{s.re}', f'{s.b}{k.get("due_at",f"{s.r}N/A")[:10]}{s.re}'+s.re])
  print(t)

while True:
  system("clear")
  user_input = input(f'{s.m}1.{s.re} Check Courses\n{s.m}2.{s.re} Check Assignments\nInput mode: {s.m}')
  if user_input.lower() in ('1', '2'):
    if user_input.lower() == '1': CheckCourses()
    if user_input.lower() == '2': CheckAssignments(input(f"{s.re}Input Course ID: {s.m}"))
    break