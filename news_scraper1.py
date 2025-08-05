# news_scraper.py

import requests
from bs4 import BeautifulSoup

# ✅ Step 1: Target news website URL
url = 'https://www.bbc.com/news'  # You can change this to any news site

try:
    # ✅ Step 2: Send GET request to fetch HTML content
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request fails

    # ✅ Step 3: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # ✅ Step 4: Find all headline tags (h1, h2, h3)
    headlines = soup.find_all(['h1', 'h2', 'h3'])

    # ✅ Step 5: Save the headlines into a .txt file
    with open('headlines.txt', 'w', encoding='utf-8') as file:
        count = 0
        for headline in headlines:
            text = headline.get_text().strip()
            if text:  # Only write non-empty lines
                file.write(text + '\n')
                count += 1

    print(f"✅ {count} headlines saved to 'headlines.txt'")

except requests.RequestException as e:
    print("❌ Failed to fetch the webpage. Error:", e)
except Exception as ex:
    print("❌ An error occurred:", ex)
