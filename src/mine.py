import os
import getpass
from github import Github

def run():
    try:
        # using an access token
        github_access_token = os.environ['GITHUB_ACCESS_TOKEN']
        g = Github(github_access_token)
    except:
        # create a github instance
        # g = Github("user", "password")
        print("Could not connect to github: no access token found.")
        print("Try using username and password.")

        username = input("Enter github username: ")
        password = getpass.getpass(prompt='Enter your github password: ')
        g = Github(username, password)

    # # Then play with your Github objects:
    # for repo in g.get_user().get_repos():
    #     print(repo.name)

    org_names = ["ps-dev", "pluralsight"]

    for org_name in org_names:

        org = g.get_organization(org_name)

        org_repos = org.get_repos()
        print(f'{org_name} repos:', org_repos.totalCount)

        org_commits = count_commits(org_repos)
        print(f'{org_name} commits: {org_commits}')




def count_commits(repos_list):
    commit_count = 0
    print('counting commits')
    for repo in repos_list:
        print(commit_count, end="\r")
        try:
            commit_count += repo.get_commits().totalCount
        except Exception as e:
            print("skipping repo", e)
    return commit_count



if __name__ == '__main__':
    run()
