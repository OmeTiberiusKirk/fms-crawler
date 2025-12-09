import requests
import hints

config: hints.Config = {
    # "MDX_BASE_URL": "https://fms-mdx.dtn.go.th/jpivot/xmla",
    "MDX_BASE_URL": "http://1.1.253.130:8088/jpivot/xmla",
}

filename = "payloads.txt"

try:
    with open(filename, "r", encoding='utf-8') as file:
        print("-------- mdx crawler -------")
        r = 0
        for line in file:
            r += 1
            print("row =", r)
            resp = requests.post(
                f"{config['MDX_BASE_URL']}",
                headers={"Content-Type": "text/xml"},
                data=line.strip(),
            )
            print(f"status = {resp.status_code}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
