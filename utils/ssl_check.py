import socket
import ssl
from urllib.parse import urlparse

def check_ssl(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        port = parsed_url.port if parsed_url.port else 443

        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        return {
            "valid": True,
            "certificate": cert,
            "status": "success"
        }
    except Exception as e:
        return {
            "valid": False,
            "error": str(e),
            "status": "fail"
        }

