import requests
import pandas as pd
import datetime
from typing import List, Dict
from src.repo_update_history_checks import RepoUpdateHistoryChecker
from src import utils


class GitInsights:
	"""
	This purpose of this cls is ONLY for RETRIEVING data from GitHub, not
	acting as a container for the data is retrieved from GitHub!
	"""
	
	@staticmethod
	def categorise_repos_by_update_dt(repos: List[Dict]):
		unique_update_dt_period_cnt = 0
		dt_categories = {}
		repo_dt_period_check_keys = RepoUpdateHistoryChecker.REPO_UPDATE_CHECK_DATETIME_PERIODS
		
		repo_update_dt_period_check_func_names = [func_name for func_name, func_obj in RepoUpdateHistoryChecker.__dict__.items() if func_name.split("_")[-1] in repo_dt_period_check_keys and callable(func_obj)]
		for func_name in repo_update_dt_period_check_func_names:
			repo_update_dt_period_check_func = getattr(RepoUpdateHistoryChecker, func_name)
			# dt_categories[func_name.split('_')[-1]] = repo_update_dt_period_check_func(repos)
			res = repo_update_dt_period_check_func(repos)
			dt_categories[func_name.split('_')[-1]] = [repo_i["id"] for repo_i in res if repo_i["id"] not in [v for vals in dt_categories.values() for v in vals]]
		return dt_categories
	

gitinsights = GitInsights()


# topic1 = "regtech"
# topic1 = "eurlex"
topic1 = "compliance"
# topic1_latest_res = utils.search_repositories_by_topicV2(topic1, sort_mode="updated")
topic1_latest_res = utils.search_repositories_by_topicV2(topic1)

# res = gitinsights.categorise_repos_by_update_dt(topic1_latest_res.json()["items"])
res = gitinsights.categorise_repos_by_update_dt(topic1_latest_res)

print(res)
print([len(v) for k,v, in res.items()])
print(sum([len(v) for k,v, in res.items()]))

