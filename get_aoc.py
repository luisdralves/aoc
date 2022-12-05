from datetime import datetime
from dotenv import load_dotenv
import os
import sys
import requests
import pytz

load_dotenv()

EST = pytz.timezone('America/New_York')
now = datetime.now(EST)

day = now.day
year = now.year

try:
    day = sys.argv[1]
    year = sys.argv[2]
except:
    pass


url = f'https://adventofcode.com/{year}/day/{day}/input'
headers = {
    "Cookie": f"session={os.environ.get('COOKIE_SESSION')}"
}
print(headers)

response = requests.get(url, headers=headers)
if not os.path.exists(str(year)):
    os.makedirs(str(year))

with open(f"{year}/{day}.txt", "w") as f:
    f.write(response.text)

if not os.path.isfile(f"{year}/{day}.py"):
    with open(f"{year}/{day}.py", "w") as f:
        f.write(f"""
total = 0

with open('{day}.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        total += len(line)

print(total)    
        """)
