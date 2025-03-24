import requests
import time


base_url = "http://35.200.185.69:8000/v1/autocomplete"

queries = [chr(i) for i in range(97, 123)]  # ie ['a', 'b', ..., 'z']
collected_names = set()
request_count = 0

for query in queries:
    page = 1
    while True:
        request_count += 1
        url = f"{base_url}?query={query}&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            names = data.get("results", [])

            if not names:
                break

            collected_names.update(names)
            print(f"Query '{query}', Page {page} → Found: {names}")
        else:
            print(f"Error! Status: {response.status_code}")
            break

        page += 1
        time.sleep(1)  # rate limiting prevent

print(f"✅ Total API requests: {request_count}")
print(f"✅ Total unique names extracted: {len(collected_names)}")
