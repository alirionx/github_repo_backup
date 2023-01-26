from tool import RepoGetter

#-------------------------------------------------------------
if __name__ == "__main__":
  myRepoGetter = RepoGetter()
  myRepoGetter.get_repos_list()
  myRepoGetter.batch_download_repos(print_info=True)

#-------------------------------------------------------------