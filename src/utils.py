import time
import constants
import requests



def search_repositories_by_topic(topic: str, sort_mode="", order_mode="desc"):
	topic_repos_search_url = f"{constants.GITHUB_API_BASE_URL}/search/repositories?q={topic}"
	if order_mode.lower() not in ["desc", "asc"]:
		raise Exception("The results ordering order_mode parameter only accepts 'desc' & 'asc' as input argument!")
	else:
		if sort_mode.lower() in ["", "stars", "forks", "updated"]:
			response = requests.get(f"{topic_repos_search_url}&sort={sort_mode.lower()}&order={order_mode.lower()}&per_page=100")
		else:
			raise Exception("The results sorting sort_mode parameter only accepts 'stars', 'forks' & 'updated' as input argument!")
	return response



def search_repositories_by_topicV2(topic: str, sort_mode="", order_mode="desc", return_mode=None):
	results = []
	topic_repos_search_url = f"{constants.GITHUB_API_BASE_URL}/search/repositories?q={topic}"
	if order_mode.lower() not in ["desc", "asc"]:
		raise Exception("The results ordering order_mode parameter only accepts 'desc' & 'asc' as input argument!")
	else:
		if sort_mode.lower() in ["", "stars", "forks", "updated"]:
			response = requests.get(f"{topic_repos_search_url}&sort={sort_mode.lower()}&order={order_mode.lower()}&per_page=100")
			# print(f"{response.json()['total_count']}: response.json()['total_count]")
		else:
			raise Exception("The results sorting sort_mode parameter only accepts 'stars', 'forks' & 'updated' as input argument!")
	if response.json()['total_count'] > 100:
		results_cnt = response.json()['total_count']
		min_rate_limit = 30
		min_rate_cnt = 0
		results_retrieved = 0
		# results = []
		# while results_retrieved < response.json()['total_count']:
		while results_retrieved <= 1000:
			results_retrieved += 100
			min_rate_cnt += 1
			response_i = requests.get(f"{topic_repos_search_url}&sort={sort_mode.lower()}&order={order_mode.lower()}&per_page=100&page={min_rate_cnt}")
			# print(f"response_i.json(): {response_i.json()}")
			if return_mode is None:
				results.append(response_i)
			else:
				if return_mode == "json":
					results.append(response_i.json())
				elif return_mode == "items":
					results.append(response_i.json()["items"])
				elif return_mode == "total_count":
					results.append(response_i.json()["total_count"])
			if min_rate_cnt % 5 == 0:
				time.sleep(10)
		# return results
	
	else:
		if return_mode is None:
			results = response
		else:
			if return_mode == "json":
				results = response.json()
			elif return_mode == "items":
				results = response.json()["items"]
			elif return_mode == "total_count":
				results = response.json()["total_count"]
	
	return results
	# return response.json()["items"]

# search_repositories_by_topicV2("compliance")
