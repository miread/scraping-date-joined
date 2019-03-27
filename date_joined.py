from bs4 import BeautifulSoup
import requests
import re

def get_member_since(username):
    page = requests.get("https://www.codewars.com/users/" + username).text
    soup = BeautifulSoup(page)
    stats = ''.join(str(soup.findAll('div', class_='stat')))
    pattern = re.compile(r'(Member Since:</b>)([\w\s]+)(</div>)')
    match = pattern.finditer(stats)
    for m in match:
        return m.group(2)
