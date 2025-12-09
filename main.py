import requests
import re
import hints


config: hints.Config = {
    "WEB_BASE_URL": "https://fms.dtn.go.th",
    "EMAIL": "user@example.com",
    "PASS": "user123"
}

with requests.Session() as s:
    WEB_BASE_URL = 2
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
url = {url}
status = {r.status_code}
----------------------------
    """)

    url = f"{config['WEB_BASE_URL']}/fta-monitoring-country"
    r = s.get(url)
    print(f"""
fta-monitoring-country
url = {url}
status = {r.status_code}
----------------------------
    """)
