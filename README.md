
# BBC News Headline Scraper App

This project is a **web scraping tool with a Streamlit frontend** that fetches the latest headlines from the BBC News homepage and displays them in a user-friendly interface.

 **Live App:** [Click here to try it live](https://pnua87dhg7lqb9rsgnah3g.streamlit.app/)

---

## Features

- Scrapes latest news headlines from [BBC News](https://www.bbc.com/news)
- Displays the headlines in a simple and clean web interface
- Saves the headlines to a local text file (`headlines.txt`)
- Built with:
Streamlit which helped me deploy the task.
---

## How It Works

1. User opens the app via the Streamlit live link.
2. Clicks on **"Scrape BBC News Headlines"**.
3. The app sends a request to BBC News, scrapes the headline titles, and displays them in real-time.
4. Headlines are also saved to a file called `headlines.txt`.

---


### Technologies Used
Python

Streamlit

BeautifulSoup

Requests

### Output

The app scrapes the latest BBC News headlines when you click "Scrape News".

Headlines are displayed instantly in the web app and saved to headlines.txt.

Around 60–70 current headlines are fetched and stored, one per line.


