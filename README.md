# git-mine

A project to understand what percentage of code in an organization is open source and what percent is 'mine'(not open source).

![MINE](https://farm4.staticflickr.com/3206/2840734419_049c2c9ca6_b.jpg)

## How to mine

Create a github developer access token:
https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line

export GITHUB_ACCESS_TOKEN='your github access token here'

pip install -r requirements.txt

python src/mine.py
