from pathlib import Path
import praw
import os
import requests

# Setting up the Reddit API with the praw module.
# API info is set up with your reddit account.
reddit = praw.Reddit(
    client_id='YOUR CLIENT ID',
    client_secret='YOUR SECRET',
    user_agent='SOME STRING',
)

# Sets up the variable for the Directory Windows is set
# to look for when changing Wallpapers and then sets the
# current working directory
wallpaperDir = Path('Your Dir')
os.chdir(wallpaperDir)

# With the Reddit instance made we use the subreddit
# method to pull our pictures, note you do not need to at the r/
# Subreddits have methods to pull either Top, Hot and New.
# You can also set the attribute Limit how many posts it pulls.
# finally it iterates over the posts and saves them to the Dir.
for i in reddit.subreddit("EarthPorn").hot(limit=30):
    res = requests.get(i.url)
    res.raise_for_status()
    tmpFile = open(i.name + '.jpg', 'wb')
    for chunk in res.iter_content(50000):
        tmpFile.write(chunk)
    tmpFile.close()

