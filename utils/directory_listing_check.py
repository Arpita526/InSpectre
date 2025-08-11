import requests
from bs4 import BeautifulSoup

def check_directory_listing(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        response = requests.get(url, timeout=5)
        if "Index of /" in response.text:
            return {"listing_enabled": True}
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.title and "Index of" in soup.title.text:
            return {"listing_enabled": True}
        return {"listing_enabled": False}
    except Exception as e:
        return {"error": str(e)}
