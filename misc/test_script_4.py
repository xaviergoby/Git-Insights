import requests

def count_regtech_repositories():
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "regtech in:description",
        "sort": "stars",
        "order": "desc",
        "per_page": 100
    }
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    total_count = 0
    page = 1
    while True:
        params["page"] = page
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            items = data["items"]
            total_count += len(items)
            if len(items) < 100:
                break
            page += 1
        else:
            print("Error occurred while fetching data.")
            break

    print(f"Total RegTech repositories: {total_count}")

count_regtech_repositories()



# https://github.com/search?q=eurlex&type=repositories&s=updated&o=desc

# &sort=stars&order=desc

# https://api.github.com/search/repositories?q=eurlex&s=updated&o=desc

# https://stackoverflow.com/questions/40762518/github-api-sorting-search-results-by-the-created-at-field
# https://api.github.com/search/repositories?q=eurlex&sort=stars&order=desc

# https://api.github.com/search/repositories?q=eurlex&sort=updated&order=desc




