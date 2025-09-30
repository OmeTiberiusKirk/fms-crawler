import requests, re

if __name__ == "__main__":
    with requests.Session() as s:
        # Session automatically stores cookies for you
        r = s.get("http://192.168.2.41")

        # Extract _token hidden input
        m = re.search(r'name="_token".+value="([^"]+)"', r.text)
        token = m.group(1)

        payload = {"_token": token, "email": "user@example.com", "password": "user123"}

        # POST using the same session (cookies are kept automatically)
        r = s.post("http://192.168.2.41/auth", data=payload)
        # r2 = s.get('http://192.168.2.41/fta-monitoring-country')
    print(r)
