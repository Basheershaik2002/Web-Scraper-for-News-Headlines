import streamlit as st
import subprocess
import os

# Set page settings
st.set_page_config(page_title="📰 BBC News Scraper", layout="centered")
st.title("📰 BBC News Headline Scraper")
st.markdown("Click the button below to fetch the latest headlines from BBC News.")

# Run scraper when button is clicked
if st.button("Scrape News Headlines"):
    with st.spinner("Scraping in progress..."):
        result = subprocess.run(
            ["python", "news_scraper.py"],
            capture_output=True,
            text=True
        )
        st.success("✅ Scraping complete!")
        st.code(result.stdout)

# Display scraped headlines
if os.path.exists("headlines.txt"):
    with open("headlines.txt", "r", encoding="utf-8") as file:
        headlines = file.readlines()
        if headlines:
            st.subheader("🗞️ Latest Headlines")
            for i, headline in enumerate(headlines, 1):
                st.write(f"{i}. {headline.strip()}")
        else:
            st.warning("No headlines found in the file.")
else:
    st.info("Click the scrape button to generate headlines.")
