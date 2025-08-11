import requests

def check_missing_headers(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        response = requests.get(url, timeout=5)
        security_headers = [
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-XSS-Protection"
        ]
        missing = [header for header in security_headers if header not in response.headers]
        return {"missing": missing, "status": "success"}
    except Exception as e:
        return {"error": str(e), "status": "fail"}
