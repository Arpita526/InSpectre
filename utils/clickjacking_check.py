import requests

def check_clickjacking(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        response = requests.get(url, timeout=5)
        xfo = response.headers.get("X-Frame-Options", None)
        if xfo:
            return {"protected": True, "value": xfo}
        else:
            return {"protected": False, "message": "X-Frame-Options header missing"}
    except Exception as e:
        return {"error": str(e)}
