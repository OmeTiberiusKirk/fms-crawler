import requests
import hints
from dotenv import dotenv_values

if __name__ == "__main__":
    filename = "payloads.txt"
    config: hints.Config = dotenv_values(".env")

    try:
        with open(filename, "r") as file:
            for line in file:
                resp = requests.post(
                    f"{config['MDX_BASE_URL']}:8080/jpivot/xmla",
                    headers={"Content-Type": "text/xml"},
                    data=line.strip(),
                )
                print(f"url: {resp.url}")
                print(f"status: {resp.status_code}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
