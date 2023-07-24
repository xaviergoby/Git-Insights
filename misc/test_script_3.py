import requests

def count_regtech_repositories():
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "topic:regtech",
        "sort": "stars",
        "order": "desc"
    }
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        total_count = data["total_count"]
        print(f"Total RegTech repositories: {total_count}")
    else:
        print("Error occurred while fetching data.")

count_regtech_repositories()
