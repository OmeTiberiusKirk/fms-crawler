import requests
import re
import hints


config: hints.Config = {
    "WEB_BASE_URL": "https://fms.dtn.go.th",
    # "WEB_BASE_URL": "http://127.0.0.1",
    "EMAIL": "user@example.com",
    "PASS": "user123"
}


def createSession(s: requests.Session):
    # Session automatically stores cookies for you
    r = s.get(config["WEB_BASE_URL"])
    # Extract _token hidden input
    m = re.search(r'name="_token".+value="([^"]+)"', r.text)
    token = m.group(1)
    print(f"""
get token
url = {r.request.url}
token = {token}
status = {r.status_code}
----------------------------
    """)

    payload = {
        "_token": token,
        "email": config["EMAIL"],
        "password": config["PASS"],
    }
    url = f"{config['WEB_BASE_URL']}/auth"
    # POST using the same session (cookies are kept automatically)
    r = s.post(url, data=payload)
    print(f"""
signin
url = {url} --> {r.url}
status = {r.status_code}
----------------------------
    """)


pages = ("fta-monitoring-country", "fta-monitoring-product")

with requests.Session() as s:
    createSession(s)
    for p in pages:
        url = f"{config['WEB_BASE_URL']}/{p}"
        r = s.get(url)
        print(f"""
{p}
url = {url}
status = {r.status_code}
----------------------------
        """)
