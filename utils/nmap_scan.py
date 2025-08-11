import subprocess
import re

def run_nmap_scan(url):
    try:
        target = url.replace("http://", "").replace("https://", "").split("/")[0]
        command = ["nmap", "-F", target]
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        return {"output": result.stdout}
    except Exception as e:
        return {"error": str(e)}
