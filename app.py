from flask import Flask, render_template, request
from utils.headers_check import check_missing_headers
from utils.ssl_check import check_ssl
from utils.clickjacking_check import check_clickjacking
from utils.directory_listing_check import check_directory_listing
from utils.nmap_scan import run_nmap_scan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]

        results = {}
        results["headers"] = check_missing_headers(url)
        results["ssl"] = check_ssl(url)
        results["clickjacking"] = check_clickjacking(url)
        results["directory_listing"] = check_directory_listing(url)
        results["nmap"] = run_nmap_scan(url)

        return render_template("result.html", url=url, results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
