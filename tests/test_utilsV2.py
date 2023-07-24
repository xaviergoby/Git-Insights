import pandas as pd
from src import utils
import requests



def test_search_repositories_by_topicV2(topic):
	responses = utils.search_repositories_by_topicV2(topic, return_mode=None)
	results_items = responses.json()["items"]
	print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Topic: {topic} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print(f"       ~~~~~~~~~~~~~~~ 'Best match' search results - Item 0 ~~~~~~~~~~~~~~~     ")
	print(f'            ~~~~~~~~~~      Total items retrieved: {responses.json()["total_count"]}      ~~~~~~~~~~')
	print(f"Created_at: {results_items[0]['created_at']}")
	print(f"Updated_at: {results_items[0]['updated_at']}")
	print(f"Pushed_at: {results_items[0]['pushed_at']}")
	print(f"Topics: {results_items[0]['topics']}")
	print(f"Language: {results_items[0]['language']}")
	print(f"Time since last push (incl. commit): {pd.Timestamp.utcnow() - pd.to_datetime(results_items[0]['pushed_at'])}")


def test_search_latest_updated_sorted_repositories_by_topicV2(topic):
	responses = utils.search_repositories_by_topicV2(topic, sort_mode="updated", order_mode="desc", return_mode="json")
	if isinstance(responses, list):
		print(f"responses: {len(responses)}")
		print(f"responses items total_count's: {[items_set_i['total_count'] for items_set_i in responses]}")
	results_items = responses["items"]
	print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Topic: {topic} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print(f"       ~~~~~~~~~~~~~~~ Latest 'pushed' search results - Item 0 ~~~~~~~~~~~~~~~     ")
	print(f'            ~~~~~~~~~~      Total items retrieved: {responses["total_count"]}      ~~~~~~~~~~')
	print(f"Created_at: {results_items[0]['created_at']}")
	print(f"Updated_at: {results_items[0]['updated_at']}")
	print(f"Pushed_at: {results_items[0]['pushed_at']}")
	print(f"Topics: {results_items[0]['topics']}")
	print(f"Language: {results_items[0]['language']}")
	print(f"Time since last push (incl. commit): {pd.Timestamp.utcnow() - pd.to_datetime(results_items[0]['pushed_at'])}")


if __name__ == "__main__":
	topic = "regtech"
	
	test_search_repositories_by_topicV2(topic)
	test_search_latest_updated_sorted_repositories_by_topicV2(topic)


	
	print(f"\n")
	print(f"\n")
	print(f"\n")
	created_at = utils.search_repositories_by_topicV2(topic, return_mode=None).json()["items"][0]["created_at"]
	created_at_dt = pd.to_datetime(created_at, utc=True)
	pushed_at = utils.search_repositories_by_topicV2(topic, return_mode=None).json()["items"][0]["pushed_at"]
	pushed_at_dt = pd.to_datetime(created_at, utc=True)
	
	
	created_at = utils.search_repositories_by_topicV2(topic, return_mode=None).json()["items"][0]["created_at"]
	created_at_dt = pd.to_datetime(created_at, utc=False)
	pushed_at = utils.search_repositories_by_topicV2(topic, return_mode=None).json()["items"][0]["pushed_at"]
	pushed_at_dt = pd.to_datetime(pushed_at, utc=False)
	print(f"\n")
	print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print(f"~~~~~ Created At Time ~~~~~")
	# print(f"Created At Time")
	print(f'GitHub: <relative-time datetime="2020-11-02T17:58:24Z" <...> title="Nov 2, 2020, 6:58 PM GMT+1">'
		  f'\nGitHub API "created_at" OG val: {created_at}'
		  f'\ntz_convert("Europe/Amsterdam"): {created_at_dt.tz_convert("Europe/Amsterdam")}')
	print(f"\n")
	print(f"~~~~~ Pushed At Time ~~~~~")
	# print(f"~~~~~")
	# print(f"Pushed At Time")
	print(f'GitHub: <relative-time datetime="2021-07-07T14:23:52Z" <...> title="Jul 7, 2021, 4:23 PM GMT+2">'
		  f'\nGitHub API "pushed_at" OG val: {pushed_at}'
		  f'\ntz_convert("Europe/Amsterdam"): {pushed_at_dt.tz_convert("Europe/Amsterdam")}')
