import requests, re
from dotenv import dotenv_values
import hints

if __name__ == "__main__":
    config: hints.Config = dotenv_values(".env")

    with requests.Session() as s:
        # Session automatically stores cookies for you
        r = s.get(config["WEB_BASE_URL"])

        # Extract _token hidden input
        m = re.search(r'name="_token".+value="([^"]+)"', r.text)
        token = m.group(1)

        payload = {
            "_token": token,
            "email": config["EMAIL"],
            "password": config["PASS"],
        }

        # POST using the same session (cookies are kept automatically)
        r = s.post(f"{config['WEB_BASE_URL']}/auth", data=payload)
        print(f"url: {r.url}")
        print(f"status: {r.status_code}")

        r = s.get(f"{config['WEB_BASE_URL']}/fta-monitoring-country")
        print(f"url: {r.url}")
        print(f"status: {r.status_code}")

