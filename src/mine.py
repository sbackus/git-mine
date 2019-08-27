import os
from github import Github

import datetime


def run():
    # connect to github
    g = Github(os.environ['GITHUB_ACCESS_TOKEN'])

    org_names = ["ps-dev", "pluralsight"]

    for org_name in org_names:
        org = g.get_organization(org_name)
        org_repos = org.get_repos()

        # count repos
        print(f'{org_name} repos:', org_repos.totalCount)

        # count commits
        print(f'{org_name} commits: {count_commits(org_repos)}')


def count_commits(repos_list):
    commit_count = 0
    print('counting commits')
    for repo in repos_list:
        print(commit_count, end="\r")
        a_year_ago = datetime.datetime.now() - datetime.timedelta(days=365)
        try:
            commit_count += repo.get_commits(since=a_year_ago).totalCount
        except Exception as e:
            print("Skipping repo: ", e)
    return commit_count


if __name__ == '__main__':
    run()
