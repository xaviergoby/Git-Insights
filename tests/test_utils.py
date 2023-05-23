import pandas as pd
from src import utils



# no sorting (def sorting via bestmatch) & no order (def ordering is desc)
# topic1 = "regtech"
topic1 = "compliace"
# https://github.com/search?q=regtech&type=repositories&s=&o=desc
# https://api.github.com/search/repositories?q=regtech&order=desc
topic1_def_res = utils.search_repositories_by_topic(topic1)

# https://github.com/search?q=regtech&type=repositories&s=updated&o=desc
# https://api.github.com/search/repositories?q=regtech&sort=updated&order=desc
topic1_latest_res = utils.search_repositories_by_topic(topic1, sort_mode="updated")

# pre-manual GitHub search gives 70 reults for repo's with "regtech" as a topic

print(topic1_def_res.json()["total_count"])
print(topic1_latest_res.json()["total_count"])


print(f"\nDef settings search results - Item 0")
print(f"created_at: {topic1_def_res.json()['items'][0]['created_at']}")
print(f"updated_at: {topic1_def_res.json()['items'][0]['updated_at']}")
print(f"pushed_at: {topic1_def_res.json()['items'][0]['pushed_at']}")
print(f"topics: {topic1_def_res.json()['items'][0]['topics']}")
print(f"language: {topic1_def_res.json()['items'][0]['language']}")

print(f"\nLatest updated search results - Item 0")
print(f"created_at: {topic1_latest_res.json()['items'][0]['created_at']}")
print(f"updated_at: {topic1_latest_res.json()['items'][0]['updated_at']}")
print(f"pushed_at: {topic1_latest_res.json()['items'][0]['pushed_at']}")
print(f"topics: {topic1_latest_res.json()['items'][0]['topics']}")
print(f"language: {topic1_latest_res.json()['items'][0]['language']}")


print(pd.Timestamp.utcnow() - pd.to_datetime(topic1_latest_res.json()['items'][0]['pushed_at']))
print(pd.Timestamp.utcnow() - pd.to_datetime(topic1_latest_res.json()['items'][1]['pushed_at']))

