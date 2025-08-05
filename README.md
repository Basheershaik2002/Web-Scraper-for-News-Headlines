# Web-Scraper-for-News-Headlines

# BBC News Headline Scraper App

This project is a **web scraping tool with a Streamlit frontend** that fetches the latest headlines from the BBC News homepage and displays them in a user-friendly interface.

 **Live App:** [Click here to try it live](https://pnua87dhg7lqb9rsgnah3g.streamlit.app/)

---

## Features

- Scrapes latest news headlines from [BBC News](https://www.bbc.com/news)
- Displays the headlines in a simple and clean web interface
- Saves the headlines to a local text file (`headlines.txt`)
- Built with:
  - `Python`
  - `BeautifulSoup` (for scraping)
  - `Requests`
  - `Streamlit` (for the web interface)

---

## 🛠How It Works

1. User opens the app via the Streamlit live link.
2. Clicks on **"Scrape BBC News Headlines"**.
3. The app sends a request to BBC News, scrapes the headline titles, and displays them in real-time.
4. Headlines are also saved to a file called `headlines.txt`.

---

## How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/news_scraper_app.git
   cd news_scraper_app
   
2.pip install -r requirements.txt

3.streamlit run news_app.py


