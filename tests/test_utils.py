import pandas as pd
from src import utils


def test_search_repositories_by_topicV2(topic):
	responses = utils.search_repositories_by_topicV2(topic, return_mode=None)
	results_items = responses.json()["items"]
	print(f"\nLatest updated search results - Item 0")
	print(f'Total retrieved items count: {responses.json()["total_count"]}')
	print(f"created_at: {results_items[0]['created_at']}")
	print(f"updated_at: {results_items[0]['updated_at']}")
	print(f"pushed_at: {results_items[0]['pushed_at']}")
	print(f"topics: {results_items[0]['topics']}")
	print(f"language: {results_items[0]['language']}")
	print(f"Time since last performed push (& w/ commit incl. ofc.): {pd.Timestamp.utcnow() - pd.to_datetime(results_items[0]['pushed_at'])}")
	print(f"Time since last performed push (& w/ commit incl. ofc.): {pd.Timestamp.utcnow() - pd.to_datetime(results_items[1]['pushed_at'])}")


def test_search_latest_updated_sorted_repositories_by_topicV2(topic):
	responses = utils.search_repositories_by_topicV2(topic, sort_mode="updated", order_mode="desc", return_mode="items")
	# responses = utils.search_repositories_by_topicV2(topic, return_mode=None)
	results_items = responses.json()["items"]
	# var_opt2_items = res_var_opt2.json()["items"]
	print(f"\nLatest updated search results - Item 0")
	print(f'Total retrieved items count: {responses.json()["total_count"]}')
	print(f"created_at: {results_items[0]['created_at']}")
	print(f"updated_at: {results_items[0]['updated_at']}")
	print(f"pushed_at: {results_items[0]['pushed_at']}")
	print(f"topics: {results_items[0]['topics']}")
	print(f"language: {results_items[0]['language']}")
	print(f"Time since last performed push (& w/ commit incl. ofc.): {pd.Timestamp.utcnow() - pd.to_datetime(results_items[0]['pushed_at'])}")
	print(f"Time since last performed push (& w/ commit incl. ofc.): {pd.Timestamp.utcnow() - pd.to_datetime(results_items[1]['pushed_at'])}")
	

# no sorting (def sorting via bestmatch) & no order (def ordering is desc)
# topic1 = "regtech"
topic1 = "compliace"
# https://github.com/search?q=regtech&type=repositories&s=&o=desc
# https://api.github.com/search/repositories?q=regtech&order=desc
topic1_def_res = utils.search_repositories_by_topic(topic1)
topic1_def_resV2 = utils.search_repositories_by_topicV2(topic1)

# https://github.com/search?q=regtech&type=repositories&s=updated&o=desc
# https://api.github.com/search/repositories?q=regtech&sort=updated&order=desc
topic1_latest_res = utils.search_repositories_by_topic(topic1, sort_mode="updated")
topic1_latest_resV2 = utils.search_repositories_by_topicV2(topic1, sort_mode="updated")

# pre-manual GitHub search gives 70 reults for repo's with "regtech" as a topic

print(f'Total retrieved items count: {topic1_def_res.json()["total_count"]}')
# print(f'Total retrieved items count: {topic1_def_resV2.json()["total_count"]}')
print(f'Total retrieved items count: {topic1_latest_res.json()["total_count"]}')
# print(f'Total retrieved items count: {topic1_latest_resV2.json()["total_count"]}')

##################
res_var_opt1 = topic1_def_resV2
res_var_opt2 = topic1_latest_resV2

var_opt1_items = res_var_opt1.json()["items"]
var_opt2_items = res_var_opt2.json()["items"]

print(f"\nDef settings search results - Item 0")
print(f'Total retrieved items count: {res_var_opt1.json()["total_count"]}')
print(f"created_at: {var_opt1_items[0]['created_at']}")
print(f"updated_at: {var_opt1_items[0]['updated_at']}")
print(f"pushed_at: {var_opt1_items[0]['pushed_at']}")
print(f"topics: {var_opt1_items[0]['topics']}")
print(f"language: {var_opt1_items[0]['language']}")
print(f"Time since last performed push (& w/ commit incl. ofc.): {pd.Timestamp.utcnow() - pd.to_datetime(var_opt1_items[0]['pushed_at'])}")
print(f"Time since last performed push (& w/ commit incl. ofc.): {pd.Timestamp.utcnow() - pd.to_datetime(var_opt1_items[1]['pushed_at'])}")

print(f"\nLatest updated search results - Item 0")
print(f'Total retrieved items count: {res_var_opt2.json()["total_count"]}')
print(f"created_at: {var_opt2_items[0]['created_at']}")
print(f"updated_at: {var_opt2_items[0]['updated_at']}")
print(f"pushed_at: {var_opt2_items[0]['pushed_at']}")
print(f"topics: {var_opt2_items[0]['topics']}")
print(f"language: {var_opt2_items[0]['language']}")
print(f"Time since last performed push (& w/ commit incl. ofc.): {pd.Timestamp.utcnow() - pd.to_datetime(var_opt2_items[0]['pushed_at'])}")
print(f"Time since last performed push (& w/ commit incl. ofc.): {pd.Timestamp.utcnow() - pd.to_datetime(var_opt2_items[1]['pushed_at'])}")



