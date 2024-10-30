import requests
from bs4 import BeautifulSoup

# doc_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
doc_url = "https://docs.google.com/document/d/e/2PACX-1vShuWova56o7XS1S3LwEIzkYJA8pBQENja01DNnVDorDVXbWakDT4NioAScvP1OCX6eeKSqRyzUW_qJ/pub"

def decode_secret_message(doc_url):
    response = requests.get(doc_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')
    
    data = []
    max_x, max_y = 0, 0
    
    for row in rows[1:]:
        columns = row.find_all('td')
        if len(columns) < 3:
            continue
        
        x = int(columns[0].text.strip())
        char = columns[1].text.strip()
        y = int(columns[2].text.strip())
        
        data.append((x, y, char))
        
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    for x, y, char in data:
        grid[y][x] = char
    
    for row in reversed(grid):
        print("".join(row))

decode_secret_message(doc_url)
