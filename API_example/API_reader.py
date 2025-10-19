import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com/"
response = requests.get(url, timeout=15)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

quotes = []
for quote_block in soup.select(".quote"):
    text = quote_block.select_one(".text").get_text(strip=True)
    author = quote_block.select_one(".author").get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in quote_block.select(".tags .tag")]
    quotes.append({"Quote": text, "Author": author, "Tags": ", ".join(tags)})

df = pd.DataFrame(quotes)
print(df)
df.to_csv("quotes.csv", index=False)
