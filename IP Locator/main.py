import json, requests
from os import system
import pyfiglet
from prettytable import PrettyTable

class colors:
  black='\033[30m'
  red='\033[31m'
  green='\033[32m'
  blue='\033[34m'
  purple='\033[35m'
  cyan='\033[36m'
  lightgrey='\033[37m'
  darkgrey='\033[90m'
  lightred='\033[91m'
  lightgreen='\033[92m'
  yellow='\033[93m'
  lightblue='\033[94m'
  pink='\033[95m'
  lightcyan='\033[96m'
  reset='\033[0m'

system("clear")

theme = [colors.cyan, colors.blue]
title = pyfiglet.figlet_format("ip locator", font="ansi_shadow").split("\n")

for i in range(len(title)-2):
  i2 = 0 if i%2 == 0 else 1
  print(f'{theme[i2]}{title[i]}')

ip = input(f"Input an IP: {theme[0]}")
r = requests.get(f"https://geolocation-db.com/json/{ip}").json()
system("clear")

information = {
  0: ("IP", f'{r.get("ipv4","Not Available")}'),
  1: ("Country", f'{r["country_name"]} ({r["country_code"]})'),
  2: ("State", f'{r["state"]}'),
  3: ("City", f'{r["city"]}'),
  4: ("Postal", f'{r["postal"]}'),
  5: ("Coordinates", f'{r["latitude"]}, {r["longitude"]}')
}

t = PrettyTable([f"{theme[1]}Key{colors.reset}", f"{theme[0]}Data{colors.reset}"])
t.header = False
t.align = "l"

print(colors.reset)

for i in range(len(information)): t.add_row([f'{theme[1]}{information[i][0]}{colors.reset}', f'{theme[0]}{information[i][1]}{colors.reset}'])

print(t)