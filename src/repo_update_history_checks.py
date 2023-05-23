import pandas as pd
import datetime
from typing import List, Dict

class RepoUpdateHistoryChecker:
	
	
	REPO_UPDATE_CHECK_DATETIME_PERIODS = ["6hr", "12hr", "36hr", "60hr", "1dy", "2dy", "3dy", "5dy", "1wk", "2wk", "4wk", "8wk", "12wk"]
	
	
	@staticmethod
	def repos_updated_in_prev_Xhr(hours, repos: List[Dict]) -> List[Dict]:
		repos_updated_in_prev_Xhrs = []
		for repo_i in repos:
			if pd.Timestamp.utcnow() - pd.to_datetime(repo_i['pushed_at']) < pd.Timedelta(hours, "hours"):
				repos_updated_in_prev_Xhrs.append(repo_i)
		return repos_updated_in_prev_Xhrs
	
	
	@staticmethod
	def repos_updated_in_prev_6hr(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xhr(6, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_12hr(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xhr(12, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_36hr(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xhr(36, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_60hr(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xhr(60, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_Xdy(days, repos: List[Dict]) -> List[Dict]:
		repos_updated_in_prev_Xdays = []
		for repo_i in repos:
			if pd.Timestamp.utcnow() - pd.to_datetime(repo_i['pushed_at']) < pd.Timedelta(days, "days"):
				repos_updated_in_prev_Xdays.append(repo_i)
		return repos_updated_in_prev_Xdays
	
	
	@staticmethod
	def repos_updated_in_prev_1dy(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xdy(1, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_2dy(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xdy(2, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_3dy(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xdy(3, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_5dy(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xdy(5, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_Xwk(weeks, repos: List[Dict]) -> List[Dict]:
		repos_updated_in_prev_Xweeks = []
		for repo_i in repos:
			if pd.Timestamp.utcnow() - pd.to_datetime(repo_i['pushed_at']) < pd.Timedelta(weeks, "W"):
				repos_updated_in_prev_Xweeks.append(repo_i)
		return repos_updated_in_prev_Xweeks
	
	
	@staticmethod
	def repos_updated_in_prev_1wk(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xwk(1, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_2wk(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xwk(2, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_4wk(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xwk(4, repos)
	
	@staticmethod
	def repos_updated_in_prev_8wk(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xwk(8, repos)
	
	
	@staticmethod
	def repos_updated_in_prev_12wk(repos: List[Dict]) -> List[Dict]:
		return RepoUpdateHistoryChecker.repos_updated_in_prev_Xwk(12, repos)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
